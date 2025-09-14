from sys import stderr

def concat_index_wise(l1,l2):
    l=list()
    if not len(l1)==len(l2):
        stderr.write("Nisu jednake duzine listi.")
        return
    for s1,s2 in zip(l1,l2):
        print(s1+s2)
        l.append(s1+s2)
    return l


list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]
#print(concat_index_wise(list1,list2))

def digits_in_string(s):
    num_list=list()
    for ch in s:
        if ch.isdigit():
            num_list.append(ch)
    return num_list

#print(digits_in_string('abasfaf'))

def palindrom(s):
    text=[ch.lower() for ch in s if ch not in " ,.?!"]
    print(text)
    return text==list(reversed(text))

#print(palindrom('!!!!!!!!!aa  Aaa!!!!!!!!'))

def password_check(passwords):
    passwords_t=[word.strip() for word in passwords.split(',')]
    correct=list()
    for word in passwords_t:
        if not 6<=len(word)<=12:
            continue
        indices=4*[False]
        for ch in word:
            if ch.islower(): indices[0]=True
            if ch.isdigit(): indices[1]=True
            if ch.isupper(): indices[2]=True
            if ch in '$#@': indices[3]=True
        if all(indices):
            correct.append(word)

    print(f"Pravilne lozinke: {','.join(correct)}")



passwords_to_check = "ABd1234@1, a F1#, 2w3E*, 2We334#5, t_456WR,123425aB#"
#password_check(passwords_to_check)

def server_status(server_list):
    from operator import itemgetter
    sredjeno=[row.strip() for row in server_list.split('\n') if row.strip()!='']
    server_names=dict()
    for item in sredjeno:
        words=[word for word in item.split(' ')]
        server_names[words[1]]=words[3]
    not_working=len([key for key,val in server_names.items() if val=='down'])
    procenat=f'{not_working/len(server_names):.4f}'

    print(f'Broj servera: {len(server_names)}\nProcenat onih koji ne rade: {procenat}\nServeri koji ne rade: {','.join([key for key,val in server_names.items() if val=='down'])}')


server_state_log = '''
    Server abc01 is up
    Server abc02 is down
    Server abc03 is down
    Server xyz01 is down
    Server xyz02 is up
    Server abc02 is up
    Server abc01 is down
    '''
#server_status(server_state_log)

def anagram(s1,s2):
   s1=[ch.lower() for ch in s1 if ch.isalnum()]
   s2=[ch.lower() for ch in s2 if ch.isalnum()]

   return len(s1)==len(s2) and sorted(s1)==sorted(s2)

print(anagram('ana voli milovana','milovana voli ana'))
print(anagram('ortoped', 'torpedo'))
print(anagram('ortopedi', 'torpedo'))
print(anagram('On sa tla Like', 'Nikola Tesla'))