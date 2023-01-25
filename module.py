import data_provider
def print_db(file):
    with open (file,'r') as file_object:
        lines = file_object.readlines()
    for i in lines:
        line = i.split() 
        for a in line:
            print(a.ljust(15), end='  ')
        print()
def change_record(r,file):
    p_book = data_provider.file_to_list(file) 
    if r in range(1,len(p_book)):
        print('Для редактирования выбрана следующая запись базы данных:')
        print(' '.join(map(str,p_book[r])))
        d = int(input("Выберите поле  для редактирования: 1 - Имя, 2 - Фамилия, 3 - Дата рождения, 4 - Место работы, 5 - Телефон №1, 6 - Телефон №2, 7 - Телефон №3"  ))
        print (f"Исходный вид поля: {p_book[r][d]}")
        p_book[r][d] = input("Введите новое представления поля: ")
        new_line = ' '.join(map(str,p_book[r]))
        data_provider.list_to_file(p_book,file) 
        print("Редактирование записи прошло успешно")  
        print()
        print("Измененное представление базы данных:")
        print()
        print_db(file)
 
def delete_record(r,file):
    p_book = data_provider.file_to_list(file) 
    if r in range(1,len(p_book)):
        print('Для удаления выбрана следующая запись базы данных:')
        print(' '.join(map(str,p_book[r])))
        print(p_book[r][0])
        print(len(p_book))
        p_book.pop(r)
        for i in range (r,len(p_book)-1):
            p_book[i][0] = str(i)
        data_provider.list_to_file(p_book,file)
        print("Удаление записи прошло успешно")  
        print()
        print("Измененное представление базы данных:")
        print()
        print_db(file)
 
def find_record(r,file):
    p_book = data_provider.file_to_list(file) 
    res = 0
    print(f'Результат поиска введенного значения {r} в базе данных:')
    with open (file,'r') as file_object:
        lines = file_object.readlines()
        for i in lines:
            if r in i:
                res = 1
                print (f"Найдена строка: {i}")
        if  res == 0:
            print ('Ничего не найдено')
 
 
