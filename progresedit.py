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
        'file2.csv',
        delimiter=';', 
        )


arr=dataset.to_numpy()
kalimat=arr[:,[0]]
skor=arr[:,[1]]

factory = StemmerFactory()
stemmer = factory.create_stemmer()
akhir=[]
akhirnomor=[]
i=0
#regex = re.compile('[^a-zA-Z]')
for i in range(0,len(kalimat)):
    #print(kalimat[i][0])
    kal=kalimat[i][0]
    l=skor[i][0]
    #print(kal)
    #print(l)
    #print(kal)
    #print("EKSEKUSI BOSSQUE")
    hasil = kal.lower()

    hasil = re.sub(r'#(\S+)', '', hasil)
    hasil = re.sub(r'((www\.[\S]+)|(https?://[\S]+)|(pic\.[\S]+))', '', hasil)
    hasil = re.sub(r'(https[\S]+)|(pic\.[\S]+)', '', hasil)
    hasil = re.sub(r'(https:/[\S]+)|(pic\.[\S]+)', '', hasil)
    hasil = re.sub(r'\brt\b', '',hasil)
    hasil = re.sub(r'@[\S]+', '',hasil)
    hasil = re.sub(r'#(\S+)', r' \1 ',hasil)
    hasil = re.sub(r'@[\S]+', '', hasil)
    hasil = re.sub(r'\.{2,}', '', hasil)
    hasil = re.sub("[\b\.\b]{3}", " ", hasil)
    hasil = re.sub(r'\s+', ' ', hasil)
    hasil = re.sub(r'\n+', ' ', hasil)
    hasil = re.sub(r"[\s\.\n]", " " , hasil)
    hasil = re.sub(r"\d+", "", hasil)
    hasil = hasil.strip()
    hasil = stemmer.stem(hasil)
    hasil = hasil.translate(str.maketrans("","",string.punctuation))
    print(i)
    
     
    #print('ini ke - ',i)
    akhir.append(hasil)
    akhirnomor.append(l)


dict = {'text': akhir,'score':l}  
df = pd.DataFrame(dict) 
df.to_csv('file2-next.csv') 
