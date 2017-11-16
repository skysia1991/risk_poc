import csv

gg=0
gb=0
bg=0
bb=0
th=0
mx = 0
mxth = 0

for lth in range(1000):
    th=(lth)/float(1000.0)
    gg = 0
    gb = 0
    bg = 0
    bb = 0
    rownum = 0
    with open('data/result.csv', 'rb') as f:
        reader = csv.reader(f)
        for row in reader:
            # print row
            rownum += 1
            if rownum>1:
                row[1]=float(row[1])
                fact = int(row[2])
                #print row[1],th,lth
                if row[1]>th:
                    predict=1
                else:
                    predict=0
                if  fact==1 and predict==1:
                    gg += 1
                elif predict == 0 and fact==0:
                    bb +=1
                elif predict == 1 and fact == 0:
                    gb +=1
                elif predict == 0 and fact == 1:
                    bg +=1
            #print th
            # print predict,fact
            # print gg,gb,bg,bb
        try:
            tpr=(gg)/float(gg+bg)
            fpr=(gb)/float(gb+bb)
            if abs(tpr-fpr)>mx:
                mx=abs(tpr-fpr)
                mxth=th
        except:
            continue
print mxth