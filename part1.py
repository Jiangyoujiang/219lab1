import csv
import matplotlib.pyplot as plt
r=[]
workflow=[]
c=0
with open ('network_backup_dataset.csv','rb') as f:
    reader=csv.reader(f)
    for row in reader:
        if (c>0):
            int_row = row
            int_row[0]=int(row[0])
            int_row [5] = float(row [5])
            if (row[1]=="Monday"):
                int_row[1] = int(1)
            if (row[1]=="Tuesday"):
                int_row[1] = int(2)
            if (row[1]=="Wednesday"):
                int_row[1] = int(3)
            if (row[1]=="Thursday"):
                int_row[1] = int(4)
            if (row[1]=="Friday"):
                int_row[1] = int(5) 
            if (row[1]=="Saturday"):
                int_row[1] = int(6)   
            if (row[1]=="Sunday"):
                int_row[1] = int(7)       
            r.append(int_row)
        c=c+1
wf0=2*[2*[0]]
for row in r:
    if (row[3]=="work_flow_0"):
        day=(row[0]-1)*7+row[1]
        if(day<20):
            wf0[0][0]=1
            wf0[0][1]+= row[5]
        if((day>=20) & (day<40)):
            wf0[1][0] = 2
            wf0[1][1] += row[5]
        if((day>=40) & (day<60)):
            wf0[2][0] = 3
            wf0[2][1] += row[5]
        if((day>=60) & (day<80)):
            wf0[3][0] = 4
            wf0[3][1] += row[5]
        if((day>=80) & (day<100)):
            wf0[4][0] = 5
            wf0[4][1] += row[5]
    print day,"  ",wf0
        