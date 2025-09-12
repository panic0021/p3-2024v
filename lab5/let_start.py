from datetime import datetime
from sys import stderr
from putnik import Putnik

class Let:
    poletanje_dt_format="%Y-%m-%d %H:%M"

    def __init__(self,broj_leta,vreme_poletanja):
        self.broj_leta=broj_leta
        self.vreme_poletanja=vreme_poletanja
        self.putnici=[]
    
    def __str__(self):
        return f'Broj leta: {self.broj_leta}\nVreme poletanja: {self.vreme_poletanja}\nPutnici: {';'.join([p.ime for p in self.putnici])}'

    @property
    def vreme_poletanja(self):
        if not hasattr(self,'_Let__vreme_poletanja'):
            self.__vreme_poletanja=None
        return self.__vreme_poletanja

    @vreme_poletanja.setter
    def vreme_poletanja(self,value):
        if not isinstance(value,(datetime,str)):
            stderr(f"Greska! Pogresan format je unet za vreme poletanja!")
        if isinstance(value,str):
            value=datetime.strptime(value,Let.poletanje_dt_format)
        if isinstance(value,datetime) and value>datetime.now():
            self.__vreme_poletanja=value


    def dodaj_putnika(self,novi_putnik):
        if not isinstance(novi_putnik,Putnik):
            print(f"Greska! Ulazni argument nije klase Putnik!")
            return
        if novi_putnik in self.putnici:
            print(f"Greska! Putnik {novi_putnik.ime} je vec ukrcan u avion!")
            return
        if not novi_putnik.COVID_bezbedan:
            print(f"Paznja! Putnik {novi_putnik.ime} ne moze biti ukrcan jer nije COVID bezbedan")
            return
        self.putnici.append(novi_putnik)
    
    def vreme_do_poletanja(self):
        razlika=self.vreme_poletanja-datetime.now()
        dani=razlika.days
        sekunde=razlika.seconds
        sati=sekunde//3600
        minuti=(sekunde%3600)//60
        return [dani,sati,minuti]
    def __iter__(self):
        self.__next_index = 0
        return self


    def __next__(self):
        if self.__next_index == len(self.putnici):
            raise StopIteration

        next = self.putnici[self.__next_index]
        self.__next_index += 1
        return next



if __name__ == '__main__':

    lh1411 = Let('LF1411', '2025-12-10 6:50')
    lh992 = Let('LH992', '2025-11-25 12:20')
    
    print("\nLETOVI:\n")
    print(lh1411)
    print()
    print(lh992)
    print()
    #
    bob = Putnik("Bob Smith", "UK", "123456", True)
    john = Putnik("John Smith", "USA", 987656, True)
    anna = Putnik("Anna Smith", "Spain", "987659")
    luis = Putnik.from_string("Luis Bouve; France; 123456; True")
    
    print(f"\nDodavanje putnika na let {lh1411.broj_leta}")
    for p in [bob, john, anna, luis]:
        lh1411.dodaj_putnika(p)
    print()
    print(lh1411)
    print(f"\nPokusaj dodavanja putnika koji je vec u listi putnika za let {lh1411.broj_leta}:")
    lh1411.dodaj_putnika(Putnik("J Smith", "USA", "987656", True))
    print()
    
    print(f"\nPodaci o letu {lh1411.broj_leta} nakon dodavanja putnika na let:\n")
    print(lh1411)
    
    print()
    
    do_poletanja = lh1411.vreme_do_poletanja()
    if do_poletanja:
        dani, sati, mins = do_poletanja
        print(f"Vreme preostalo do poletanja leta {lh1411.broj_leta}: "
              f"{dani} dana, {sati} sati, i {mins} minuta")
    
    print()
    
    print("\nPUTNICI NA LETU LH1411 (iter / next):")
    p_iter = iter(lh1411)
    try:
        while True:
            print(next(p_iter))
    except StopIteration:
        print("Svi putnici su izlistani")
    
    print()
    print("\nPUTNICI NA LETU LH1411 (FOR petlja):")
    for p in iter(lh1411):
        print(p)


