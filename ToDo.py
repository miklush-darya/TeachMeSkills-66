
# tasks = {1: 'do homework', 2: 'read book'}
done_tasks = {}


f = open('Tasks_Manager.txt', 'r')
q=0
for i in f:
    q+=1

f.seek(0)
def read_str (f):
    rear_f = f.readline()
    rear_word = rear_f.split()
    return rear_word

a=0
tasks = {}
for i in range(q):
    a+=1
    x= read_str (f)
    y = "".join(map(str, x))
    tasks[a] = y
print(tasks)


def repeat_dec(func):
    def vnutr_funk():
        while True:
            func()
            wd = input('repeat action? y/n ')
            if wd == 'y':
                continue
            else:
                break
    return vnutr_funk

# добавить задачу
@repeat_dec
def add_task():
    
    tas_k = input('enter task: ')
    if tasks == {}:        #для записи в пустой файл
        tasks[1]= tas_k
        print (tasks)
    else:
        for i in tasks.keys():
            p = i
            # if tas_k in tasks[i]:
                # print ('задача уже есть')
        tasks[p+1] = tas_k
        print (tasks)

# удалить задачу
@repeat_dec
def del_task():
    print(tasks)
    d = int(input('enter number of task to be deleted:'))
    # for i in tasks:
    #     if d!= i:
    #         print('no task')
    #     else:
    #         tasks.pop(d)
    del tasks[d]
    print(tasks)

# выполненые задачи
@repeat_dec
def done_task():
    print (tasks)
    do = list(map(int, input('enter numbers of tasks that done: ').split()))

    for i in do:
        done_tasks[i] = tasks[i]
        del tasks[i]

    for i in do:
        d_f = f'{done_tasks[i]} - done'
        print(d_f)

    print('done_tasks -', done_tasks)

# изменить задачу
@repeat_dec
def change_task():
    print (tasks)
    c = int(input('enter number of task you want to change:'))
    h = input('make changes: ')
    tasks[c] = h
    print(tasks)

# найти по слову
@repeat_dec
def find_tasks():
    y = input('enter search value: ')
    for i, j in tasks.items():
        if y in j:
            f_z1 = f'{i}. {tasks[i]}'
            print (f_z1)
    for k, v in done_tasks.items():
        if y in v:
            f_z2 = f'{i}. {done_tasks[i]}'
            print (f_z2)

# menu
menu = {1: 'task list', 
        2: 'add task', 
        3: 'change task', 
        4: 'do task',
        5: 'delete task',
        6: 'find task'}

while True:
    print (menu)
    numb_menu = int(input('введите номер действия: '))
    
    if numb_menu != 1 and  numb_menu != 2 and numb_menu != 3 and numb_menu != 4 and numb_menu != 5 and numb_menu != 6:
        print ('action not found')
        numb_menu = int(input('enter action number 1, 2, 3, 4, 5, 6: '))
    
    if numb_menu == 1:
        print(tasks)
    elif numb_menu == 2:
        add_task()
    elif numb_menu == 3:
        change_task()
    elif numb_menu == 4:
        done_task()
        ToDo_done = open('Tasks_Manager_done.txt', 'a')
        for k in done_tasks.values():
            n="".join(map(str, k))
            record_done = f'{n}\n'
            ToDo_done.write(record_done)
        ToDo_done.close()
    elif numb_menu == 5:
        del_task()
    elif numb_menu == 6:
        find_tasks()


    n = input('want to take action : y/n ')
    if n == 'y':
        continue
    else:
        print ('goodbye')
        break

f.close()

ToDo = open('Tasks_Manager.txt', 'w')

for i in tasks.values():
    m="".join(map(str,i))
    record = f'{m}\n'
    ToDo.write(record)

ToDo.close()

