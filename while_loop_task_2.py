def add_task():
    print('Введите задачу для планирования')
    ad0_list = input()
    list.append(ad0_list)
def print_tasks():
    counter = 0
    for ad1_list in list:
        counter = counter + 1
        print(counter, ad1_list)
def delete_task():
    print('Выберите план')
    ad2_list = int(input())
    list.remove(list[ad2_list - 1])

list=[]
while True:
    print('Выберите действие:')
    print('1.Добавить задачу')
    print('2.Вывести список задач')
    print('3.Удалить задачу')
    print('0.Выйти')
    admin = int(input())
    if admin==1:
        add_task()
    elif admin==2:
        print_tasks()
    elif admin==3:
        print_tasks()
        delete_task()
    else:
        print('Вы вышли')
        break

