# -*- coding:utf-8 -*-

import jieba, jieba.analyse, os, re
from gensim import corpora, models, similarities
import python.readdata.read


"""创建停用词列表"""


def stopwordslist():
    stopwords = [line.strip() for line in open('./stopwords.txt', encoding='UTF-8').readlines()]
    return stopwords


"""对句子进行中文分词"""


def seg_depart(sentence):
    sentence_depart = jieba.cut(sentence.strip())
    stopwords = stopwordslist()
    outstr = ''
    for word in sentence_depart:
        if word not in stopwords:
            outstr += word
            outstr += " "
    # outstr：'黄蜂 湖人 首发 科比 带伤 战 保罗 加索尔 ...'
    return outstr


"""分词"""
# if not os.path.exists('./cnews.train_jieba.txt'):
#     # 给出文档路径
#     filename = "./cnews.train.txt"
#     outfilename = "./cnews.train_jieba.txt"
#     inputs = open(filename, 'r', encoding='UTF-8')
#     outputs = open(outfilename, 'w', encoding='UTF-8')
#
#     # 把非汉字的字符全部去掉
#     for line in inputs:
#         line = line.split('\t')[1]
#         line = re.sub(r'[^\u4e00-\u9fa5]+', '', line)
#         line_seg = seg_depart(line.strip())
#         outputs.write(line_seg.strip() + '\n')
#
#     outputs.close()
#     inputs.close()
#     print("删除停用词和分词成功！！！")


def word_cut_by_jieba(sentences):
    """
    对一组句子进行分词
    :param sentences:
    :return:
    """
    words = []
    for sentence in sentences:
        words.append(jieba.analyse.extract_tags(sentence))
    return words
