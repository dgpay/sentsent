import re
import string 
import nltk
import csv
import numpy as n
import pandas as pd
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
from nltk.tokenize import word_tokenize
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory

def preprocess_word(word):
    # Remove punctuation
    word = word.strip('\'"?!,.():;')
    # Convert more than 2 letter repetitions to 2 letter
    # funnnnny --> funny
    word = re.sub(r'(.)\1+', r'\1\1', word)
    # Remove - & '
    word = re.sub(r'(-|\')', '', word)
    return word


def is_valid_word(word):
    # Check if word begins with an alphabet
    return (re.search(r'^[a-zA-Z][a-z0-9A-Z\._]*$', word) is not None)

dataset = pd.read_csv(
        'data train.csv',
        delimiter=';', 
        )


arr=dataset.to_numpy()
kalimat=arr[:,[0]]

factory = StemmerFactory()
stemmer = factory.create_stemmer()
akhir=[]
i=5
regex = re.compile('[^a-zA-Z]')
for i in range(5,6):
    tweet=kalimat[i][0]
    tweet = tweet.lower()
    # Replaces URLs with the word URL
    tweet = re.sub(r'((www\.[\S]+)|(https?://[\S]+))', ' URL ', tweet)
    # Replace @handle with the word USER_MENTION
    tweet = re.sub(r'@[\S]+', 'USER_MENTION', tweet)
    # Replaces #hashtag with hashtag
    tweet = re.sub(r'#(\S+)', r' \1 ', tweet)
    # Remove RT (retweet)
    tweet = re.sub(r'\brt\b', '', tweet)
    # Replace 2+ dots with space
    tweet = re.sub(r'\.{2,}', ' ', tweet)
    # Strip space, " and ' from tweet
    tweet = tweet.strip(' "\'')
    # Replace multiple spaces with a single space
    tweet = re.sub(r'\s+', ' ', tweet)
    word = tweet.split()
    
    word = preprocess_word(word)
    if(is_valid_word(word)):
        word = stemmer.stem(word)
        word = word.translate(str.maketrans("","",string.punctuation))
        akhir.append(word)
    
print(akhir)
    
     
    #print('ini ke - ',i)
    


#dict = {'text': akhir}  
#df = pd.DataFrame(dict) 
#df.to_csv('file1.csv') 
