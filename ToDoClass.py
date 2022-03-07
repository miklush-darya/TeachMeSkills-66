
class TasksManager:
  
    def __init__ (self, tasks, done_tasks):
        self.tasks = tasks
        self.done_tasks = done_tasks

    @property
    def spisok_1(self):
        return self.tasks
    

    # добавить
    def add_task(self):
    # global tasks
        tas_k = input('enter task: ')
        for i in self.tasks.keys():
            p = i
        # if tas_k in tasks[i]:
            # print ('задача уже есть')
        self.tasks[p+1] = tas_k
        print (self.tasks)


    # удалить
    def del_task(self):
        print(self.tasks)
        d = int(input('enter number of task to be deleted:'))
        del self.tasks[d]
        print(self.tasks)

    # изменить задачу
    def change_task(self):
        c = int(input('enter number of task you want to change:'))
        h = input('make changes: ')
        self.tasks[c] = h
        print(self.tasks)


    # найти по слову
    def find_tasks(self):
        y = input('enter search value: ')
        for i, j in self.tasks.items():
            if y in j:
                f_z1 = f'{i}. {self.tasks[i]}'
                print (f_z1)
        for k, v in self.done_tasks.items():
            if y in v:
                f_z2 = f'{i}. {self.done_tasks[i]}'
                print (f_z2)

    # выполненые задачи
    def done_task(self):

        do = list(map(int, input('enter numbers of tasks that done: ').split()))

        for i in do:
            self.done_tasks[i] = self.tasks[i]
            del self.tasks[i]

        for i in do:
            d_f = f'{self.done_tasks[i]} - done'
            print(d_f)

        print('tasks -', self.tasks)
        print('done_tasks -', self.done_tasks)


menu = {1: 'task list', 
        2: 'add task', 
        3: 'change task', 
        4: 'do task',
        5: 'delete task',
        6: 'find task'}

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
tasks_1 = {}
for i in range(q):
    a+=1
    x= read_str (f)
    y = "".join(map(str, x))
    tasks_1[a] = y
print(tasks_1)

done_tasks_1 = {}
D = TasksManager(tasks_1, done_tasks_1)

while True:
    print (menu)
    numb_menu = int(input('введите номер действия: '))
    
    if numb_menu != 1 and  numb_menu != 2 and numb_menu != 3 and numb_menu != 4 and numb_menu != 5 and numb_menu != 6:
        print ('action not found')
        numb_menu = int(input('enter action number 1, 2, 3, 4, 5, 6: '))
    
    if numb_menu == 1:
        print(tasks_1)
    elif numb_menu == 2:
        D.add_task()
    elif numb_menu == 3:
        D.change_task()
    elif numb_menu == 4:
        D.done_task()
        ToDo_done = open('Tasks_Manager_done.txt', 'a')
        for k in done_tasks_1.values():
            n="".join(map(str, k))
            record_done = f'{n}\n'
            ToDo_done.write(record_done)
        ToDo_done.close()

    elif numb_menu == 5:
        D.del_task()
    elif numb_menu == 6:
        D.find_tasks()


    n = input('want to take action : y/n ')
    if n == 'y':
        continue
    else:
        print ('goodbye')
        break