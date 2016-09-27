import nltk, json
import numpy as np

stemmer = nltk.PorterStemmer()

def business(bus_id,star_count):
    if bus_id not in business_count:
        business_count[bus_id]=1
        star[bus_id]=star_count
    else:
        business_count[bus_id]+=1
        star[bus_id]+=star_count
    return 0
        
def sentiment(bus_id,review_text):
    temp_sentiment_score=0
    review_text=review_text.split(' ')
    for i in range(len(review_text)):
        word_stem=stemmer.stem(review_text[i].strip())
        if word_stem in word:
            temp_sentiment_score+=word_sentiment[word_stem]
        else:
            temp_sentiment_score+=0
    if bus_id not in sentiment_score:
        sentiment_score[bus_id]=temp_sentiment_score
    else:
        sentiment_score[bus_id]+=temp_sentiment_score
    return 0

def output():
    outfile=open('star_sentimentscore.txt','w')
    for bus_id in business_count.keys():
        outfile.write(str((star[bus_id]/float(business_count[bus_id])))+'\t'+str((sentiment_score[bus_id]/float(business_count[bus_id])))+'\n')
    outfile.close()           
    return 0

if __name__ == '__main__':
    sentiment_file=open('sentiment_word_list_stemmed.json','rU')
    word_sentiment=json.loads(sentiment_file.read())
    word=word_sentiment.keys()

    business_count={}
    sentiment_score={}
    star={}

    yelp_data=open('yelp_academic_dataset.json','rU')
    next(yelp_data,130874)
    for line in yelp_data:
        review=json.loads(line)
        if review['type']=='review':
            business(review['business_id'],review['stars'])
            sentiment(review['business_id'],review['text'])
    output()


            


