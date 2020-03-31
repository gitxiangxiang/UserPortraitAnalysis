from gensim.test.utils import common_texts
from gensim.corpora.dictionary import Dictionary
from gensim import models

for common_text in common_texts:
    print(common_text)
# Create a corpus from a list of texts
common_dictionary = Dictionary(common_texts)
common_corpus = [common_dictionary.doc2bow(text) for text in common_texts]
# Train the model on the corpus.
lda = models.LdaModel(common_corpus, num_topics=10)
topic_list = lda.print_topics(10)
print("10个主题的单词分布为：\n")
for topic in topic_list:
    print(topic)

"""
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False  # 这里设置字体，防止中文乱码
"""