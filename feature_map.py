from unidecode import unidecode

def feature_map(file_name,features):
    outfile = open(file_name, 'w')
    for i, feat in enumerate(features):
        #outfile.write('{0}\t{1}\tq\n'.format(i, feat.encode('unicode-escape')))
        tmp = ""
        for elm in unidecode(feat).split(' '):
            tmp += str(elm) + '_'
        
        outfile.write('{0}\t{1}\tq\n'.format(i, tmp[:-1]))
    outfile.close()

def feature_map_w_load_file(infile_name, outfile_name):
    infile = open(infile_name, 'r+')
    outfile = open(outfile_name, 'w')
    for elm in infile.read().split('\n')[:-1]:
        v = elm.split('\t')
        #print v[1].decode('u8').encode('unicode-escape')
        tmp = ""
        for elm in unidecode(v[1].decode('unicode-escape')).split(' ')[:-1]:
            tmp += str(elm) + '_'

        outfile.write('{0}\t{1}\tq\n'.format(v[0], tmp[:-1]))
    infile.close()
    outfile.close()

if __name__ == "__main__":
    feature_map_w_load_file('xgbrand.fmap', 'xgbrand_uni.fmap')
        

