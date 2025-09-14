from sys import stderr


def create_print_numeric_dict(n):
    recnik=dict()
    if n<=0 or not isinstance(n,int):
        stderr.write("Greska: unesite ceo broj veci od 0")
    recnik[0]=0
    for i in range(1,n+1,1):
        recnik[i]=recnik[i-1]+i
    del recnik[0]
    for key,val in reversed(recnik.items()):
        print(f"{key} : {'+'.join([str(i) for i in range(1,key+1)])} = {val}")

# create_print_numeric_dict(5)


def lists_to_dict(l1,l2):
    from operator import itemgetter
    recnik=dict()
    for key,val in zip(l1,l2):
        recnik[key]=val
    
    for key,val in sorted(recnik.items(),key=itemgetter(1)):
        print(f'{key} : {val}')
    


l1=['Nemacka','Svajcarska','Italija','SAD','Srbija']
l2=['Bratwurst','Muda','Calzone','Hamburger','Gurmanska']
#lists_to_dict(l1,l2)


def string_stats(s):
    recnik=dict()
    for ch in s:
        if ch in recnik:
            recnik[ch]+=1
        else:
            recnik[ch]=1
    return recnik

s='aabbbaa'
#print(string_stats(s))

def team_stats(lista_recnika):
    from statistics import mean
    from operator import itemgetter
    avg_age=mean([recnik['godine'] for recnik in lista_recnika])
    younger_21_min=min([recnik['rezultat'] for recnik in lista_recnika if recnik['godine']<21])
    younger_21_max=max([recnik['rezultat'] for recnik in lista_recnika if recnik['godine']<21])
    print(f'Prosecne godine: {avg_age}\nMladji od 21 najgrdji: {younger_21_min}\nMladji od 21 najbolji: {younger_21_max}')
    for recnik in sorted(lista_recnika,key=itemgetter('rezultat'),reverse=True):
        print(f"Ime: {recnik['ime']}\tGodine: {recnik['godine']}\tRezultat: {recnik['rezultat']}")



d1={'ime':'Veljko','godine':2,'rezultat':55.5}
d2={'ime':'Jovan','godine':20,'rezultat':100}
d3={'ime':'Dusan','godine':9,'rezultat':68}
d4={'ime':'Marko','godine':5,'rezultat':250.5}
lista=[d1,d2,d3,d4]

#team_stats(lista)


def classroom_stats(lista):
    from operator import itemgetter
    recnik=dict()
    for tupl in lista:
        if tupl[0] not in recnik:
            recnik[tupl[0]]=tupl[1]
        else:
            recnik[tupl[0]]+=tupl[1]

    for key,val in sorted(recnik.items(),key=itemgetter(0),reverse=True):
        print(f"Razred: {key} | Broj ucenika: {val}")


lista=[('V', 1), ('VI', 1), ('V', 2), ('VI', 2), ('VI', 3), ('VII', 10)]

classroom_stats(lista)