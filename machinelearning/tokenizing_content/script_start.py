import nltk
import pprint
# pip install nltk

tokenizer = None
tagger = None
nltk.download('brown')

def init_nltk():
    global tokenizer
    global tagger
    tokenizer = nltk.tokenize.RegexpTokenizer(r'\w+|[^\w\s]+')
    tagger = nltk.UnigramTagger(nltk.corpus.brown.tagged_sents())

def tag(text):
    global tokenizer
    global tagger
    if not tokenizer:
        init_nltk()
    tokenized = tokenizer.tokenize(text)
    tagged = tagger.tag(tokenized)
    tagged.sort(lambda x,y:cmp(x[1],y[1]))
    return tagged

def main():
    text = """
            Well, as usual after watching a Fast and Furious movie, I was always amazed by how crazy
            the action stunts in every installment. It was like they tried to make it bigger, better 
            and crazier in each movie. This one is no exception. The action sequences were all there, 
            from the street car racing (which is the movie's unique specialty), the fighting scenes 
            (made even more special with the addition of Jason Statham), and of course the car chase 
            involving sooo many vehicles.
            In term of story, I think the writers were quite smart to make the story intriguing with 
            the betrayal of Dom to his family. They even made some surprising twists (though they were 
            quite easily guessed by us audiences), nevertheless, kudos for their effort. The most 
            surprising thing about the movie was the amount of funny scenes which I think were quite 
            significant. The moments involving Tyrese Gibson were hilarious and even Jason Statham also 
            had some moments as well.
            The movie also had some brief appearances and cameos by few characters from previous movies 
            and a new interesting character played by Helen Mirren. I think she would appear in the 
            future installments as well. One thing that I am quite amazed was how smart the people behind 
            the franchise were. They have made the movie evolved again from originally a street car movies, 
            to heist and now more like spy thing. But of course all the ingredients of Fast and Furious were 
            still kept in tact. The special effects of the movie were good, the sound effects should be good 
            (though I did not experience it as I watched it in the studio with normal sound system). I am 
            seriously tempted to watch it again in a cinema with the cool sound system just to re-live the 
            scenes with better sound.
    """
    tagged = tag(text)
    l = list(set(tagged))
    l.sort(lambda x,y:cmp(x[1],y[1]))
    pprint.pprint(l)

if __name__ == '__main__':
    main()