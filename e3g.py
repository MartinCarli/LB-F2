
class Calcolatrice:

    def __init__(self, a, b):
        self.a=a
        self.b=b
#somma
    def somma(self):
        try:
            float(self.a) 
            float(self.b)
        except Exception as e:
            print('i valori inseriti non sono numeri:{}'.format(e)) 
            
        print('somma:{}'.format(self.a+self.b))

#sottrazione
    def sottrazione(self):
        try:
            float(self.a) 
            float(self.b)
        except Exception as e:
            print('i valori inseriti non sono numeri:{}'.format(e)) 
        print('sottrazione:{}'.format(self.a-self.b))

#moltiplicazione
    def moltiplicazione(self):
        try:
            float(self.a) 
            float(self.b)
        except Exception as e:
            print('i valori inseriti non sono numeri:{}'.format(e)) 
        print('moltiplicazione{}:'.format(self.a*self.b))

#divisione
    def divisione(self):
        try:
            float(self.a) 
            float(self.b)
        except Exception as e:
            print('i valori inseriti non sono numeri:{}'.format(e))
        else:
            if(self.b==0):
                raise Exception('divisione per zero e ammessa')
            else:
                print('divisione:{}'.format(self.a/self.b))

#potenza
    def potenza(self):
        try:
            isinstance(self.a, int)
            isinstance(self.b, int)

        except Exception as e:
            print('i valori inseriti non sono numeri:{}'.format(e)) 
        print('potenza:{}'.format(pow(self.a, self.b))


#modulo
    def modulo(self):
        try:
            float(self.a) 
            float(self.b)
        except Exception as e:
            print('i valori inseriti non sono numeri:{}'.format(e)) 
            
        print('modulo:{}'.format(abs(self.a-self.b))

#radice
    def radice(self):
        from math import sqrt
        try:
            float(self.a) 
            float(self.b)
        except Exception as e:
            print('i valori inseriti non sono numeri:{}'.format(e)) 
        else:
            if(self.a>0 or self.b>0):
                print('i valori inseriti nelle radice sono ammessi')
            else:
                Exception('i valori inseriti nella radice non sono ammessi:{}, {}'.format(e))
        print('radice:{}'.format(sqrt(self.a)))

#conversione di base
    def conversione_di_base(self):
        try:
            float(self.a) 
            float(self.b)
        except Exception as e:
            print('i valori inseriti non sono numeri:{}'.format(e))
        else:
            from math import log
            if (self.b==10):
                y=log(self.a, self.b)
                print('{}'.format(y))
                y=log(self.a, 2)
                z=log(self.b, 2)
                print('{}'.format(y/z))
            else:
                raise Exception('base non valida')
                



es1=Calcolatrice(4, 10)
es2=Calcolatrice(3, 2)


    
#primo test
print('PRIMO TEST')
es1.somma()
es1.sottrazione()
es1.moltiplicazione()
es1.divisione()
es1.potenza()
es1.modulo()
es1.radice()
es1.conversione_di_base()
#secondo test
print('\n\tSECONDO TEST')
es2.somma()
es2.sottrazione()
es2.moltiplicazione()
es2.divisione()
es2.potenza()
es2.modulo()
es2.radice()
es2.conversione_di_base()







        

        