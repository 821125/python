# 1. Определение количества различных подстрок с использованием хэш-функции.
# Пусть дана строка S длиной N, состоящая только из маленьких латинских букв.
# Требуется найти количество различных подстрок в этой строке.

import hashlib

string = input('Введите строку, состоящую только из маленьких латинских букв: ')

sum_substring = set()

for i in range(len(string)):
    for j in range(len(string), i, -1):
        hash_str = hashlib.sha1(string[i:j].encode('utf-8')).hexdigest()
        sum_substring.add(hash_str)

print(f'{len(sum_substring) -1} различных подстрок в строке {string}\n')

# 2. Закодируйте любую строку из трех слов по алгоритму Хаффмана.

str = 'one two three'
print(str)
print()

import heapq                        # модуль для работы с кучей
from collections import Counter     # словарь со счетчиком
from collections import namedtuple


class Node(namedtuple('Node', ['left', 'right'])):  # класс для ветвей (внутр. узлы)
    
    def walk(self, code, acc):
        self.left.walk(code, acc + '0')   # пойти в левого потомка добавив 0 к префиксу
        self.right.walk(code, acc + '1')  # пойти в правого потомка добавив 1 к префиксу
        
class Leaf(namedtuple('Leaf', ['char'])):  # класс для листьев дерева (без потомков) - знач.
    
    def walk(self, code, acc):
        code[self.char] = acc or '0'  # если строка длинной 1 - acc = ''
        
def huffman_encode(s):
    h = []                                       # инициализируем очередь с приоритетами
    for ch, freq in Counter(s).items():          # поставим очередь через цикл со счетчиком уник. зн.
        h.append((freq, len(h), Leaf(ch)))       # очередь предст. частотой символа, сч. и символом
    heapq.heapify(h)                             # построим очередь с приоритетами    
    count = len(h)                               # инициализируем знач. счетчика длинной очереди
    while len(h) > 1:                            # пока в очереди по крайней мере 2 эл.
        freq1, _count1, left = heapq.heappop(h)  # вытащим эл. с мин. част. - левый узел
        freq2, _count1, right = heapq.heappop(h)  # вытащим след. эл.-т с мин част. - прав. узел
        heapq.heappush(h, (freq1 + freq2, count, Node(left, right)))  # добавим нов. вн. узел
        count += 1                               # инкрименируем значение счетчика
    code = {}                                    # инициализируем словарь кодов символов
    if h:                                        # если строка пустая, обходить нечего
        [(_freq, _count, root)] = h              # в очереди 1 эл.-т, приоритет не важен
        root.walk(code, '')                      # обход дерева от корня и заполнение словаря
    return code                                  # возвращаем словарь символов и кодов
    
def main():
    s = str                                   # получаем строку
    code = huffman_encode(s)                  # кодируем строку
    encoded = ''.join(code[ch] for ch in s)   # отображаем закодированную версию (кажд. символ)
    print(len(code), len(encoded))            # выводим число симв. и длинну кодир. строки
    for ch in sorted(code):                   # обходим символы в словаре в алф. порядке
        print('{}: {}'.format(ch, code[ch]))  # выводим символ и соотв. ему код
    print(encoded)                            # выводим закодированную строку
    

if __name__ == '__main__':
    main()