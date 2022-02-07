#  длина строки

def len_str (x):
    c= 0
    for i in x:
        c+=1
    return(c)


stroka=input('enter string: ')
# n=len(stroka)
# print(n)
print(len_str(stroka))