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
    password_list=[]
    for word in lozinke.split(","):
        password_list.append(word.strip())
    valid_passwords = []
    for word in password_list:
        if not(len(word)>=6 and len(word)<=12):continue
        par=[False]*4
        for c in word:
            if c.islower():par[0]=True
            if c.isdigit():par[1]=True
            if c.isupper():par[2]=True
            if c in "$#@":par[3]=True
            if len(c)>=6 and len(c)<=12:par[4]:True
        if all(par):
            valid_passwords.append(word)
    print("Validne lozinke su: "+", ".join(valid_passwords))

#%%
# Test the function
# passwords_to_check = "ABd1234@1, a F1#, 2w3E*, 2We334#5, t_456WR"
# print(f"Passwords to check: {passwords_to_check}")
#
# password_check(passwords_to_check)


#%%
# Zadatak 5
def server_status(s):
    rows=[p.strip() for p in s.split("\n")]
    rows=rows[1:-1]
    distinct_servers={}
    for r in rows:
        #print(r)
        row_words=r.split(" ")
        distinct_servers[row_words[1]]=row_words[3]
        # for i in range(0,len(row_words),1):
        #     print(f"{row_words[i]} and {i}")
    ctr=0
    down_servers=[]
    for item in distinct_servers:
        #print(f"{item} : {distinct_servers[item]}")
        if(distinct_servers[item]=="down"):
            down_servers.append(item)
            ctr+=1
    down_servers_num=ctr/len(distinct_servers)
    print(f'''
    Ukupan broj servera: {len(distinct_servers)}
    Procenat servera koji ne rade: {down_servers_num*100:.2f}%
    Serveri koji ne rade: {(", ").join(down_servers)}
    ''')


#%%
# Test the function
server_state_log = '''
    Server abc01 is up
    Server abc02 is down
    Server abc03 is down
    Server xyz01 is up
    Server xyz02 is up
    Server abc02 is up
    Server abc01 is down
    Server xyz02 is down
    Server Veljko is down
    '''
#server_status(server_state_log)


#%%
# Zadatak 6
def anagram(s1,s2):
    l1=[ch.lower() for ch in s1 if ch.isalpha()]
    l2=[ch.lower() for ch in s2 if ch.isalpha()]
    removed=0
    for ch in l1:
        if(ch in l2):
            l2.remove(ch)
            removed+=1
    if(len(l2)==0 and len(l1)==removed):
        print("Jeste anagram!")
    else:
        print("Nije anagram!")
        

# #%%
# print(anagram('ortoped', 'torpedo'))
# print(anagram('ortopedi', 'torpedo'))
# print(anagram('On sa tla Like', 'Nikola Tesla'))

#%%
# Zadatak 7
def all_even_digits():
    num_list=[]
    start=100
    for i in range(start,401,1):
        if((i//100)%2==0 and ((i//10)%10)%2==0 and (i%10)%2==0):
            num_list.append(str(i))

    print((", ").join(num_list))


#%%
# Test the function
all_even_digits()
