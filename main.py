in_file = input("Введите название файла с (.txt): ")
txt = open(f'{in_file}','r+')

name = str(txt).replace("<_io.TextIOWrapper ","")
name = str(name).replace("encoding='cp1251'>","")
name = str(name).replace("mode='r+'","")
name = str(name).replace("name=","")
name = str(name).replace("'","")
name = str(name).replace(".txt","")
name = str(name).strip()
name = str(name) + "_output.txt"

lines = txt.readlines()
after = [x for x in lines if len(x) <= 33]
txt.close()

output = open(f'{name}','w+')
output.writelines(after)
output.close()

