#calcolatrice



# inizio con fare i vari test  
def testzero(self,a):
    b=False 
    if  a==0:
        b=True
    return b

def test_int(self,a): 
    self.a=a
    b=False
    if isinstance(a,int):
        b=True
    return b

def test_i_f(self,b):
    self.b=b
    c=False
    if isinstance(b,int):
        c=True
    if isinstance(b,float):
        c=True

def test_pos(slef,p):
    self.p=p 
    b=false
    if p>0:
        b=True
    return b

def trasf_pos(self,p):
    print('ATTENZIONE: per fare questo calcolo bisogna avere soltanto numeri positivi, adesso cambio il segno del valore')
    p= -1 * p
    return p

######  inizio a fare la funzioni della calcolatrice

def somma(self,numberlist):
    cerca=1
    i=0
    som=0
    if not isinstance(numberlist,list):
        print('ATTENZIONE (somma): la variabile {} non e` di tipo lista'.format(numberlist))
    
    else:
        for item in numberlist:
            if(test_i_f(item[0])==False):
                cerca=cerca*0
            i=i+1
        if(cerca==1):
            for item in numberlist:
                som= item + som
            return som
        if(cerca==0):
            print('ATTENZIONE (somma): Il numero deve essere di tipo int o float')


def divisione(self,numberlist):
    c=0
    n=len(numberlist)
    if n>2:
        print('ATTENZIONE (divisione): la lista deve contenere soltanto due numeri')
    else:
        elements= list.split(',')
        if test_i_f(elements[0])==False):
            print('ATTENZIONE (divisione): Il numero deve essere di tipo int o float')
        elif(test_i_f(elements[1]==False)):
            print('ATTENZIONE (divisione): Il numero deve essere di tipo int o float')
        elif (testzero(elements[1]==True)):
            print('ATTENZIONE (divisione): non si puo` dividere per 0')
        else:
            c=elements[0]/elements[1]
            return c

    
def potenza(self,numberlist):
    c=0
    n=len(numberlist)
    if n>2:
        print('ATTENZIONE: la lista deve contenere soltanto due numeri')
    else:
        elements= list.split(',')
        if test_int(elements[0])==False):
            print('ATTENZIONE: Il numero deve essere di tipo int')
        elif(test_i_f(elements[1]==False)):
            print('ATTENZIONE: Il numero deve essere di tipo int')
        elif (testzero(elements[1]==True)):
            print('ATTENZIONE: non si puo` dividere per 0')
        else:
            c=elements[0]/elements[1]
            return c
