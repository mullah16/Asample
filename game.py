class GuessMe(object):
    def __init__(self):
        from random import randint
        self.rand = randint(1, 1000)
        print "welcome to Guess me"

    def guess_value(self):
        i=1
        while i<=10:
            n= int(raw_input("guess the value"))
            if n==self.rand:
                print "you win"
                return
            i=i+1
        print "you lose the number is",self.rand

g = GuessMe()
g.guess_value()



