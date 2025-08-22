#%%
# Zadatak 1
def odd_or_even():
    num_str=input("Please enter a whole number\n")
    num=int(num_str)
    res,remainder=divmod(num,2)
    print(f"Rezultat: {res} Ostatak: {remainder}")

#%%
# Test the function
#odd_or_even()


#%%
# Zadatak 2
def factorial(number):
    res=1
    for i in range(number,0,-1):
        res*=i
    return res
#%%
# Test the function
#print(factorial(4))


#%%
# Zadatak 3
def nth_lowest(items,num):
    if num<=0 or len(items)<num:
        return min(items)
    return sorted(items)[num-1]




#%%
# Test the function with...
# ... a sequence of numbers:
# numbers  = [31, 72, 13, 41, 5, 16, 87, 98, 9]
# print(f"3rd lowest among numbers: {numbers}:")
# print(nth_lowest(numbers,3))

# Zadatak 4
# Napišite funkciju (list_stats) koja prima listu brojeva (numbers) i
# vraća uređenu n-torku sa sledećim elementima:
# - najmanji element liste po apsolutnoj vrednosti
# - najveći element liste po apsolutnoj vrijednosti
# - zbir svih nenegativnih elemenata u listi
# - proizvod svih negativnih elemenata u listi

def list_stats(numbers):
    min_abs=max_abs=numbers[0]
    sum_positive=0
    prod_negative=1
    for i in range(0,len(numbers),1):
        if abs(numbers[i])<abs(min_abs):
            min_abs=numbers[i]
        if abs(numbers[i])>abs(max_abs):
            max_abs=numbers[i]
        if numbers[i]>=0:
            sum_positive+=numbers[i]
        else:
            prod_negative*=numbers[i]

    return min_abs,max_abs,sum_positive,prod_negative


# ... a sequence of letters:
# letters = ['f', 'r', 't', 'a', 'b', 'y', 'j', 'd', 'c']
# print(f"6th lowest among letters: {letters}:")
# print(nth_lowest(letters, 6))

# ... a string:
# s = "today"
# print(f"2nd lowest in string: '{s}':")
# print(nth_lowest(s, 2))


#%%
# Zadatak 4






#%%
# Test the function
#print(list_stats([3.4, 5.6, -4.2, -5.6, 9, 1.2, 11.3, -23.45, -81]))
# Zadatak 5
# Napišite funkciju (list_operations) koja prima dva ulazna argumenta:
# listu brojeva (numbers) i jedan celi broj (threshold). Funkcija bi trebalo da:
# - kreira novu listu sa jedinstvenim elementima iz ulazne liste (numbers) koji su ispod praga (threshold)
# - ispisuje broj elemenata u novoj listi
# - sortira elemente u novoj listi u opdajućem redosledu i ispisuje ih, po jedan element u redu


#%%
# Zadatak 5
# def list_operations(numbers,threshold):
#     new_numbers=[]
#     for num in numbers:
#         if(num<threshold):
        



#%%
# Test the function
# list_operations([1, 1, 2, 3, 5, 8, 13, 5, 21, 34, 55, 89], 20)



#%%
# Zadatak 6
# Napišite funkciju (guessing_game) za igranje igre pogađanja broja između 1 i 9.
# Preciznije, funkcija bi trebalo da emulira sledeći scenario:
# Korisniku se najpre prikaže par osnovnih informacija o igri.
# Zatim se korisniku daje mogućnost da pogodi broj koji je funkcija "zamislila".
# Ako korisnik ne pogodi, daje mu se mogućnost ponovnog pogađanja.
# Korisnik može pokušati da pogodi maksimalno 3 puta.
# U slučaju uspešnog pogađanja, trebalo i ispisati poruku "Tacno - broj je <broj>! Bravo!" i funkcija se završava.
# Ako prilikom pogađanja korisnik unese broj koji je izvan granica (manji od 1 ili veći od 9) ili znak koji nije broj,
# trebalo bi prikazati poruku da su dopušteni samo jednocifreni brojevi. Ovakvu grešku ne računati kao neuspešno pogađanje.

# Saveti:
# - možete koristiti funkciju 'randint' iz paketa 'random' za generiranje broja koji se pogađa u igri
# - string funkcija 'isdigit' može se koristiti za proveru je li je uneta vrednost broj
def guessing_game():
    from random import randint
    correct=randint(1,9)
    print(f"{correct}")
    print("Dobrodosli u igru pogadjanja, imate 3 pokusaja!\n")
    counter=0
    while counter<3:
        guess=input("Unesite broj: ")
        if not guess.isdigit() or int(guess)<1 or int(guess)>9:
            print("Dopusteni su samo jednocifreni brojevi!\n")
            continue
        if int(guess)==correct:
            print(f"Tacno - broj je {guess}! Bravo!\n")
            return
        else:
            counter+=1
            print(f"Nije tacan broj! Imate jos {3-counter}\n")
    print("Niste pogodili nazalost!")





#%%
# Test the function
guessing_game()


# %%
