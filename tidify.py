import argparse
import time
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

from utils.processing import *

PUNCT_TO_REMOVE = string.punctuation
", ".join(stopwords.words('english'))

def process(source,attributes):
    data=pd.read_csv(source)
    for item in attributes:
        data[item]=data[item].astype(str)
        data[item]=data[item].str.lower()
        data[item]=data[item].apply(remove_punctuation)
        data[item]=data[item].apply(remove_stopwords)

        


    return data


def tidify():
    source=opt.source
    attributes=opt.attribute
    data=process(source,attributes)
    print(data[attributes[0]][0])
    print(opt)



if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--source',help='Define source file location',required=True)
    parser.add_argument('--attribute',help='Define attributes you want to process. 3 attributes can be defined.',nargs='+')

    opt = parser.parse_args()
    # print(opt)

    tidify()