import jieba
import jieba.analyse
import os

jieba.analyse.set_stop_words(os.path.abspath("./user_profiles/data_process/custom_stop_words.txt"))


def segment_by_jieba(sentences):
    """
    对一组句子进行分词
    :param sentences:
    :return:
    """

    words = []
    for sentence in sentences:
        words.append(jieba.analyse.extract_tags(sentence))
    return words


def segment_with_weight(sentences):
    """
    对一组句子进行分词,带权重，默认取前30个词
    :param sentences:
    :return:
    """

    words = []
    for sentence in sentences:
        words.append(jieba.analyse.extract_tags(sentence, withWeight=True, topK=100))
    return words
