import csv
def main():
    line_name=''
    bs_p=0
    bs=''
    ls_p=99999999999
    ls=''
    t=True
    print("*** Subway Report for Seoul on March 2023 ***")
    f = open('q4.csv','r',encoding='ANSI')
    data = csv.reader(f)
    next(data)
    for row in data:
        line_name = row[1]
        break
    for row in data:
        for i in range(4,6):
            if row[i] == '':
                for j in range(4,6):
                    row[j]=0
                t = False
            row[i]=int(row[i])
        if t:
            if(line_name==row[1]):
                if(bs_p<row[4]+row[5]):
                    bs_p = row[4]+row[5]
                    bs = row[3]
                if(ls_p>row[4]+row[5]):
                    ls_p = row[4]+row[5]
                    ls = row[3]
            else:
                if(line_name =="1호선"):
                    print("Line 1:")
                    print("Busiest Station: ", bs,"(",bs_p,")")
                    print("Least used Station: ",ls,"(",ls_p,")")
                if(line_name =="2호선"):
                    print("Line 2:")
                    print("Busiest Station: ", bs,"(",bs_p,")")
                    print("Least used Station: ",ls,"(",ls_p,")")
                if(line_name =="3호선"):
                    print("Line 3:")
                    print("Busiest Station: ", bs,"(",bs_p,")")
                    print("Least used Station: ",ls,"(",ls_p,")")
                if(line_name =="4호선"):
                    print("Line 4:")
                    print("Busiest Station: ", bs,"(",bs_p,")")
                    print("Least used Station: ",ls,"(",ls_p,")")
                line_name = row[1]
                bs=''
                bs_p=0
                ls=''
                ls_p=999999999
        t= True
if __name__ == '__main__':

    main()
