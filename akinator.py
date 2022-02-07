
Tom = {'animal', 'cat', 'grey', 'doesnt like mice'}
Simba = {'animal', 'lion', 'ginger', 'son king'}
Belosnezhka = {'person', 'girl', 'dark hair', 'befriend the gnomes'}
Karlson = {'person', 'man', 'ginger', 'friends with a boy'}

# who_iswho = input('your character person (1) or animal (2) ? ')
# if who_iswho == '1':
#     who_iswho2 = input('your character girl (1) or man (2) ? ')
#     if who_iswho2 == '1':
#         print ('your character - Belosnezhka')
#     else:
#         print ('your character - Karlson')
# else:
#     who_iswho3 = input('your character cat (1) or lion (2) ? ')
#     who_iswho4 = input('your character grey (1) or ginger (2) ? ')
#     if who_iswho3 == '1' and who_iswho4 == '1':
#         print ('your character - Tom')
#     else:
#         print ('your character - Simba')

who_iswho = input('your character person (y/n) ? ')
who_iswho2 = input('your character girl (y/n) ? ')
who_iswho3 = input('your character cat (y/n) ? ')
who_iswho4 = input('your character lion (y/n) ? ')
who_iswho5 = input('your character befriend the gnomes (y/n) ? ')
who_iswho6 = input('your character son king (y/n) ? ')
who_iswho7 = input('your character doesnt like mice (y/n) ? ')
who_iswho8 = input('your character friends with a boy (y/n) ? ')


if who_iswho == 'y' and  who_iswho2 == 'y' and who_iswho5 == 'y':
    print ('your character - Belosnezhka')
elif who_iswho == 'y' and  who_iswho2 == 'n' and who_iswho8 == 'y':
    print ('your character - Karlson')
elif who_iswho == 'n' and  who_iswho3 == 'y' and who_iswho7 == 'y':
    print ('your character - Tom')
elif who_iswho == 'n' and  who_iswho3 == 'y' and who_iswho6 == 'y':
    print ('your character - Simba')
else:
    print ('your character is not identified')