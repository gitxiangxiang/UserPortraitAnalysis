from python.readdata import read
from python.dataprocess import wordcut
from gensim import corpora, models, similarities
# import jieba as jp


if __name__ == "__main__":
    # excel 路径
    bookName = r"..\..\数据\个人诉求.xlsx"
    # 表单名
    sheetName = "第五人"
    # 读取Excel
    data = read.read_data_from_excel(bookName, sheetName)
    # 提取投诉的主要内容
    documents = [x[12].value for x in data]
    # 分词
    words = wordcut.word_cut_by_jieba(documents[:100])
    for i in words:
        for j in i:
            print(j, end=' ')
        print()
    """构建词频矩阵，训练LDA模型"""
    dictionary = corpora.Dictionary(words)
    # corpus[0]: [(0, 1), (1, 1), (2, 1), (3, 1), (4, 1),...]
    # corpus是把每条新闻ID化后的结果，每个元素是新闻中的每个词语，在字典中的ID和频率
    corpus = [dictionary.doc2bow(text) for text in words]

    lda = models.LdaModel(corpus=corpus, id2word=dictionary, num_topics=10)
    topic_list = lda.print_topics(num_topics=10,num_words=20)
    print("10个主题的单词分布为：\n")
    for topic in topic_list:
        print(topic)

    text5 = '请政府尽快落实关于疫情的防治工作'
    testData = wordcut.word_cut_by_jieba([text5, ])
    other_corpus = [dictionary.doc2bow(text) for text in testData]
    ndarray = lda[other_corpus[0]]
    print(ndarray)
