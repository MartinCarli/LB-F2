class CSVFile:
    def __init__(self, filename):
        self.name=filename
  
    def get_data1(self, start=None, end=None):
    #inizializzo una lista vuota per salvare i valori
        values=[]
        i=start
        #apro e leggo il dile, linea per linea
        try:
            my_file = open(self.name, 'r')
        except:
            print('il file non esiste')
            return None

        for line in my_file:
            #faccio lo split di goni riga sulla virgola
            elements = line.split(',')
            if i<=end+1:
                #se non sto processando l'intestazione
                if elements[0] != 'Date':
                    #setto la data e il valore
                    date = elements[0]
                    value = elements[1]
            
                    #Aggiungo alla lista dei valori questo valore
                    try:
                        float(value)
                    except:
                        print('dati non numerici')
                        continue
                    values.append(value)
            i=i+1
        my_file.close()
        return values
    
    def get_data2(self):
    #inizializzo una lista vuota per salvare i valori
        values=[]
        #apro e leggo il dile, linea per linea
        try:
            my_file = open(self.name, 'r')
        except:
            print('il file non esiste')
            return None

        for line in my_file:
            #faccio lo split di goni riga sulla virgola
            elements = line.split(',')
            #se non sto processando l'intestazione
            if elements[0] != 'Date':
                #setto la data e il valore
                date = elements[0]
                value = elements[1]
          
                #Aggiungo alla lista dei valori questo valore
                try:
                    float(value)
                except:
                    print('dati non numerici')
                    continue
                values.append(value)
        my_file.close()
        return values

    def list_sum(self, dati):
        somma=0
        i=2
        while i<len(dati):
            if (dati[i]!='Date, Sales'):
                try:
                    float(dati)
                except:
                    print('dati non numerici')
            somma = somma+dati[i]
            i = i + 1
        return somma

file=CSVFile('shampoo_sales.csv')
data = file.get_data1(1, 37)
print('\tdata1=', data)

data1=file.get_data2()
print('\n\tdata2=', data1)

print('\tSOMMA1')
somma1 = file.list_sum(data1)
print('\n\tSOMMA2')
somma2 = file.list_sum(data2)


        