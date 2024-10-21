line = [] #Создаем пустой список
with open('text.txt', 'r') as file: #Читаем файл text.txt
    for i in file:  #Цикл для добавления в список
        line.append(line[::-1]) #Добавляем в список
with open('output.txt', 'w') as file: #Записываем в output.txt
    file.write(''.join(line)) #Объединяем список в строку       