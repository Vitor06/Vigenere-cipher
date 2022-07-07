from operator import mod
import string
LENGTH_ALPHABET = 26
KEY = 'LEMONLEMONLE'.lower()
# def get_in_tabula(l,c):
#     tabula = tabula_recta()
#     sc = scheme()
#     line = sc.get(l)
#     column = sc.get(c)
#     return  tabula[line][column]

def scheme():
    letters = list(string.ascii_lowercase)
    values = [i for i in range(0,26)]
    scheme = dict(zip(letters,values))

    return scheme

def print_tabula(matrix):
    for line in matrix:
        print(*line)

def read_text():
    with open('input_text_vigenere_cipher.txt','r') as f:
        text = f.read()
    
    return text

#just to see 
def tabula_recta():
    k=0
    alphabet = list(string.ascii_lowercase)
    tabula = [ [ 0 for l in range(LENGTH_ALPHABET) ] for c in range(LENGTH_ALPHABET) ]
   
    for l in range(LENGTH_ALPHABET):
        x = 0
        for c in range(LENGTH_ALPHABET):
            if(c+k<LENGTH_ALPHABET): tabula[l][c] = alphabet[c+k] 
            else: 
                tabula[l][c] = alphabet[x] 
                x+=1
        k+=1
    return tabula

def fill_with_key(text):
    
    text_key = ''
    k  = 0
    for i in range(len(text)):
            if(k>=len(KEY)):k=0
            text_key = text_key +KEY[k]
            k+=1
       
    return text_key

def encrypt(text,sc,text_with_key):
    #NOTE:
    #We can just apply the function get_in_tabula with a map
    #map(get_in_tabula,text_with_key,text_original)

    text_original = list(text)

    #mathematical formula
    C = lambda p,k: mod((p+k),26) if (p and k) is not  None else  ' '
    
    search_value = lambda letter : sc.get(letter)
    search_key = lambda num : [key for key,value in sc.items() if value==num][0] if num!=' ' else ' '

    letter_to_num_text_original = list(map(search_value,text_original))
    letter_to_num_text_with_key = list(map(search_value,text_with_key))
    text_num= list(map(C,letter_to_num_text_original,letter_to_num_text_with_key))
    encrypt_text =list(map(search_key,text_num))
    
    return  ''.join(encrypt_text)
    

def decrypt(encrypt_text,sc,text_with_key):
    encrypt_text = list(encrypt_text)

    #mathematical formula
    P = lambda c,k: mod((c-k)+26,26) if (c and k) is not  None else  ' '
    
    search_value = lambda letter : sc.get(letter)
    search_key = lambda num : [key for key,value in sc.items() if value==num][0] if num!=' ' else ' '
    
    letter_to_num_encrypt_text = list(map(search_value,encrypt_text))
    letter_to_num_text_with_key = list(map(search_value,text_with_key))
    text_num= list(map(P,letter_to_num_encrypt_text,letter_to_num_text_with_key))
    decrypt_text =list(map(search_key,text_num))

    return    ''.join(decrypt_text)
   

def main():
    sc  = scheme()
    tabula = tabula_recta()

    text = read_text().lower()
    text_with_key=list(fill_with_key(text))

    encrypt_text = encrypt(text,sc,text_with_key).upper()
    decrypt_text = decrypt(encrypt_text.lower(),sc,text_with_key)

    print('Encrypt :' +encrypt_text )
    print('Decrypt :' + decrypt_text)
    print('___________________________________________________')
    print_tabula(tabula)
    
main()
