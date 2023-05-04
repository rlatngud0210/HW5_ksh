import csv
def main():
    f = open('q2.csv','r',encoding='ANSI')
    data = csv.reader(f)
    next(data)
    max_tv=-999
    max_tv_date=''
    min_tv=999
    min_tv_date=''
    t = True
    for row in data:
        for i in range(2,5):
            if row[i] == '':
                for j in range(2,5):
                    row[j]=0
                t = False
            row[i]=float(row[i])
        if(t):
            if(max_tv<row[4]-row[3]):
                max_tv = row[4]-row[3]
                max_tv_date = row[0]
            if(min_tv>row[4]-row[3]):
                min_tv = row[4]-row[3]
                min_tv_date = row[0]
        t = True

    print("*** Annual Temperature Report for Seoul in 2022 ***")
    print("Day with the Largest Temperature Variation: ",max_tv_date)
    print("Maximum Temperature Difference: ",max_tv)
    print("Day with the Smallest Temperature Variation: ",min_tv_date)
    print("Minimum Temperature Difference: ",round(min_tv,1))

if __name__ == '__main__':

    main()