import pandas as PD
import nltk
import wordninja
import string
import spacy
import re
import emoji
from nltk.corpus import stopwords




nlp = spacy.load('en_core_web_sm')
col_list = ["text"]
Tweets = open(r"C:\Users\foxsq\OneDrive\Documents\ctu school stuff\Big Data Analytics\Tweets.csv", 'rb') #opens csv file in panda
TT = PD.read_csv(Tweets, usecols = col_list) #TT is Tweet Text, limits read list to just the text list.
print("data_shape: ", TT.shape)
TT.head(2)


def Scrub_token(IT): #remove unneeded text and symbols then tokenize text columns. 
    mention_words_removed = re.sub(r'@\w+', ' ', IT) 
    hash_sign_removed = re.sub(r'#', '', mention_words_removed) 
    url_removed = ' '.join(word for word in hash_sign_removed.split(" ") if not word.startswith('http'))
    #removes #,@,\, + from text column.
    
    demoj = emoji.demojize(url_removed)
    
    splitted = wordninja.split(demoj)
    splitted = " ".join(word for word in splitted)
    
    lem = nlp(splitted) #strips punctuation from text column
    punctuations = string.punctuation
    punctuations = punctuations + '...'
    
    sentence = []
    for word in lem:
        word = word.lemma_.lower().strip()
        if ((word != '-pron-') & (word not in punctuations)):
            sentence.append(word)
    
    stop_words = set(stopwords.words('english'))
    stop_words_removed = [word for word in sentence if word not in stop_words]
    
    return stop_words_removed

TT["text_"] = TT["text"].apply(Scrub_token) #applies Scrub token to text coloum and adds text_ as a new column without additions.
TT[["text", "text_"]].head()



print(TT)

print(TT['text_'].value_counts())

TT.to_csv('Tweets.csv') 

