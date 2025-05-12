import random
import csv
import string
import os

info=[]
with open("client.csv","r",encoding="GBK") as f:
    reader=csv.reader(f)
    next(reader)
    for row in reader:
        text=""
        text+=" ".join(row)+" "
        info.append(text)

    num=random.randint(0,len(info)-1)
    print(f"一等奖是:{info[num]}")
    info.remove(info[num])
print("------------------------")
for i in range(2):
    num = random.randint(0, len(info) - 1)
    print(f"二等奖是:{info[num]}")
    info.remove(info[num])

print("-------------------------")
for i in range(10):
    num = random.randint(0, len(info) - 1)
    print(f"三等奖是:{info[num]}")
    info.remove(info[num])

print("-------------------------")