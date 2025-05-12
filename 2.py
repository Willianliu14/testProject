import collections
import csv
import jieba
import wordcloud
import matplotlib.pyplot as plt
filename="family_info.csv"
data=[
    ["关系","职业","兴趣爱好"],
    ["母亲","老师","阅读 旅行"],
    ["父亲","经理","旅行 运动"],
    ["本人","学生","旅行 阅读 游戏 运动"],
]
with open(filename,"w",newline="",encoding="utf-8") as f:
    writer=csv.writer(f)
    writer.writerows(data)
    f.close()

text=""
with open(filename,"r",encoding="utf-8") as f:
    reader=csv.reader(f)
    next(reader)
    for row in reader:
        text+=" ".join(row[1:])+" "
    f.close()

words=jieba.lcut(text)
word_counts=collections.Counter(words)
wc=wordcloud.WordCloud(
        font_path="msyh.ttc",
        width=800,
        height=400,
        background_color="white"
    ).generate_from_frequencies(word_counts)

plt.figure(figsize=(10,5))
plt.imshow(wc,interpolation='bilinear')
plt.axis("off")
plt.show()

