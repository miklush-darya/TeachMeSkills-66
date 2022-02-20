import string
import os

os.mkdir('Alphabet_file2')
os.chdir('Alphabet_file2')

def Alphabet_file():
    Alpha = string.ascii_lowercase
    for i in Alpha:
        name=f'{i}.txt'
        n=open(name, 'w')
        n.write(i)
        n.close()

Alphabet_file()

# def Alphabet_file_str():
#     Alpha = string.ascii_lowercase
#     for i in Alpha:
#         j = i.swapcase()
#         name=f'{j}{i}.txt'
#         n=open(name, 'w')
#         n.write(j+i)
#         n.close()

# Alphabet_file_str()

os.chdir("..")