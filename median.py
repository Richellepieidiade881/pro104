import csv
with open ("data.csv",newline="")as f:
    reader=csv.reader(f)
    data=list(reader)

data.pop(0)
newdata=[]
for i in range(len(data)):
    num=data[i][2] 
    newdata.append(float(num))


n=len(newdata)
newdata.sort()
if n%2==0:
    median1=float(newdata[n//2])
    meadian2=float(newdata[n//2-1])
    meadian=median1+meadian2

else:
    meadian=float(newdata[n//2])

print(meadian)