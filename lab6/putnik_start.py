from datetime import datetime
from sys import stderr
class Putnik:
    def __init__(self,ime,drzava,pasos,cena_karte,COVID_bezbedan=False):
        self.ime=ime
        self.drzava=drzava
        self.pasos=pasos
        self.cena_karte=cena_karte
        self.COVID_bezbedan=COVID_bezbedan
        self.usluge=list()

    @property
    def cena_karte(self):
        if not hasattr(self,'_Putnik__cena_karte'):
            self.__cena_karte=None
        return self.__cena_karte

        # Option 2: EAFP
        # try:
        #     return self.__cena_karte
        # except AttributeError:
        #     self.__cena_karte=None
        #     return self.__cena_karte

    @cena_karte.setter
    def cena_karte(self,value):
        if not isinstance(value,(int,float,str)):
            stderr(f"Uneti tip vrednosti {type(value)} ne odgovara tipu podatka!")
        if isinstance(value,(int,float)) and value>=0:
            self.__cena_karte=int(value)
            return
        if isinstance(value,str) and value.isdigit() and int(value)>=0:
            self.__cena_karte=int(value)


    @property
    def pasos(self):
        # if not hasattr(self,'_Putnik__pasos'):
        #     self.__pasos=None
        # return self.__pasos
        #Easier to ask for forgiveness than permission
        try:
            return self.__pasos
        except AttributeError:
            self.__pasos=None
            return self.__pasos
    
    @pasos.setter
    def pasos(self,value):
        if isinstance(value,str) and len(value)==6 and value.isdigit():
            self.__pasos=value
            return
        if isinstance(value,int) and 100000<=value<=999999:
            self.__pasos=str(value)
            return
        stderr.write(f'Pogresno uneta vrednost za pasos => nije izvrsena dodela vrednosti')
    
    def __str__(self):
        putnik_str=f'Putnik: {self.ime}\n\t-drzavljanstvo: {self.drzava}\n\t-broj pasosa: {self.pasos}\n\t-cena karte: {self.cena_karte}\n'
        putnik_str+=f'\t-COVID-bezbedan: {'DA' if self.COVID_bezbedan else 'NE'}\n'
        return putnik_str

    def __eq__(self,other):
        return isinstance(other,Putnik) and self.pasos==other.pasos and self.drzava==other.drzava


    @classmethod
    def from_string(cls,putnik_string):
        delovi=[deo.strip() for deo in putnik_string.split(';')]
        if len(delovi)==5:
            ime,zemlja,broj_pasosa,cena_karte,kovid_status=delovi
            return cls(ime,zemlja,broj_pasosa,cena_karte,kovid_status)
        stderr.write(f'Greska! Ulazni string nije odgovarajuceg formata!')
        return None

    def azuriraj_COVID_bezbedan(self,tip_uverenja,datum_uverenja):
        if tip_uverenja.lower() not in ['vakcinacija','negativan_test']:
            stderr.write(f'Neispravan unos tipa uverenja.')
            return
        if not isinstance(datum_uverenja,(datetime,str)):
            stderr.write(f'Neispravan unos datuma uverenja')
            return
        if isinstance(datum_uverenja,str):
            datum=datetime.strptime(datum_uverenja,'%d/%m/%Y')
        print(datetime.now())
        time_delta=datetime.now()-datum
        if tip_uverenja.lower() == 'vakcinacija' and time_delta.days<365:
            self.COVID_bezbedan=True
        if tip_uverenja.lower() == 'negativan_test' and time_delta.days<3:
            self.COVID_bezbedan=True

if __name__ == '__main__':

    bob = Putnik("Bob Smith", "UK", "123456", 250.0, True)
    john = Putnik("John Smith", "USA", 987656, 450, True)
    anna = Putnik("Anna Smith", "Spain", "987659", 375)
    luis = Putnik.from_string("Luis Bouve; France; 123456; 225; True")

    print("PUTNICI:\n")
    print(bob)
    print(john)
    print(anna)
    print(luis)

    print("\nPUTNICI NAKON UPDATE-a COVID STATUS-a:\n")
    anna.azuriraj_COVID_bezbedan('vakcinacija', '01/02/2024')
    print(anna)

    luis.azuriraj_COVID_bezbedan('negativan_test', '04/11/2024')
    print(luis)
    print()

    print("Provera da li su 'bob' i 'john' reference na istog putnika")
    print("Isti putnik" if bob == john else "Razliciti putnici")
    print()
    print("Provera da li su 'john' i 'johnny' reference na istog putnika")
    johnny = Putnik("Johnny Smith", "USA", 987656, 650, False)
    print("Isti putnik" if john == johnny else "Razliciti putnici")
