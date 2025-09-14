from sys import stderr
from operator import itemgetter
from statistics import mean

def compute_product(*numbers,squared=False):
    product=1
    if squared:
        for num in numbers:
            product*=num**2
    else:
        for num in numbers:
            product*=num
    return product

numbesss=[1,4,5]
#print(compute_product(*numbesss))

def select_strings(*ss,threshold=3):
    final=list()
    for word in ss:
        unique_chars=list()
        for ch in word:
            if ch.lower() not in unique_chars:
                unique_chars.append(ch.lower())
        if word[0].lower()==word[-1].lower() and len(unique_chars)>threshold:
            final.append(word)
    return final

str_list = ['yellowy', 'Bob', 'lovely', 'Yesterday', 'too']

# print(select_strings('veljaaav','nevoljaN','najjN'))
# print(select_strings(*str_list,threshold=4))

def process_product_orders(lista_porudzbina,discount=None,shipping_cost=10):
    recnik=dict()
    for item in lista_porudzbina:
        total_price=item[2]*item[3]
        if(total_price<100):
            total_price=item[2]*item[3]+shipping_cost
        if not discount==None:
            total_price*=(100-discount)/100
        recnik[item[0]]=total_price
    return recnik



l=[(1,'ringla',12,200),(2,'frizider',5,400),(3,'rerna',4,350)]
#print(process_product_orders(l,discount=0))


import functools
def timer(func):
    @functools.wraps(func)
    def wrapper_timer(*args,**kwargs):
        from time import perf_counter
        start_time=perf_counter()

        value=func(*args,**kwargs)

        working_time=perf_counter()-start_time
        print(f'Function {func.__name__} completed in {working_time:.4f} seconds')

        return value
    return wrapper_timer

@timer
def compute_sum(n):
    sum_of_sums=0
    for i in range(n+1):
        for x in range(i+1):
            sum_of_sums+=i
    return sum_of_sums

@timer
def compute_sum_oneliner(n):
    return sum(i for i in x for x in n)

# print(compute_sum(10000))
# print(compute_sum_oneliner(10000))
@timer
def mean_median_diff(n,k,iterations=100):
    from statistics import mean,median
    from random import randint,seed
    lista=list()
    seed(1)
    for i in range(0,iterations):
        lista_brojeva=list()
        for num in range(n+1):
            lista_brojeva.append(randint(1,k))
        diff=mean(lista_brojeva)-median(lista_brojeva)
        lista.append(diff)
    for i,j in enumerate(lista):
        print(f"Iteracija {i+1}: {j:.4f}")
    print(mean(lista))


# mean_median_diff(100, 250)



from statistics import mean,stdev
import functools
def standardiser(func):
    @functools.wraps(func)
    def wrapper_standardiser(*args,**kwargs):
        flag=False
        for num in args:
            if not isinstance(num,int):
                print("Arguments should be only of type int! Keeping them as they are.")
                flag=True
        if not flag:
            m=mean(args)
            st=stdev(args)
            args=[(arg-m)/st for arg in args]
        func_str=f'Calling function {func.__name__} with positional arguments:'
        func_str+=", ".join([f'{arg:.4f}' for arg in args])
        if kwargs:
            func_str+="\nand keyword arguments: "+",".join(f"{key}={val}" for key,val in kwargs.items())
        print(func_str)

        value=func(*args,**kwargs)
        value=round(value,4)
        return value
    return wrapper_standardiser


@standardiser
def sum_of_sums(*numbers,n=7):
    sum=0
    for num in numbers:
        for i in range(0,n+1,1):
            #print(f'{sum}+={num}**{i})')
            sum+=num**i
    return sum 

numbers=[1,3,5,7,9,11,13]
print(sum_of_sums(*numbers))
