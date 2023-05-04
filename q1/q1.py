import csv
def main():
    f = open('q1.csv','r',encoding='ANSI')
    data = csv.reader(f)
    next(data)
    total_temp=0
    total_min=0
    total_max=0
    count = 0;
    t = True
    for row in data:
        for i in range(2,5):
            if row[i] == '':
                for j in range(2,5):
                    row[j]=0
                t= False
            row[i]=float(row[i])
        if(t):
            count+= 1
            total_temp += row[2]
            total_min += row[3]
            total_max += row[4]
        t = True
    print("*** Annual Temperature Report for Seoul in 2022 ***")
    print("Average Temperature: ",round(total_temp/count,2)," Celsius")
    print("Average Minimum Temperature: ",round(total_min/count,2)," Celsius")
    print("Average Maximum Temperature: ",round(total_max/count,2)," Celsius")

if __name__ == '__main__':

    main()