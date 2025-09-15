from putnik_test import Putnik
from sys import stderr
from statistics import mean,median
from random import randint
from enum import Enum
from operator import itemgetter


class PutnikEkonomskeKlase(Putnik):

    def dodaj_izabrane_usluge(key_dict):
        



    def __str__(self):
        putnik_str=super().__str__()
        putnik_str.replace("Putnik",'Putnik ekonomske klase')
        return putnik_str