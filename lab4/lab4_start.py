"""
Vezbe, dvocas 4
"""


#%%
# Zadatak 1
def compute_product(*numbers,squared=False):
    product=1
    if not squared:
        for num in numbers:
            product*=num
    else:
        for num in numbers:
            product*=num**2
    return product



#%%
# print(compute_product(1,-4,13,2))
# print(compute_product(1, -4, 13, 2, squared=True))
# # print()
# # # Calling the compute_product function with a list
# num_list = [2, 7, -11, 9, 24, -3]
# # # This is NOT a way to make the call:
# # print("Calling the function by passing a list as the argument")
# print(compute_product(num_list))
# # print()
# # # instead, this is how it should be done (the * operator is 'unpacking' the list):
# # print("Calling the function by passing an UNPACKED list as the argument")
# print(compute_product(*num_list))

#%%
# Zadatak 2
def select_strings(*strs,threshold=3):
    list_of_strs=[]
    for s in strs:
        if len(s)<=threshold:
            continue
        if(s.lower()[0]==s.lower()[len(s)-1]):
            list_of_strs.append(s)
    return list_of_strs



#%%
str_list = ['yellowy', 'Bob', 'lovely', 'Yesterday', 'too']
# print(select_strings(*str_list,threshold=5))

#%%
# Zadatak 3
def process_product_orders(orders, discount=None, shipping_cost=10):
    recnik=dict()
    for item in orders:
        recnik[item[0]]=item[2]*item[3]+shipping_cost
        if discount is not None:
            recnik[item[0]]*=(100-discount)/100
    return recnik


#%%
orders = [("34587", "Learning Python, Mark Lutz", 4, 40.95),
          ("98762", "Programming Python, Mark Lutz", 5, 56.80),
          ("77226", "Head First Python, Paul Barry", 3, 32.95),
          ("88112", "Einführung in Python3, Bernd Klein", 3, 24.99)]
#
# print(process_product_orders(orders,shipping_cost=200))
# print()
# print("The same orders with discount of 10%")
# print(process_product_orders(orders, discount=10))

#%%
#Zadatak 4
import functools
def timer(func):
    @functools.wraps(func)
    def wrapper_timer(*args,**kwargs):
        from time import perf_counter
        start_time=perf_counter()

        value=func(*args,**kwargs)

        working_time=perf_counter()-start_time
        print(f"Function {func.__name__} completed its task in {working_time:.4f} seconds")

        return value
    return wrapper_timer


#%%
# Zadatak 4.1
@timer
def compute_sum_loop(n):
    full_sum=0
    for x in range(n+1):
        for i in range(x+1):
            full_sum+=i
    return full_sum

@timer
def compute_sum_lc(n):
    return sum([sum(range(x+1)) for x in range(n+1)])

@timer
def compute_sum_mr(n):
    from functools import reduce
    mapping=map(lambda x:sum(range(n+1)),range(n+1))
    return reduce(lambda a,b:a+b,mapping)


#%%
# print(compute_sum_loop(10000))
# print()
# print(compute_sum_lc(10000))
# print()
# print(compute_sum_mr(10000))

#%%
# Zadatak 4.2
@timer
def mean_median_diff(n,k,iterations=10):
    from random import seed,randint
    from statistics import mean,median

    seed(4)
    diffs=[]
    for _ in range(iterations):
        random_numbers=[]
        for _ in range(n):
            random_numbers.append(randint(1,k))
        diffs.append(mean(random_numbers)-median(random_numbers))
    
    for i,diff in enumerate(diffs):
        print(f"Iteration {i}: {diff:.4f}")
    

#%%
#mean_median_diff(10000, 2500)


#%%
#Zadatak 5



#%%
# Zadatak 5.1



#%%
# print(sum_of_sums(1,3,5,7,9,11,13, n=7))

