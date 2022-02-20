import json

f = open('A_file.txt', 'w')
f.write(input('enter: '))
f.close()

f = open('A_file.txt', 'r')
q=0
for i in f:
    q+=1
print('q:', q)

f.seek(0)
def read_line (f):
    rear_f = f.readline()
    rear_word = rear_f.split()
    n = len(rear_word)
    return n

a=0
dict_for_file = {}
for i in range(q):
    a+=1
    x= read_line (f)
    dict_for_file[a] = x
print(dict_for_file)

f.close()

with open('file_task3.json', 'w') as file_json:
    json.dump(dict_for_file, file_json)