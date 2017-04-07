from BricksOfBayes import Suite



class CookieWithoutReplacement (Suite):
    mixes = {
        'Bowl 1': dict(vanilla=0.75, chocolate=0.25),
        'Bowl 2': dict(vanilla=0.5, chocolate=0.5)
    }
    def Likelihood(self, data, hypo):
        mix = self.mixes[hypo]
        like = mix[data]
        self.mixes[hypo] = [dict(vanilla=0.75, chocolate=0.25), dict(vanilla=0.5, chocolate=0.5)]
        return like

