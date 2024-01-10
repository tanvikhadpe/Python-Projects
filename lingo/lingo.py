import frame
def fun():
            word = frame.return_word()
            #print word
            guesslst=[]
            while guesslst != word:
                new = []
                guess = input("Enter word: ")
                if(guess == 'revl'):
                    print (word)
                guesslst = list(guess)
                for x in guesslst:
                    if x in word:
                        for y in word:
                            if x == y:
                                if word.index(y) == guesslst.index(x):
                                    if x not in new:
                                        new.append("[%s]" %x)
                                else:
                                    if x not in new:
                                        new.append("(%s)" %x)
                    else:
                        if x not in new:
                            new.append(x)
                print("".join(new))
fun()

