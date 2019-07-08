import json
import os
import xml.etree.ElementTree as ET
from collections import Counter


def get_text_xml(file_name):
    tree = ET.parse(file_name)
    root = tree.getroot()
    for rss in root.iter('description'):
        with open('text_xml.txt', 'a') as document:
            document.write(' ')
            document.write(rss.text)


def get_text_json(file_name):
    with open(file_name, encoding='utf-8-sig') as datafile:
        json_data = json.load(datafile)
        for rss in json_data.values():
            channel = rss['channel']
            for news in channel['items']:
                description = news['description']
                with open('text_json.txt', 'a') as document:
                    document.write(' ')
                    document.write(description)


def get_top_10(file_name):
    long_words = []
    with open(file_name) as text_file:
        for line in text_file:
            words_list = line.split()
            for word in words_list:
                if len(word) <= 6:
                    pass
                else:
                    long_words.append(word)
    top_10 = Counter(long_words).most_common(10)
    for top_word in top_10[0:10]:
        print(f'"{top_word[0]}" встречается {top_word[1]} раз')


def get_json_results():
    get_text_json('newsafr.json')
    get_top_10('text_json.txt')
    os.remove('text_json.txt')


def get_xml_results():
    get_text_xml('newsafr.xml')
    get_top_10('text_xml.txt')
    os.remove('text_xml.txt')


def main():
    print()
    print('Домашнее задание к лекции 3.1 «Работа с разными форматами данных»')
    print()
    print('1 - json')
    print('2 - xml')
    print('q - Конец')
    while True:
        print()
        user_input = input('Выбор: ')
        print()
        if user_input == '1':
            get_json_results()
        elif user_input == '2':
            get_xml_results()
        elif user_input == 'q':
            print('До встречи!')
            break
        else:
            print('Что-то не то :(')


if __name__ == "__main__":
    main()

# print(globals())
