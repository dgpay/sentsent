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


dataset = pd.read_csv(
        'data train.csv',
        delimiter=';', 
        )


arr=dataset.to_numpy()
kalimat=arr[:,[0]]

factory = StemmerFactory()
stemmer = factory.create_stemmer()
akhir=[]
i=0
regex = re.compile('[^a-zA-Z]')
for i in range(0,len(kalimat)):
    #print(kalimat[i][0])
    kal=kalimat[i][0]
    #print(kal)
    #print("EKSEKUSI BOSSQUE")
    hasil = kal.lower()

    hasil = re.sub(r'#(\S+)', '', hasil)
    hasil = re.sub(r'((www\.[\S]+)|(https?://[\S]+)|(pic\.[\S]+))', '', hasil)
    hasil = re.sub(r'@[\S]+', '', hasil)
    hasil = re.sub(r'\.{2,}', '', hasil)
    hasil = re.sub("[\b\.\b]{3}", " ", hasil)
    hasil = re.sub(r'\s+', ' ', hasil)
    hasil = re.sub(r"\d+", "", hasil)
    hasil = hasil.strip()
    hasil = stemmer.stem(hasil)
    hasil = hasil.translate(str.maketrans("","",string.punctuation))
    print(i)
    
     
    #print('ini ke - ',i)
    akhir.append(hasil)


dict = {'text': akhir}  
df = pd.DataFrame(dict) 
df.to_csv('xxx.csv') 
