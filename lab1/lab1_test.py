from sys import stderr


def odd_or_even():
    izbor_str=input("Unesite ceo broj: ")
    if not izbor_str.isdigit():
        stderr.write("Neispravan format, unesite ceo broj!")
        return
    izbor=int(izbor_str)
    rez,ostatak=divmod(izbor,2)
    if ostatak==0:
        print("Paran")
    else:
        print("Neparan")
    #print(f"Ostatak je {ostatak} a rezultat je {rez}")

#odd_or_even()

def factorial(num):
    if not isinstance(num,int) or num<0:
        stderr.write("Unesite pozitivan ceo broj!")
        return
    fakt=1
    for i in range(1,num+1,1):
        fakt*=i
    print(fakt)

#factorial(5)

def nth_lowest(items,n):
    if n<0 or n>len(items):
        stderr.write("Greska, neispravni ulazni argumenti.")
        return
    sorted_items=sorted(items)
    return sorted_items[n-1]

# l1=[1,2,41,5,2,4,3,9,10]
# n=5
# print(nth_lowest(l1,n))

def list_stats(numbers):
    from statistics import mean
    import math
    help_val_min=10**100
    min_abs=max(numbers)
    for num in numbers:
        if abs(num)<help_val_min:
            help_val_min=abs(num)
            min_abs=num

    help_val_max=0
    max_abs=min(numbers)
    for num in numbers:
        if abs(num)>help_val_max:
            help_val_max=abs(num)
            max_abs=num

    zbir_neneg=sum([num for num in numbers if num>=0])
    proizvod_neg=math.prod([num for num in numbers if num<0])
    return min_abs,max_abs,zbir_neneg,proizvod_neg


nums=[4,11,99,100,-5,200,3,-3]
# print(list_stats(nums))
# print(list_stats([3.4, 5.6, -4.2, -5.6, 9, 1.2, 11.3, -23.45, -81]))


def list_operations(numbers,threshold):
    nova_lista=[]
    for num in numbers:
        if num<threshold and num not in nova_lista:
            nova_lista.append(num)

    print(f"Broj elemenata u novoj listi: {len(nova_lista)}")
    for i in reversed(sorted(nova_lista)):
        print(f'{i}',end='\n')
    nova_lista.sort(reverse=True)
    for i in nova_lista:
        print(f"{i}",end='\n')


#list_operations([1,4,2,5,1,2,10,15,24,3,22,4],10)

def guess_number():
    from random import randint,seed
    seed(1)
    random_number=randint(1,10)
    print(random_number)

guess_number()