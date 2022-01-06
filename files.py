myfile = open('C:/xampp/htdocs/python/myfile.txt')
print(myfile.read())

with open('C:/xampp/htdocs/python/myfile.txt') as my_new_file:
    contents = my_new_file.read()

with open('C:/xampp/htdocs/python/myfile.txt', mode='r') as myfile:
    content = myfile.read()

a = open('test.txt', mode='w')
a.write('Hello World')
a.close()