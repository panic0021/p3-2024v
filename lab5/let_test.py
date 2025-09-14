from sys import stderr
from datetime import datetime
from putnik_test import Putnik
class Let():
    poletanje_dt_format='%Y-%m-%d %H:%M'
    def __init__(self,broj_leta,vreme_poletanja):
        self.broj_leta=broj_leta
        self.vreme_poletanja=vreme_poletanja
        self.putnici=list()
    
    @property
    def vreme_poletanja(self):
        try:
            return self.__vreme_poletanja
        except AttributeError:
            self.__vreme_poletanja=None
            return self.__vreme_poletanja
        
    @vreme_poletanja.setter
    def vreme_poletanja(self,value):
        if isinstance(value,str):
            try:
                value_adjusted=datetime.strptime(value,self.poletanje_dt_format)
                if value_adjusted>datetime.now():
                    self.__vreme_poletanja=value_adjusted
                    return
                else:
                    stderr.write("Vreme poletanja se mora odnositi na trenutak u buducnosti.")  
            except ValueError:
                stderr.write("Greska, string nije u ispravnom formatu!")
        elif isinstance(value,datetime):
            #value_adjusted=datetime.strftime(value,self.poletanje_dt_format)
            if value>datetime.now():
                self.__vreme_poletanja=value
                return
            else:
                stderr.write("Vreme poletanja se mora odnositi na trenutak u buducnosti.") 
        else:
            stderr.write("Uneta vrednost mora biti ili string ili datetime.")
            return

    def __str__(self):
        let_str=f'Broj leta: {self.broj_leta}\nVreme poletanja: {self.vreme_poletanja}'
        if self.putnici:
            let_str+=f" "+', '.join([putnik.ime for putnik in self.putnici])
        return let_str


    def dodaj_putnika(self,novi_putnik):
        if not isinstance(novi_putnik,Putnik):
            stderr.write(f"Ulazni objekat nije tipa Putnik!")
            return
        if novi_putnik in self.putnici:
            stderr.write("Putnik je vec ukrcan")
        else:
            if not novi_putnik.COVID_bezbedan:
                stderr.write("Nazalost, putnik nije COVID bezbedan!")
            else:
                self.putnici.append(novi_putnik)


    def preostalo_vreme(self):
        if self.vreme_poletanja:
            diff=self.vreme_poletanja-datetime.now()
            days=diff.days
            seconds=diff.seconds
            minutes,secs_leftover=divmod(seconds,60)
            hours,mins_leftover=divmod(minutes,60)
            return f'Preostalo vremena:\nDana: {days}\nSati: {hours}\nMinuta: {mins_leftover}'
        else:
            stderr.write("Vreme poletanja nije definisano.")

    def __iter__(self):
        self.__next_index=0
        return self
    
    def __next__(self):
        if self.__next_index==len(self.putnici):
            raise StopIteration
        next=self.putnici[self.__next_index]
        self.__next_index+=1
        return next


if __name__=='__main__':
    dt_obj=datetime(2025,9,23,22,16)
    novi_let=Let('12341',dt_obj)
    #print(novi_let)
    veki=Putnik("Veljko",'Srbistan',123455,COVID_bezbedan=True)
    joci=Putnik("Jovan",'Srbistan',123451,COVID_bezbedan=True)

    novi_let.dodaj_putnika(veki)
    novi_let.dodaj_putnika(joci)
    print(novi_let)
    #novi_let.dodaj_putnika(veki)
    print(novi_let.preostalo_vreme())
    for putnik in iter(novi_let):
        print(putnik)


