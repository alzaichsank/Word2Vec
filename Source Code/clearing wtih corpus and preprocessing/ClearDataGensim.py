#@title Clear text data (gensim)
import io
import time
from datetime import timedelta

import gensim

start_time = time.time()
print('Streaming corpus data...')
id_wiki = gensim.corpora.TextCorpus('black_campaign.txt')


with io.open('result_gensim.txt', 'w',encoding="utf-8") as wiki_txt:
    for text in id_wiki.get_texts():
        wiki_txt.write(" ".join(map(str, text)) + '  . ' +  '\n')

finish_time = time.time()
print('Elapsed time: {}'.format(timedelta(seconds=finish_time-start_time)))