#calcolatrice

#       il programma non e` finito, 




# inizio con fare i vari test (di controllo)
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

######  inizio a fare le funzioni della calcolatrice

#somma
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

#sottrrazione


#divisione
def divisione(self,numberlist):
    c=0
    n=len(numberlist)
    if n>2:
        print('ATTENZIONE (divisione): la lista deve contenere soltanto due numeri')
    else:
        elements= list.split(',')
        if test_i_f(elements[0])==False:
            print('ATTENZIONE (divisione): Il numero deve essere di tipo int o float')
        elif(test_i_f(elements[1]==False)):
            print('ATTENZIONE (divisione): Il numero deve essere di tipo int o float')
        elif (testzero(elements[1]==True)):
            print('ATTENZIONE (divisione): non si puo` dividere per 0')
        else:
            c=elements[0]/elements[1]
            return c

#potenza    

#forse ce un errore nel for dove si calcola la potenza 
#                  ~~~~~~CONTROLLA~~~~~~               #

def potenza(self,numberlist):
    c=0
    n=len(numberlist)
    if n>2:
        print('ATTENZIONE: la lista deve contenere soltanto due numeri')
    else:
        elements= list.split(',')
        if test_int(elements[0])==False:
            print('ATTENZIONE (potenza): La base deve essere di tipo int')
        elif(test_int(elements[1])==False):
            print('ATTENZIONE (potenza): L esponente deve essere di tipo int')
        elif test_pos(elements[1])==False:
            print('ATTENZIONE (potenza): L esponente deve essere positivo')
        elif(elements[1]==1):
            return elements[0]
        elif(elements[1]==0):
            return 1
        else:
            i=elements[1]
            a=elements[0]
            for x in range(1,i):
                elements[0]=elements[0]*a
            return elements[0]
        
#radice
def radice(self,numberlist):
    c=0
    n=len(numberlist)
    if n>1:
        print('ATTENZIONE: la lista deve contenere soltanto un numero')
    else:

        if test_int(numberlist)==False:
            print('ATTENZIONE (potenza): Il numero deve essere di tipo int')

        elif test_pos(numberlist)==False:
            print('ATTENZIONE (potenza): Il numero deve essere positivo')
        else:
            return sqrt(numberlist)



es2= [3, 2, 5]

print(somma(es2))

####errore