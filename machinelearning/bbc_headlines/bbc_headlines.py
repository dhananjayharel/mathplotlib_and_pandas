from nltk.tokenize import sent_tokenize,word_tokenize
from nltk.corpus import stopwords
from collections import defaultdict
from string import punctuation
from heapq import nlargest
import urllib2
from bs4 import BeautifulSoup

#pip install nltk
#pip install bs4

class FrequencySummarizer:
    def __init__(self,min_cut=0.1, max_cut=0.9):
        #cut words from these ranges
        self._min_cut = min_cut
        self._max_cut = max_cut
        self._stopwords = set(stopwords.words('english') + list(punctuation))

    #we are calcuating the frequency for each element in our headline
    def _compute_frequencies(self, word_sent):
        #compute the frequency of each word.
        #input: word_sent, a list of sentences already tokenized
        #output: freq, a dictionary where freq[w] is the frequency of w
        freq = defaultdict(int)
        for s in word_sent:
            for word in s:
                if word not in self._stopwords:
                    freq[word] += 1
        #frequences normalized and filtering
        m = float(max(freq.values()))
        for w in freq.keys():
            freq[w] = freq[w]/m
            if freq[w] >= self._max_cut or freq[w] <= self._min_cut:
                del freq[w]
        return freq

    def summarize(self, text, n):
        sents = sent_tokenize(text) #text tokens
        assert n <= len(sents) #size of tokens
        word_sent = [word_tokenize(s.lower()) for s in sents] #getting tokens from work_tokenizer
        self._freq = self._compute_frequencies(word_sent) #calculating frequencies
        ranking = defaultdict(int)
        #rank most import word in data
        for i,sent in enumerate(word_sent):
            for w in sent:
                if w in self._freq:
                    ranking[i] += self._freq[w]
        sents_idx = self._rank(ranking,n)
        return [sents[j] for j in sents_idx]

    def _rank(self,ranking,n):
        #return first n sentences with highest ranking
        return nlargest(n, ranking, key=ranking.get)

def get_only_text(url):
    #return the title and text of the article at the specified url
    page = urllib2.urlopen(url).read().decode('utf8')
    soup = BeautifulSoup(page)
    text = ' '.join(map(lambda p: p.text, soup.find_all('p')))
    return soup.title.text, text

feed_xml = urllib2.urlopen('http://feeds.bbci.co.uk/news/rss.xml').read()
feed = BeautifulSoup(feed_xml.decode('utf8'))
to_summarize = map(lambda p: p.text, feed.find_all('guid'))

fs = FrequencySummarizer()
for article_url in to_summarize[:5]:
    title, text = get_only_text(article_url)
    print '------------------------------'
    print title
    for s in fs.summarize(text, 2):
        print '*',s 