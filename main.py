#coding:utf-8
from datetime import datetime
from sklearn.model_selection import KFold
from sklearn.metrics import roc_auc_score
import xgboost as xgb
import pandas as pd
from sklearn.feature_extraction import DictVectorizer
from transformer import *
from config import getParam
import sys
from feature_map import *

def main():
    #Get param
    param = getParam()
    ID = param['ID']
    label = param['label']

    #Load data
    train = pd.read_csv('data/' + str(param['train_file']), encoding='u8')
    test = pd.read_csv('data/' + str(param['test_file']), encoding='u8')

    #Drop features
    drop_list = param['drop_list']
    df_train = train.drop(drop_list, axis=1)
    df_test = test.drop(drop_list, axis=1)

    #Assign feature and label
    selected_cols = df_train.columns[(df_train.columns != ID) & (df_train.columns != label)]
    X_train, X_test = df_train.loc[:, selected_cols], df_test.loc[:, selected_cols]
    Y_train, Y_test = df_train[label], df_test[label]
    
    #Fillna
    X_train = naTransformer(X_train)
    X_test = naTransformer(X_test)

    #Deal with Date feature
    date_cols = param['date_cols']
    X_train = dateTransformer(X_train, date_cols)
    X_test = dateTransformer(X_test, date_cols)

    #Deal with Category Feature
    dict_train = X_train.to_dict(orient='records')
    dict_test = X_test.to_dict(orient='records')
    vectorizer = DictVectorizer()
    vec_train = vectorizer.fit_transform( dict_train )
    vec_test = vectorizer.transform( dict_test ) 
    
    #Store the feature names
    features = vectorizer.feature_names_
    feature_map('xgb'+str(sys.argv[2])+'.fmap', features)

    #Cross validation
    kf = KFold(n_splits=5, shuffle=True) 
    output_test = pd.DataFrame()
    for train_index, val_index in kf.split(Y_train):
        #print("TRAIN:", train_index, "VAL:", val_index)
        feature_train, feature_val = vec_train[train_index, :], vec_train[val_index, :]
        label_train, label_val = Y_train[train_index], Y_train[val_index]
            
        ###XGBOOST Model
        dtrain = xgb.DMatrix(feature_train, label=label_train)
        dval = xgb.DMatrix(feature_val, label=label_val)
        #dtest = xgb.DMatrix(vec_test, label=Y_test)
        param = {'max_depth':4, 'eta':0.1, 'silent':1, 'objective':'binary:logistic', 'nthread':29, 'eval_metric': 'auc'}
        evallist = [(dval, 'val'), (dtrain, 'train')]
        num_round = int(sys.argv[1])
        bst = xgb.train(param.items(), dtrain, num_round, evallist)
        break
        ###################################################################
            
    dtrain = xgb.DMatrix(vec_train, label=Y_train)
    dtest = xgb.DMatrix(vec_test, label=Y_test)
    bst = xgb.train(param.items(), dtrain, num_round)
    #dump model
    bst.dump_model('xgb'+str(sys.argv[2])+'.dump', fmap='xgb'+str(sys.argv[2])+'.fmap', with_stats=True)
    bst.save_model('test'+str(sys.argv[2])+'.model')

    feature_score =  bst.get_score(fmap='xgb.fmap', importance_type='gain')
    #for key, value in feature_score.iteritems():
    #    print key.encode('u8'), value
    
    #print datetime.now()
    dtest = xgb.DMatrix(vec_test, label=Y_test)
    output_test['XGB'] = bst.predict(dtest)
    #print datetime.now()
    output_test['ID'] = test[ID].astype(str)
    output_test['Label'] = test[label]
    #output_test['Money'] = test[u'本金余额']
    output_test[['ID', 'XGB', 'Label']].to_csv('data/result.csv', index=False, encoding='u8')

if __name__ == "__main__":
    main()
