from .word_segment import segment_by_jieba
from gensim import corpora, models
from gensim.test.utils import datapath


def LDA_model(words):
    """
    训练LDA主题模型
    :param words:
    :return:
    """
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
    model_file = datapath('lda_model')
    lda.save(model_file)
    lda = models.LdaModel.load(model_file)
    topic_list = lda.print_topics(num_topics=10, num_words=20)
    print("10个主题的单词分布为：\n")
    for topic in topic_list:
        print(topic)

    text5 = '请政府尽快落实关于疫情的防治工作'
    testData = segment_by_jieba([text5, ])
    other_corpus = [dictionary.doc2bow(text) for text in testData]
    result = lda[other_corpus[0]]
    lda.update(other_corpus)
    print(result)
