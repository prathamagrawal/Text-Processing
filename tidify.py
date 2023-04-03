import argparse
import time
import os
from pathlib import Path
import numpy as np
import pandas as pd
import re
import nltk
import spacy
import string
pd.options.mode.chained_assignment = None
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer
import json
from collections import Counter

from utils.processing import *

PUNCT_TO_REMOVE = string.punctuation
", ".join(stopwords.words('english'))
stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()
with open('./utils/abbre.json') as json_file:
    abbreviations = json.load(json_file)

def process(source,attributes,freqWords,rareWords,skemmetization,lemmetization):
    data=pd.read_csv(source)
    for item in attributes:
        data[item]=data[item].astype(str)
        data[item]=data[item].str.lower()
        data[item]=data[item].apply(remove_punctuation)
        data[item]=data[item].apply(remove_stopwords)

    if(freqWords or rareWords):
        cnt = Counter()
        for text in data[item].values:
            for word in text.split():
                cnt[word] += 1

        if(freqWords):
            FREQWORDS = set([w for (w, wc) in cnt.most_common(10)])
            data[item]=data[item].apply(remove_freqwords)
        
        if(rareWords):
            n_rare_words = 10
            RAREWORDS = set([w for (w, wc) in cnt.most_common()[:-n_rare_words-1:-1]])
            data[item]=data[item].apply(remove_rarewords)
   
    if(skemmetization):
        # print("Skemmetization: ")
        data[item]=data[item].apply(stem_words)
    if(lemmetization):  
        data[item]=data[item].apply(lemmatize_words)
    data[item]=data[item].apply(clean_text)


    return data


def tidify():
    source=opt.source
    attributes=opt.attribute
    freqWords=opt.remove_frequent
    rareWords=opt.remove_rare
    skemmetization=opt.skemmetization
    lemmetization=opt.lemmetization
    data=process(source,attributes,freqWords,rareWords,skemmetization,lemmetization)
    # print(data[attributes[0]][0])
    print("Tidify Called with attributes: ")
    print()
    print(opt)
    print()
    os.makedirs('output', exist_ok=True)  
    data.to_csv('output/outData.csv') 


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--source',help='Define source file location',required=True)
    parser.add_argument('--attribute',help='Define attributes you want to process. 3 attributes can be defined.',nargs='+')
    parser.add_argument('--remove_frequent',help="Define true to remove frequent words. Default: False",default=False)
    parser.add_argument('--skemmetization',help="Define true to apply Skemmetion. Default: False",default=False)
    parser.add_argument('--lemmetization',help="Define true to apply lemmetization. Default: False",default=False)
    parser.add_argument('--remove_rare',help="Define true to remove rare words. Default: False",default=False)
    

    opt = parser.parse_args()
    # print(opt)

    tidify()