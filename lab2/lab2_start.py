#%%
# Zadatak 1 
def concat_index_wise(l1,l2):
    if len(l1)!=len(l2):
        print("Neispravne liste unete, mora biti jednak broj stringova!")
        return
    duzina=len(l1)
    l3=[]
    for i in range(0,duzina,1):
        l3.append(l1[i]+l2[i])
    return l3




#%%
list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]
#print(concat_index_wise(list1, list2))

#%%
# Zadatak 2

def digits_in_string(s):
    numbers=[]
    for i in range(0,len(s),1):
        if(s[i].isdigit()):
            numbers.append(int(s[i]))
    return numbers


#%%
# Test the function
s1 = "Tokyo's 2024 population is now estimated at 37,115,035."
s2 = "Tokyo is one of the most populated cities."
#print(digits_in_string(s1))
##print(digits_in_string(s2))
#
#%%
# Zadatak 3
def palindrom(s):
    s=s.replace(" ","").replace(",","").replace(".","").replace("!","").replace("?","").lower()
    for i in range(0,len(s),1):
        if(s[i]!=s[len(s)-i-1]):
            return False
    return True

#%%

# s1 = "potop"
# print(f"{s1}: {palindrom(s1)}")
# s2 = "Si... !!  !,,,.,., .,,.r ima miris!!!!!!!!!!!         !"
# print(f"{s2}: {palindrom(s2)}")
# s3 = "ananas"
# print(f"{s3}: {palindrom(s3)}")

#%%
# Zadatak 4
def password_check(lozinke):
    



#%%
# Test the function
# passwords_to_check = "ABd1234@1, a F1#, 2w3E*, 2We334#5, t_456WR"
# print(f"Passwords to check: {passwords_to_check}")
# passwords_check(passwords_to_check)


#%%
# Zadatak 5




#%%
# Test the function
# server_state_log = '''
#     Server abc01 is up
#     Server abc02 is down
#     Server abc03 is down
#     Server xyz01 is up
#     Server xyz02 is up
#     Server abc02 is up
#     Server abc01 is down
#     '''
# server_status(server_state_log)


#%%
# Zadatak 6




#%%
# Test the function
# print(anagram('ortoped', 'torpedo'))
# print(anagram('ortopedi', 'torpedo'))
# print(anagram('On sa tla Like', 'Nikola Tesla'))

#%%
# Zadatak 7




#%%
# Test the function
# all_even_digits()
