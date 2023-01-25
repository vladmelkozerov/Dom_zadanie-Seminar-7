import data_provider 

def create_html(file,file1):
    p_book1 = data_provider.file_to_list(file)
    with open(file1,'w') as file_object:
        file_object.write('<html>\n  <head>Users data base</head>\n  <body>\n')
        for i in p_book1:
            style = 'style="font-size:30px;"'
            html = '<html>\n  <head></head>\n  <body>\n'
            html  = '    <p {}>  {} </p>\n'\
                .format(style, i)
            file_object.writelines(html)
        file_object.writelines('  </body>\n</html>')
    print("Сохранение базы данных в формате HTML прошло успешно, файл index.html")
    
 