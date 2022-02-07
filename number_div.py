

def num_div(x):

    s = []
    for i in range(1, x+1):
        
        if x%i == 0:
            s.append(i)
            #print (i)
    print ('делители числа', x, s)


x = int(input())
num_div(x)