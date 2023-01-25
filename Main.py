import controller
import module
file = 'Data_base.txt'
file1 = 'index.html'
print("\n Текущее представление базы данных")
module.print_db(file)
finish = 1
while finish == 1 :
    controller.a_button(file,file1)
    finish = int(input("\n Для продолжения работы с базой данных нажмите 1, для завершения 2  "))
if finish == 2:
    print ("\n Работа с базой данных завершена")

 