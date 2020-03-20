from collections import Counter
import csv
import re
import matplotlib.pyplot as plt


with open("train andai - Sheet1.csv", 'r') as file:
    tweet = list(csv.reader(file))



def text(tweet, score):
    return " ".join([r[0] for r in tweet if r[1] == str(score)])

def hitung_tweet(text):
    words = re.split("\s+", text)
    return Counter(words)

kataNeg = text(tweet, -1)
kataPos = text(tweet, 1)

jumneg = hitung_tweet(kataNeg)
jumpos = hitung_tweet(kataPos)

#print("contoh Negative ke-0: {0}".format(kataNeg[:100]))
#print("contoh Positive ke-0: {0}".format(kataPos[:100]))



def hitung_score(score):
    return len([r for r in tweet if r[1] == str(score)])

Postweet = hitung_score(1)
Negtweet = hitung_score(-1)

Ppos = Postweet / len(tweet)
Pneg = Negtweet / len(tweet)

def hitung_prediksi(text, jumlah_kata, class_peluang, class_score):
    prediksi = 1
    hitung_kata = Counter(re.split("\s+", text))
    for word in hitung_kata:
        prediksi *=  hitung_kata.get(word) * ((jumlah_kata.get(word, 0) + 1) / (sum(jumlah_kata.values()) + class_score))
    return prediksi * class_peluang


#print("Review: {1}".format(tweet[1][1])
#print("Negative prediction: {1}".format(hitung_prediksi(tweet[1][1], jumneg, Pneg, Negtweet)))
#print("Positive prediction: {1}".format(hitung_prediksi(tweet[1][1], jumpos, Ppos, Postweet)))


def hasil(text, hitung_prediksi):
    negative_prediction = hitung_prediksi(text, jumneg, Pneg, Negtweet)
    positive_prediction = hitung_prediksi(text, jumpos, Ppos, Postweet)

    if negative_prediction > positive_prediction:
      return -1
    return 1

with open("test andai - Sheet1.csv", 'r') as file:
    test = list(csv.reader(file))

end = [hasil(r[0], hitung_prediksi) for r in test]

with open("test andai - Sheet1.csv", 'r') as file:
    test = list(csv.reader(file))

end = [hasil(r[0], hitung_prediksi) for r in test]
print(end)
pakhir=0
nakhir=0
for i in range (0,len(end)):
    if(end[i]==1):
        pakhir=pakhir+1
    elif(end[i]==-1):
        nakhir=nakhir+1
    
pakhir=(pakhir*100)/len(end)
nakhir=(nakhir*100)/len(end)
print("positif percent",pakhir)
print("negative percent",nakhir)
print("positif perobability",Pneg)
print("negatif perobability",Ppos)



nama =["positif","negatif"]
nilai =[pakhir,nakhir]

x = range(len(nama))
plt.bar(x, nilai)
plt.xticks(x, nama)

plt.ylabel('Nilai')
plt.xlabel('Nama')
plt.title('Grafik Nilai')
plt.show()