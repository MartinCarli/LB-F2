import random

class   Automa:
    def __init__(self, biancheria, calzini, maglia, pantaloni, calzatura):
        self.biancheria=None
        self.calzini=None
        self.maglia=None
        self.pantaloni=None
        self.calzatura=None


    def indossa_biancheria(self):
        rand=random.randint(0,1)
        if rand==1:
            self.biancheria=True
        else:
            self.biancheria=False
        return rand

        
    def indossa_calzini(self):
        rand=random.randint(0,1)
        if rand==1:
            self.calzini=True
        else:
            self.calzini=False
        return rand

    def indossa_maglia(self):
        rand=random.randint(0,1)
        if rand==1:
            self.maglia=True
        else:
            self.maglia=False
        return rand


    def indossa_pantaloni(self):
        rand=random.randint(0,1)
        if rand==1:
            self.pantaloni=True
        else:
            self.pantaloni=False
        return rand


    def indossa_calzatura(self):
        rand=random.randint(0,1)
        if rand==1:
            self.calzatura=True
        else:
            self.calzatura=False
        return rand

def esegui(self, capo):
    if capo=="biancheria":
        a=self.indossa_biancheria()
    if capo=='calzini':
        a=self.indossa_calzini()
    if capo=='maglia':
        a=self.indossa_maglia()
    if capo=='pantaloni':
        a=self.indossa_pantaloni()
    if capo=='calzatura':
        a=self.indossa_calzatura()
    return a

automa1=Automa(0, 0, 0, 0, 0)         
capi_vestiario=['biancheria', 'calzini', 'maglia', 'pantaloni', 'calzatura']
vestito= True
i=0


while (vestito):
    capo_da_indossare=random.choice(capi_vestiario)
    print(capo_da_indossare)
    if(capo_da_indossare==capi_vestiario[i]):
        print('il capo puo essere indossato')
        test=esegui(automa1,capo_da_indossare)
        if (test==0):
            raise Exception('l automa non e stato in grado di indossare il capo')
        i=i+1
    else:
        print('il capo non puo essere indossato')

    if (i==5):
        vestito=False
    
    print('vestito correttamente')


