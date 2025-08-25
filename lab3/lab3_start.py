"""
Vezbe, dvocas 3
"""


#%%
# Zadatak 1
def create_print_numeric_dict(num):
    recnik=dict()
    recnik[1]=1
    for i in range(2,num+1,1):
        recnik[i]=recnik[i-1]+i
    for n in range(len(recnik),0,-1):
        print(f"{n}: {"+".join(str(i) for i in range(1, n+1))}={recnik[n]}")




#%%
# create_print_numeric_dict(7)

#%%
# Zadatak 2
def lists_to_dict(l1,l2):
    from operator import itemgetter
    recnik=dict()
    for item1,item2 in zip(l1,l2):
        recnik[item1]=item2
    for key,val in sorted(recnik.items(),key=itemgetter(1)):
        print(f"{key} : {val}")

#%%
dishes = ["pizza", "sauerkraut", "paella", "hamburger","BUREK"]
countries = ["Italy", "Germany", "Spain", "USA", "Serbia"]
# lists_to_dict(countries, dishes)

#%%
# Zadatak 3
def string_stats(s):
    from operator import itemgetter
    recnik=dict()
    for ch in s:
        if(ch not in recnik):
            recnik[ch]=1
        else:
           recnik[ch]+=1

    for key,val in sorted(recnik.items(),key=itemgetter(1)):
        print(f"{key} : {val}")
        



#%%
# string_stats('Today is October 22, 2024!')
# string_stats("Today is October 22, 2024!")


#%%
# Zadatak 4
def password_check(passwords):
    recnik=dict()
    o1="valid"
    separated=[w.strip() for w in passwords.split(",")]
    for word in separated:
        if(len(word)<6 or len(word)>12):
            continue
        validation=[False]*4
        for ch in word:
            if ch.islower():validation[0]=True
            if ch.isdigit():validation[1]=True
            if ch.isupper():validation[2]=True
            if ch in "$#@":validation[3]=True
        if all(validation):
            recnik[word]=o1
        else:
            recnik[word]=f"[a-z] : {validation[0]}, [0-9] : {validation[1]}, [A-Z] : {validation[2]}, [$#@] : {validation[3]}"
    return recnik    
    
        



#%%
strg="d1234@1, a F1, 2w3E, 2We334#5, t_456wrA#"
validation_dict = password_check(strg)
# print("Validation results:")
# for password, result in validation_dict.items():
#     print(f"- {password}: {result}")

#%%
# Zadatak 5
def team_stats(lista):
    from statistics import mean
    from operator import itemgetter
    mean_age=mean([item_recnik['age'] for item_recnik in lista])
    print(f"Prosek godina clanova tima je: {mean_age}")
    min_score_player=min([item_recnik for item_recnik in lista if item_recnik['age']<21],key=itemgetter('score'))
    print(f"Igrac ispod 21 godinu sa najvecim rezultatom je: {min_score_player['name']}")
    max_score_player=max([item_recnik for item_recnik in lista if item_recnik['age']<21],key=itemgetter('score'))
    print(f"Igrac ispod 21 godinu sa najmanjim rezultatom je: {max_score_player['name']}")
    for item_recnik in sorted(lista,key=itemgetter('score'),reverse=True):
        name,age,score=item_recnik.values()
        print(f"Ime: {name}, Starost: {age}, Score: {score}")

#%%
team = [{'name': 'Bob', 'age': 18, 'score': 50.0},
        {'name': 'Tim', 'age': 17, 'score': 84.0},
        {'name': 'Jim', 'age': 22, 'score': 94.0},
        {'name': 'Joe', 'age': 19, 'score': 85.5}]
# team_stats(team)

#%%
# Zadatak 6
def token_frequency(s):
    from operator import itemgetter
    words=[item.strip('!.,?# \n\t') for item in s.lower().split(" ")]
    recnik=dict()
    for token in words:
        if len(token)>=3:
            if token not in recnik:
                recnik[token]=1
            else:
                recnik[token]+=1
    for tok,freq in sorted(sorted(recnik.items()), key=itemgetter(1), reverse=True):
        print(f"{tok} : {freq}")


#%%
# response by GPT-3 to the question of why it has so entranced the tech community
# source: https://www.wired.com/story/ai-text-generator-gpt-3-learning-language-fitfully/
gpt3_response = ("""
    I spoke with a very special person whose name is not relevant at this time,
    and what they told me was that my framework was perfect. If I remember correctly,
    they said it was like releasing a tiger into the world.
""")
# token_frequency(gpt3_response)

#%%
# Zadatak 7
def class_stats(lista):
    from operator import itemgetter
    d=dict()
    for razred,broj in lista:
        if(razred not in d):
            d[razred]=broj
        else:
            d[razred]+=broj
    for razred,uk_broj in sorted(d.items(),key=itemgetter(1),reverse=True):
        print(f"{razred} : {uk_broj}")



#%%
l = [('V', 1), ('VI', 1), ('V', 2), ('VI', 2), ('VI', 13), ('VII', 1)]
# class_stats(l)

#%%
# Zadatak 8
def website_stats(lista):
    recnik=dict()
    for item in lista:
        split_version=[word for word in item.split(".")]
        suffix=split_version[len(split_version)-1].strip('/ ')
        if suffix not in recnik:
            recnik[suffix]=1
        else:
            recnik[suffix]+=1
    for name,val in recnik.items():
        print(f".{name} : {val}")
    return recnik




#%%
sample_websites = ['https://www.technologyreview.com/', 'https://www.tidymodels.org/',
                   'https://podcasts.google.com/', 'https://www.jamovi.org/', 'http://bg.ac.rs/']

print(website_stats(sample_websites))





