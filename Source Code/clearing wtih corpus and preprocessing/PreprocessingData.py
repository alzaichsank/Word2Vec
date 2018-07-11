import io
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus.reader import PlaintextCorpusReader

import time
from datetime import timedelta

start_time = time.time()
print('clearing corpus data...')

ps = PorterStemmer()
stop_words = set(stopwords.words('indonesian'))
file1 = open("result_gensim.txt")
line = file1.read()
words = line.split()
#words = sent_tokenize(line)
#words = PlaintextCorpusReader('.',line)
#appendFile = open('test_data.txt','w+')
data=['txt','url','http','blogspot','com','file','filename','html','https','black_campaign','parent_folder']
endData=['.']
for r in words:
    if not r in stop_words and not r in data :
        #print(r)        
        appendFile = open('result_final_prepocessing.txt','a+')        
        appendFile.write(" "+ r)
        if r in endData :
            appendFile = open('result_final_prepocessing.txt','a+')        
            appendFile.write(" " + '\r\n')
             #print(' ') 

f.close() 
    
finish_time = time.time()
print('Elapsed time: {}'.format(timedelta(seconds=finish_time-start_time)))
