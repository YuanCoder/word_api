# -*- coding: utf-8 -*-
import gensim

from gensim.models import word2vec

model = word2vec.Word2Vec.load('D:/baike.model')

for i in model.most_similar("会计"):
    print(i[0],i[1])
#
# more_sentences = word2vec.Text8Corpus('D:/gitHubRes/python/词向量/text-classification-cnn-rnn/data/baike_triples.txt')
# model.build_vocab(more_sentences, update=True)
# model.train(more_sentences, total_examples=model.corpus_count, epochs=model.iter)
#
# for i in model.most_similar("会计"):
#     print(i[0],i[1])
#
# model.save('D:/new.model')