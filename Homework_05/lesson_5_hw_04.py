from googletrans import Translator

translator = Translator()
dic = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}

f_w = open('write_to_task_04.txt', 'w', encoding='utf-8')
f_w.close()

with open('text_for_task_04.txt', 'r') as f, open('write_to_task_04.txt', 'a', encoding='utf-8') as f_w:
    print(f'\nread file "{f.name}":\n')

    # variant 1 (Translator)
    print(translator.translate(f.readlines(), src='en', dest='ru'), file=f_w)

    # variant 2 (Dictionary)
    for el in f:
        for key in dic:
            if key in el:
                print(el.replace(key, dic.get(key)), end='', file=f_w)
