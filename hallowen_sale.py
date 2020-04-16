class Mist:
    gamenumbers = 0
    def __init__(self,p,d,m,s):
        self.p = p
        self.d = d
        self.m = m
        self.s = s
    def games(self):

        while self.s>=self.m:
            if self.s==self.s:
                self.m==self.d
            else:
                self.s -=self.d
                Mist.gamenumbers +=1
        return Mist.gamenumbers

s = list(map(int,input().split()))
damn = Mist(s[0],s[1],s[2],s[3])
print(damn.games())
