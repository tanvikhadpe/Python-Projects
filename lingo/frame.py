import random
def return_word():
        f=open("words.txt",'r')
        data=f.read()
        f.close()
        data=data.split('\n')
        Data = [word for word in data if len(word)==4]
        s =[word for word in Data if (((len(set(word)))==4))]
        return random.choice(s)
x=return_word()
