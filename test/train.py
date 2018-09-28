# -*- coding: utf-8 -*-
import gensim

from gensim.models import word2vec
sentences = word2vec.Text8Corpus('D:/gitHubRes/python/词向量/text-classification-cnn-rnn/data/baike_triples.txt')
model = word2vec.Word2Vec(sentences,min_count=5,size=100)

model.save('D:/baike.model')
print("训练完成")