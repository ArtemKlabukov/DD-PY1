def get_count_char(str_):
    list_words = str_.split(" ")
    list_words.sort()
    del list_words[0:4]
    new_str = "".join(list_words)
    new_str = new_str.lower()
    list_of_letters: list[str] = []
    for simbol in new_str:
        if simbol.isalpha():
            #print(simbol)
            list_of_letters.append(simbol)
    dict ={}
    for letter in list_of_letters:
        if letter in dict:
            dict[letter]+=1
        else:
            dict[letter]=1
    return(dict)

def get_percents (str_):
    list_words = str_.split(" ")
    list_words.sort()
    del list_words[0:4]
    new_str = "".join(list_words)
    new_str = new_str.lower()
    list_of_letters: list[str] = []
    for simbol in new_str:
        if simbol.isalpha():
            # print(simbol)
            list_of_letters.append(simbol)
    dict = {}
    for letter in list_of_letters:
        if letter in dict:
            dict[letter] += 1
        else:
            dict[letter] = 1
    for letter in dict:
        dict[letter] =float('{:.3f}'.format(dict[letter]/len(list_of_letters)*100))
    return(dict)




# TODO посчитать количество каждой буквы в строке в аргументе
main_str = ("""Данное предложение будет разбиваться на отдельные слова. 
 В качестве разделителя для встроенного метода split будет выбран символ пробела. 
 На выходе мы получим список отдельных слов. 
 Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. 
 Приступим!!!!""")
print(get_count_char(main_str))
print(get_percents(main_str))
# print(get_count_char(main_str))
