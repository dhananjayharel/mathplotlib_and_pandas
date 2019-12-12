from collections import Counter
import pandas
import re

#create matrix to contain all data
def make_matrix(headlines, vocab):
    matrix = []
    for headline in headlines:
        headline = headline.split(" ")
        #count each word in the headline and make a dictionary
        counter = Counter(headline)
        #turn the dictionary into a matrix row using the vocab
        row = [counter.get(w,0) for w in vocab]
        matrix.append(row)
    df = pandas.DataFrame(matrix)
    df.columns = unique_words
    #display settings for matrix
    pandas.set_option('display.max_columns', None)
    pandas.set_option('display.max_rows', None)
    return df

headlines = [
    "PretzelBros, airbnb for people who like pretzels, raises $2 million",
    "Top 10 reasons why Go is better than whatever language you use.",
    "Why working at apple stole my soul (I still love it though)",
    "80 things I think you should do immediately if you use python.",
    "Show HN: carjack.me -- Uber meets GTA"
]

with open("stop_words.txt", 'r') as f:
    stopwords = f.read().split("\n")

#we are removing punctuations if any
stopwords = [re.sub(r'[^\w\s\d]','',s.lower()) for s in stopwords]

#lowercase then replace any non-letter space or digit character in headlines
new_headlines = [re.sub(r'[^\w\s\d]','',h.lower()) for h in headlines]

unique_words = list(set(" ".join(new_headlines).split(" ")))

#find unique words after removing stop words
unique_words = [w for w in unique_words if w not in stopwords]

print(make_matrix(headlines, unique_words))
