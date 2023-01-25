import data_provider
import html_creator
import view
import module
def a_button(file,file1):
    value_a = view.get_mode()
    if value_a == 1:
        html_creator.create_html(file,file1)
    elif value_a == 2:
        r = view.Choose_record_to_change()
        module.change_record(r,file)
    elif value_a == 3:
        r = view.Choose_record_to_delete()
        module.delete_record(r,file)
    elif value_a == 4:
        r = view.Record_to_find()
        module.find_record(r,file)
    else:
        print('Данной команды не существует')

