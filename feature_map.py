def feature_map(file_name,features):
    outfile = open(file_name, 'w')
    for i, feat in enumerate(features):
        outfile.write('{0}\t{1}\tq\n'.format(i, feat.encode('unicode-escape')))
        #outfile.write('{0}\t{1}\tq\n'.format(i, feat.encode('u8')))
    outfile.close()
