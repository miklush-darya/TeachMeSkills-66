
def have_elem(a, str_ing):
        
    if a in str_ing:
        print (a, 'have in ', str_ing)
    else:
        print (a, 'dont have in ', str_ing)


a = input('введите элемент: ')
str_ing = input('введите строку ')

have_elem (a, str_ing)