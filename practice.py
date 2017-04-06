from BricksOfBayes import Pmf, Suite

"""1-Throwing a dice"""
pmf = Pmf()
for x in [1, 2, 3, 4, 5, 6]:
    pmf.Set(x, 1 / 6.0)

"""2-word count """
pmf2 = Pmf()
word_list = ["ali", "seed", "the", "the", "milan"]
for word in word_list:
    pmf2.Incr(word, 1)

pmf2.Normalize()
print pmf2.Prob('the')

"""3-The cookie Problem"""
"""Priors"""
pmfcookies = Pmf()
pmfcookies.Set('Bowl 1', 0.5)
pmfcookies.Set('Bowl 2', 0.5)

"""Multiplying priors with likelihoods"""
pmfcookies.Mult('Bowl 1', 0.75)
pmfcookies.Mult('Bowl 2', 0.5)
pmfcookies.Normalize()

print pmfcookies.Prob('Bowl 1')
print pmfcookies.Prob('Bowl 2')


#
class Cookie(Pmf):
    def __init__(self, hypos):
        Pmf.__init__(self)
        for hypo in hypos:
            self.Set(hypo, 1)
        self.Normalize()

    def Update(self, data):
        for hypo in self.Values():
            like = self.Likelihood(data, hypo)
            self.Mult(hypo, like)
        self.Normalize()

    mixes = {
        'Bowl 1': dict(vanilla=0.75, chocolate=0.25),
        'Bowl 2': dict(vanilla=0.5, chocolate=0.5)
    }

    def Likelihood(self, data, hypo):
        mix = self.mixes[hypo]
        like = mix[data]
        return like


hypos = ['Bowl 1', 'Bowl 2']
pmfCookies2 = Cookie(hypos)
pmfCookies2.Update('vanilla')

for hypo, prob in pmfCookies2.Items():
    print hypo, prob

dataset = ['vanilla', 'chocolate', 'vanilla']
for data in dataset:
    pmfCookies2.Update(data)

for hypo, prob in pmfCookies2.Items():
    print hypo, prob


class Monty(Pmf):
    def __init__(self, hypos):
        Pmf.__init__(self)
        for hypo in hypos:
            self.Set(hypo, 1)
        self.Normalize()

    def Update(self, data):
        for hypo in self.Values():
            like = self.Likelihood(data, hypo)
            self.Mult(hypo, like)
        self.Normalize()

    def Likelihood(self, data, hypo):
        if hypo == data:
            return 0
        elif hypo == 'A':
            return 0.5
        else:
            return 1


hypos = 'ABC'
pmfMonty = Monty(hypos)
data = 'B'
pmfMonty.Update(data)

for hypo, prob in pmfMonty.Items():
    print hypo, prob

print "This is when using encapsulated framework"


class MontyHall(Suite):
    def Likelihood(self, data, hypo):
        if hypo == data:
            return 0
        elif hypo == 'A':
            return 0.5
        else:
            return 1


suite = MontyHall('ABC')
suite.Update('B')
suite.Print()


