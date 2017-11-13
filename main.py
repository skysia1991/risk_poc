#coding:utf-8
from sklearn.model_selection import KFold
from sklearn.metrics import roc_auc_score
import xgboost as xgb
import pandas as pd
from sklearn.feature_extraction import DictVectorizer
from transformer import *

def main():
    #Load data
    train = pd.read_csv('data/train.csv', encoding='u8')
    test = pd.read_csv('data/test.csv', encoding='u8')

    #Drop features
    drop_list = [u'资产编号',u'姓名']
    drop_list += [u'截至倒数第二期剩余期数（月）',u'截至倒数第二期历史最长逾期天数',u'截至倒数第二期已还本金（元）',u'截至倒数第二期逾期本金（元）',u'截至倒数第二期已还利息（元）',u'截至倒数第二期历史逾期次数',u'倒数第二期逾期天数',u'截至倒数第二期历史平均还款间隔（天）',u'截至倒数第二期剩余本金（元）',u'截至倒数第二期剩余利息（元）']
    drop_list += [u'截至倒数第三期剩余期数（月）',u'截至倒数第三期历史最长逾期天数',u'截至倒数第三期已还本金（元）',u'截至倒数第三期逾期本金（元）',u'截至倒数第三期已还利息（元）',u'截至倒数第三期历史逾期次数',u'倒数第三期逾期天数',u'截至倒数第三期历史平均还款间隔（天）',u'截至倒数第三期剩余本金（元）',u'截至倒数第三期剩余利息（元）']
    drop_list += [u'截至倒数第四期剩余期数（月）',u'截至倒数第四期历史最长逾期天数',u'截至倒数第四期已还本金（元）',u'截至倒数第四期逾期本金（元）',u'截至倒数第四期已还利息（元）',u'截至倒数第四期历史逾期次数',u'倒数第四期逾期天数',u'截至倒数第四期历史平均还款间隔（天）',u'截至倒数第四期剩余本金（元）',u'截至倒数第四期剩余利息（元）']
    df_train = train.drop(drop_list, axis=1)
    df_test = test.drop(drop_list, axis=1)

    #Assign feature and label
    X_train, X_test = df_train.iloc[:, 2:], df_test.iloc[:, 2:]
    Y_train, Y_test = df_train[u'标注'], df_train[u'标注']
    
    #Fillna
    X_train = naTransformer(X_train)
    X_test = naTransformer(X_test)

    #Deal with Date feature
    date_cols = [u'起始日',u'到期日']
    X_train = dateTransformer(X_train, date_cols)
    X_test = dateTransformer(X_test, date_cols)

    #Deal with Category Feature
    dict_train = df_train.to_dict(orient='records')
    dict_test = df_test.to_dict(orient='records')
    vectorizer = DictVectorizer()
    vec_train = vectorizer.fit_transform( dict_train )
    vec_test = vectorizer.transform( dict_test ) 
    
    #Cross validation
    kf = KFold(n_splits=5, shuffle=True) 
    output_test = pd.DataFrame()
    for train_index, val_index in kf.split(Y_train):
        print("TRAIN:", train_index, "VAL:", val_index)
        feature_train, feature_val = vec_train[train_index, :], vec_train[val_index, :]
        label_train, label_val = Y_train[train_index], Y_train[val_index]
            
        ###XGBOOST Model
        dtrain = xgb.DMatrix(feature_train, label=label_train)
        dval = xgb.DMatrix(feature_val, label=label_val)
        #dtest = xgb.DMatrix(vec_test, label=Y_test)
        param = {'max_depth':4, 'eta':0.1, 'silent':1, 'objective':'binary:logistic', 'nthread':29, 'eval_metric': 'auc'}
        evallist = [(dval, 'val'), (dtrain, 'train')]
        num_round = 200
        bst = xgb.train(param.items(), dtrain, num_round, evallist)
        break
        ###################################################################
            
    dtrain = xgb.DMatrix(vec_train, label=Y_train)
    dtest = xgb.DMatrix(vec_test, label=Y_test)
    bst = xgb.train(param.items(), dtrain, num_round)
    output_test['XGB'] = bst.predict(dtest)
    
    output_test['ID'] = test[u'资产编号'].astype(str)
    output_test['Label'] = test[u'标注']
    output_test[['ID', 'XGB', 'Label']].to_csv('data/result.csv', index=False, encoding='u8')

if __name__ == "__main__":
    main()
