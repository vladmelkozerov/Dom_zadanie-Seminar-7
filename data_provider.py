def file_to_list(file):
    p_book = []
  
    with open(file, 'r') as file_object:
        a = True
        while a:
            file_line = file_object.readline()
            if not file_line == None:
                p_book.append(file_line.split())
            if not file_line:
                a = False
    
    return(p_book)
def list_to_file(p_book,file):
    with open(file,'w') as file_object: 
        for i in p_book:
            if not i == []:
                new_line = ' '.join(map(str,i))
                file_object.writelines(f'{new_line}\n')
    
     

 