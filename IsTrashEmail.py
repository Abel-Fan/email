"""
1、获取邮件内容
2、邮件分词
3、通过贝叶斯算法计算 邮件是垃圾邮件的概率
"""
# 获取ratio数据
import pickle,jieba,re

with open("ratio.txt",'rb+') as f:
    ratio = pickle.load(f)

with open("data/normal/33","r",encoding="gbk",errors="ignore") as f:
    email = f.read()


def GetRatio(con):
    index = con.index("\n\n")
    con = con[index:]
    con = con.replace("\n", "").strip()
    r = re.compile('[^\u4E00-\u9FA5]+')
    con = r.sub("", con)
    con = jieba.cut(con, cut_all=False)

    words = [word for word in con if len(word) >= 2]
    p = 1
    rest_p = 1
    for word in words:
        p *= ratio[word][1]  # word词 是垃圾邮件的概率
        rest_p *= 1-ratio[word][1]

    P = p/(p+rest_p)

    p1 = 1
    rest_p1 = 1
    for word in words:
        p1 *= ratio[word][0]  # word词 是正常邮件的概率
        rest_p1 *= 1-ratio[word][0]

    P1 = p1/(p1+rest_p1)
    print(P)
    if P>P1:
        print("垃圾邮件")
    else:
        print("正常邮件")

GetRatio(email)