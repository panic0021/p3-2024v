from sys import stderr
from datetime import datetime

class Putnik():

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
    
    @cena_karte.setter
    def cena_karte(self,value):
        if isinstance(value, (int, float)) and value > 0:
            self.__cena_karte = int(value)
            return
        if isinstance(value, str):
            try:
                value = int(value)
            except ValueError:
                stderr.write(f"Greska! Uneti string {value} se ne moze parsirati u int vrednost\n")
                return
            if value > 0:
                self.__cena_karte = value
        else:
            stderr.write(f"Greska! Pogresan tip ulazne vrednosti ({type(value)}) => cena karte nije postavljena\n")

    @property
    def pasos(self):
        # if not hasattr(self,'_Putnik__pasos'):
        #     self.__pasos=None
        # return self.__pasos
        #Option 2:EAFP
        try:
            return self.__pasos
        except AttributeError:
            self.__pasos=None
            return self.__pasos
    
    @pasos.setter
    def pasos(self,value):
        if isinstance(value,int):
            if len(str(value))==6:
                self.__pasos=str(value)
            else:
                stderr.write("Passport input value must be 6 digits!")
            return
        if isinstance(value,str):
            if len(value)==6 and value.isdigit():
                self.__pasos=value
            else:
                stderr.write("Passport input value must be must consist of digits only, and 6 of them!")
            return
        stderr.write(f'Input value should be a string or int, not {type(value)}.')

    def __str__(self):
        putnik_str=f'Putnik: {self.ime}\n\t-drzava: {self.drzava}\n\t-broj pasosa: {self.pasos}\n\t-cena karte: {self.cena_karte}\n\t-COVID bezbedan:{self.COVID_bezbedan}'
        if not len(self.usluge)==0:
            putnik_str+=','.join([usluga.value for usluga in self.usluge])
        return putnik_str

    def azuriraj_COVID_bezbedan(self,tip_uverenja,datum_uverenja):
        if not tip_uverenja.lower() in ['vakcinacija','negativan_test']:
            stderr.write(f'Uneta vrednost za tip_uverenja: {tip_uverenja} nije odgovarajuca!')
            return
        if not isinstance(datum_uverenja,(datetime,str)):
            stderr.write('Datum uverenja mora biti string ili datetime!')
            return
        if isinstance(datum_uverenja,str):
            try:
                datum=datetime.strptime(datum_uverenja,'%d/%m/%Y')
                if datum>datetime.now():
                    stderr.write('Datum uverenja mora biti u proslosti!')
                    return
                diff=datetime.now()-datum
                if tip_uverenja=='vakcinacija' and diff.days<365:
                    self.COVID_bezbedan=True
                    return
                if tip_uverenja=='negativan_test' and diff.days<3:
                    self.COVID_bezbedan=True
                    return
            except ValueError:
                stderr.write(f'Datum mora biti u odgovarajucem formatu: %d/%m/%Y')
                return
        if isinstance(datum_uverenja,datetime):
            if datum_uverenja>datetime.now():
                stderr.write('Datum uverenja mora biti u proslosti!')
                return
            diff=datetime.now()-datum_uverenja
            if tip_uverenja=='vakcinacija' and diff.days<365:
                    self.COVID_bezbedan=True
                    return
            if tip_uverenja=='negativan_test' and diff.days<3:
                    self.COVID_bezbedan=True
                    return
    @classmethod
    def from_string(cls,s):
        if not len(s.split('; '))==4:
            stderr.write('Ne valja format!')
            return None
        ime,drzava,pasos,covid_status=s.split('; ')
        return cls(ime,drzava,pasos,covid_status)

    def __eq__(self,other):
        return isinstance(other,Putnik) and other.drzava==self.drzava and other.pasos==self.pasos


if __name__=='__main__':
    john=Putnik('Veljko','Avganistan','123432',14124.2,COVID_bezbedan=False)
    print(john)
    john.azuriraj_COVID_bezbedan('negativan_test',datetime(2025,9,12))
    print(john)
    s='Veljko; Avganistan; 123432; True'
    veljko=Putnik.from_string(s)
    print(veljko)
    print(john==veljko)