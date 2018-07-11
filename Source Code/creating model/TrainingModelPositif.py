#@title Training data positif
from gensim.models import word2vec

import time
from datetime import timedelta

import multiprocessing



start_time = time.time()
sentences = word2vec.LineSentence('positif_new.txt')
id_w2v = word2vec.Word2Vec(sentences, size=200, workers=multiprocessing.cpu_count()-1)
id_w2v.save('models_positif.model')
finish_time = time.time()

print('Finished. Elapsed time: {}'.format(timedelta(seconds=finish_time-start_time)))