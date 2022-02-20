from asyncore import read

f1 = open('A_file.txt', 'r')
f2 = open('B_file.txt', 'r')
f3 = open('C_file.txt', 'w+')

q=w=0
for i in f1:
    q+=1
print('q:', q)
for j in f2:
    w+=1
print('w:', w)

f1.seek(0)
f2.seek(0)
def read_line (f):
    rear_f = f.readline()
    return rear_f

if q<=w:
    for i in range(q):
        x= read_line (f1)
        y= read_line (f2)
        f3.write(x+' '+y)
else:
    for i in range(w):
        x= read_line (f1)
        y= read_line (f2)
        f3.write(x+' '+y)

f1.close()
f2.close()
f3.close()

