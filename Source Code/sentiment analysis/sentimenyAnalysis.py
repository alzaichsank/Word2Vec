from nltk.sentiment.vader import SentimentIntensityAnalyzer
sid = SentimentIntensityAnalyzer()
import string
import pandas as pd

start_time = time.time()
print('sentiment analysis data...')

summary = {"positive":0,"negative":0}
messages = [line.rstrip() for line in open("test_data_2.txt",encoding="utf8")]
with io.open('positive.txt', 'w',encoding='utf-8') as f:
    for x in messages:
        
        ss = sid.polarity_scores(x)
        if ss["compound"] > 0.0:
            summary["positive"] +=1
            f.write(x  + '\n')
f.close()

with io.open('negative.txt', 'w',encoding='utf-8') as f:
    for x in messages:
        
        ss = sid.polarity_scores(x)
        if ss["compound"] <= 0.0:
            summary["negative"] +=1
            f.write(x  + '\n')
f.close()

finish_time = time.time()
print('Elapsed time: {}'.format(timedelta(seconds=finish_time-start_time)))