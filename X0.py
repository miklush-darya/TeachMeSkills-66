
game = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
n = len(game)

def table ():
    for i in game:
        print(i)

table ()

while True:
    order = int(input('введите № места на которое поставить Х '))

    for i in range(n):
        for j in range(n):
            if game[i][j] == order:
                game[i][j] = 'x'
    table ()

    order = int(input('введите № места на которое поставить 0 '))
    for i in range(n):
        for j in range(n):
            if game[i][j] == order:
                game[i][j] = '0'
    table ()

    def check():
        x = "выиграли Х"
        y = "выиграли 0"
        if game [0][0] == 'X' and game [0][1] == 'X' and game [0][2] == 'X':
            return x
        elif game [1][0] == 'X' and game [1][1] == 'X' and game [1][2] == 'X':
            return x
        elif game [2][0] == 'X' and game [2][1] == 'X' and game [2][2] == 'X':
            return x
        elif game [0][0] == 'X' and game [1][0] == 'X' and game [2][0] == 'X':
            return x
        elif game [0][1] == 'X' and game [1][1] == 'X' and game [2][1] == 'X':
            return x
        elif game [0][2] == 'X' and game [1][2] == 'X' and game [2][2] == 'X':
            return x
        elif game [0][0] == 'X' and game [1][1] == 'X' and game [2][2] == 'X':
            return x
        elif game [0][2] == 'X' and game [1][1] == 'X' and game [2][0] == 'X':
            return x
        elif game [0][0] == '0' and game [0][1] == '0' and game [0][2] == '0':
            return y
        elif game [1][0] == '0' and game [1][1] == '0' and game [1][2] == '0':
            return y
        elif game [2][0] == '0' and game [2][1] == '0' and game [2][2] == '0':
            return y
        elif game [0][0] == '0' and game [1][0] == '0' and game [2][0] == '0':
            return y
        elif game [0][1] == '0' and game [1][1] == '0' and game [2][1] == '0':
            return y
        elif game [0][2] == '0' and game [1][2] == '0' and game [2][2] == '0':
            return y
        elif game [0][0] == '0' and game [1][1] == '0' and game [2][2] == '0':
            return y
        elif game [0][2] == '0' and game [1][1] == '0' and game [2][0] == '0':
            return y
    
    print(check())
    if check() == True:
        break
    else:
        continue
    
