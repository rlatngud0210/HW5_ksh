import csv
def main():
    f = open('q3.csv','r',encoding='ANSI')
    data = csv.reader(f)
    next(data)
    l1=0
    l2=0
    l3=0
    l4=0
    l5=0
    l6=0
    l7=0
    l8=0
    l9=0

    t= True
    for row in data:
        for i in range(4,6):
            if row[i] == '':
                for j in range(4,6):
                    row[j]=0
                t = False
            row[i]=int(row[i])
        if t:
            if(row[1]=="1호선"):
                l1 += row[4]+row[5]
            if(row[1]=="2호선"):
                l2 += row[4]+row[5]
            if(row[1]=="3호선"):
                l3 += row[4]+row[5]
            if(row[1]=="4호선"):
                l4 += row[4]+row[5]
            if(row[1]=="5호선"):
                l5 += row[4]+row[5]
            if(row[1]=="6호선"):
                l6 += row[4]+row[5]
            if(row[1]=="7호선"):
                l7 += row[4]+row[5]
            if(row[1]=="8호선"):
                l8 += row[4]+row[5]
            if(row[1]=="9호선"):
                l9 += row[4]+row[5]
            else:
                continue
        t = True
    dic = {l1:"1",l2:"2",l3:"3",l4:"4",l5:"5",l6:'6',l7:'7',l8:'8',l9:'9'}
    list=[l1,l2,l3,l4,l5,l6,l7,l8,l9]
    list.sort()
    print("*** Subway Report for Seoul on March 2023 ***")
    print("1st Busieset Line: Line ",dic[list[-1]]," (",list[-1],")")
    print("2nd Busieset Line: Line ",dic[list[-2]]," (",list[-2],")")
    print("1st Least used Line: Line ",dic[list[0]]," (",list[0],")")
    print("2nd Least used Line: Line ",dic[list[1]]," (",list[1],")")

if __name__ == '__main__':

    main()