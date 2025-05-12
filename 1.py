import os
import csv
import tushare as ts
ts.set_token('377efbb33d789b4e122c37dc27e2aec8796893667c41f925f899f5f0')
pro = ts.pro_api()
df=pro.daily(ts_code='601288.SH', start_date='20250201', end_date='20250228')
df.to_csv("601288_Februrar",index=False)
file_path=r"C:\Users\刘懿君\Desktop\华东理工大学\python与金融数据\3.12\601288_Februrar"
max=0
answer=[]
with open(file_path,mode='r',encoding="utf-8") as file:
    header=file.readline()
    for line in file:
        row=line.strip().split(',')
        close=float(row[5])
        if close>max:
            max=close
            answer=row
print(f"收盘价最高值：{max}")
print(f"当日全部信息：{answer}")