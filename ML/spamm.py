import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import string
from joblib import dump

dataset = pd.read_csv("spam.tsv", sep='\t', names=['Class', 'Message'])
dataset.loc[dataset['Class'] == "ham", "Class"] = 1
dataset.loc[dataset['Class'] == "spam", "Class"] = 0


def cleanMessage(message):
    nonPunc = [char for char in message if char not in string.punctuation]
    nonPunc = "".join(nonPunc)
    return nonPunc


dataset['Message'] = dataset['Message'].apply(cleanMessage)

CV = CountVectorizer(stop_words="english")
xSet = dataset['Message'].values
ySet = dataset['Class'].values

xSet = CV.fit_transform(xSet)

NB = MultinomialNB()
NB.fit(xSet, ySet)

dump(NB, "../templates/nb_model.joblib")
dump(CV, "../templates/vector.joblib")
