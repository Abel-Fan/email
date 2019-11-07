import os,jieba,re
from collections import Counter,defaultdict
import pickle
class GetPro:
    def __init__(self):
        # 正常邮件中的词
        # [ ]
        self.normalWord = []
        # 垃圾邮件中的词
        self.trashWord = []
        self.words = []
        # {'公司','保险','基金'}

        #计算得出结果： { '公司':[0.01,0.02],}
    def getWord(self):
        """
        获取邮件中的 词
        :return:
        """
        confiles = os.listdir("./data") # 词 的分类 normal trash
        for dirname in confiles:
            path = "./data/"+dirname
            for filename in os.listdir(path):
                self.splitWord( path+"/"+filename, dirname)

    def splitWord(self,filename,type):
        """
        :param filename: 邮件路径
        :param type: 邮件类型
        :return: None
        """
        with open(filename,"r",encoding="gbk",errors='ignore') as f:
            # 邮件内容
            con = f.read()
            # 筛选无用数据
            # 1 过滤邮件信息
            index = con.index("\n\n")
            con = con[index:]
            con = con.replace("\n","").strip()
            r = re.compile('[^\u4E00-\u9FA5]+')
            con = r.sub("",con)
            con = jieba.cut(con,cut_all=False)
            words = [ word for word in con if len(word)>=2]
            if type=="normal":
                self.normalWord += list(set(words))
            else:
                self.trashWord += list(set(words))
            self.words+=words

    def getRatio(self):
        data = defaultdict(list)
        normalWord = Counter(self.normalWord)
        trashWord = Counter(self.trashWord)
        for word in set(self.words):
            num = normalWord[word]
            num2 = trashWord[word]
            arr = [num,num2]
            for i in arr:
                if i !=0:
                    data[word].append(i/8000)
                else:
                    data[word].append(0.00001)
        print(data)
        with open("ratio.txt","wb+") as f:
            pickle.dump(data,f)

obj = GetPro()
obj.getWord()
obj.getRatio()

