
from sympy import Eq,solve,symbols
import math
def modeChecker(pattern):
    pat = pattern.split('/')
    if(len(pat) > 2):
        if(pat[0] == 'D' and pat[1] == 'D'):
            return Deter()

#start of deterministic
class Deter:
    lambdda = 1
    meu = 0
    k = 0
    ti = 0
    m = 0
    # find ti

    def tI(self):
        if(self.lambdda > self.meu):
            self.tICase1()
        else:
            self.tICase2()

    # ti case1 self.lambdda > self.meu
    def tICase1(self):
        #self.ti = int((self.k-(self.meu/self.lambdda))/(self.lambdda-self.meu))
        Ti = symbols('Ti')
        eq = Eq(((self.lambdda * Ti) - ((self.meu * Ti) - (self.meu / self.lambdda))), self.k)
        self.ti=solve(eq)[0]
        ktemp = self.k
        while(ktemp == self.k):
            self.ti = self.ti-(1/self.lambdda)
            #ktemp = int(self.ti*self.lambdda)-int((self.ti*self.meu)-(self.meu/self.lambdda))
            x1, x2 = symbols('x1, x2')  # brake ti eq into 2 parts
            x1 = solve(Eq(self.lambdda * self.ti, x1))[0]  # get first part value
            x2 = solve(Eq((self.meu * self.ti) - (self.meu / self.lambdda), x2))[0]  # get second part value
            ktemp= math.floor(x1)-math.floor(x2)

        self.ti += (1/self.lambdda)
        self.ti=int(self.ti)

    # ti case2 self.lambdda <= self.meu

    def tICase2(self):
        
        self.ti = int(self.m/(self.meu-self.lambdda))
        mtemp = self.m
        while(mtemp == self.m):
            self.ti = self.ti-(1/self.lambdda)
            mtemp = int(self.ti*self.meu)-int(self.ti*self.lambdda)
            
        
        self.ti += (1/self.lambdda)
        self.ti=int(self.ti)
        
    

    # find nt
    def nT(self):
        if(self.lambdda > self.meu):
            return self.nTCase1()

        else:
            return self.nTCase2()

    def nTCase1(self):
        nt = []
        i = 0
        l = int(1/self.lambdda)
        for t in range(l, self.ti+(l*5), l):
            nt.append(int(t*self.lambdda)-(int((t*self.meu)-(self.meu/self.lambdda))))
            if(nt[i] >= self.k):
                nt[i] = self.k-1
            i += 1
        return nt

    def nTCase2(self):
        nt = []
        i = 0
        l = int(1/self.lambdda)
        rang = int(self.ti+(l*5))
        for t in range(0, rang, l):
            nt.append(int(self.m+(self.lambdda*t)-(self.meu*t)))
            if(t > 10):
                nt[i] = 1
            i += 1
        return nt

    #calculate wq(n)
    def wqN(self, n):
        #case1
        if(self.lambdda > self.meu):
            if(n<int(self.lambdda*self.ti)):
                if(n==0):
                    return 0
                else:
                    return ((1/self.meu)-(1/self.lambdda))*(n-1)
            elif(n>=int(self.lambdda*self.ti)):
                if((1/self.meu)%(1/self.lambdda)!=0):
                    return int(((1/self.meu)-(1/self.lambdda))*((self.lambdda*self.ti)-3)),int(((1/self.meu)-(1/self.lambdda))*((self.lambdda*self.ti)-2))
                #the special case when 1/lambdda = m (1/meu)
                else:
                    return int(((1/self.meu)-(1/self.lambdda))*((self.lambdda*self.ti)-2))
        
        #case2
        elif(self.meu > self.lambdda):
            if(n == 0):
                return int((self.m-1)/(2*self.meu))
            elif (n <= int(self.lambdda*self.ti)):
                return int((self.m-1+n)*(1/self.meu)-n*(1/self.lambdda))
            elif (n > int(self.lambdda*self.ti)):
                return 0
        else:
            return int((self.m-1)*(1/self.meu))
#end of deterministic

#start of socjastic
class sochasitc:
    lambdaa=0
    meu=0
    k=0
    def L(self):
        if(k==0):
            return int((self.lambdaa)/(self.meu-self.lambdaa))
        else:
            if(self.lambdaa/self.meu!=1):
                numerator= 1-((k+1)*self.raw(k))+(k*self.raw(k+1))
                denominator=(1-self.raw(1))*(1-self.raw(k+1))
                return self.raw(1)*(numerator/denominator)
    def Lq(self):
        if(k==0):
            return (self.lambdaa*self.lambdaa)/(self.meu*(self.meu-self.lambdaa))
        else:
            return self.lambdaa*(1-self.Pk())*self.Wq()

    def Wq(self):
        if(k==0):
            return (self.lambdaa/(self.meu*(self.meu-self.lambdaa)))
        else:
            return self.W()-(1/self.meu)

    def W(self):
        if(k==0):
            return int(1/(self.meu-self.lambdaa))
        else:
            return self.L()/(self.lambdaa*(1-self.Pk()))

    def raw(self,num):
        return (self.lambdaa/self.meu)**num
    
    def Pk(self):
        if(self.raw(1)!=1):
            return self.raw(k)*((1-self.raw(1))/(1-self.raw(k+1)))
        else:
            return 1/(k+1)
soch=sochasitc()
soch.lambdaa=2
soch.meu=2.4
k=5

print(soch.Lq())