import random
articles=("A","THE")
nouns=("BOY","GIRL","BAT","BALL")
verbs=("HIT","SAW","LIKED")
prepositions=("WITH","BY")
def sentence():
    a=int(input("Enter the number of sentences: "))
    b=0

    while b<a:
        prob=random.randint(1,4)
        if prob==1:
           print(preposition())
           break
        print( NounPhrase()+" "+Verbphrase()+".")
        b+=1
def NounPhrase():
    return random.choice(articles)+" "+random.choice(nouns)
def Verbphrase():
    return random.choice(verbs)+" "+NounPhrase()+" "+preposition()
def preposition():
    return random.choice(prepositions)+" "+NounPhrase()
sentence()
