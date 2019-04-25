'''
Natural language-based similiarity check

'''

import nltk
import string

from sklearn.feature_extraction.text import TfidfVectorizer

stemmer = nltk.stem.porter.PorterStemmer()
rm_punct = dict((ord(char), None) for char in string.punctuation)

def stem_tokens(tokens):
    return [stemmer.stem(item) for item in tokens]

'''remove punctuation, lowercase, stem'''
def normalize(text):
    return  stem_tokens(
                nltk.word_tokenize(
                    text.lower().translate(rm_punct)
                )
            )

vectorizer = TfidfVectorizer(
                tokenizer=normalize,
                stop_words='english'
            )

def cosine_sim_comp(text1, text2):
    tfidf = vectorizer.fit_transform([text1, text2])
    return ((tfidf * tfidf.T).A)[0,1]

# Assume we only get the answer column
def cosine_sim(df):
    tf_idf = vectorizer.fit_transform(df)
    return (tf_idf * tf_idf.T).A