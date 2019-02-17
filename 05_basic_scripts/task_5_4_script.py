#!/usr/bin/env python3

num_list = [10, 2, 30, 100, 10, 50, 11, 30, 15, 7]
word_list = ['python', 'ruby', 'perl', 'ruby', 'perl', 'python', 'ruby', 'perl']

num_list.reverse()
word_list.reverse()
#count_elements = 

digit = input('Введите число из списка: ')
print(9-num_list.index(int(digit)))

word = input('Введите слово из списка: ')
print(7-word_list.index(word))
