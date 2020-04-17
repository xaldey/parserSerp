from bs4 import BeautifulSoup as bs
import csv
import requests
import datetime
import unittest

from keys import ROOT_URL_YA, HEADERS

date_stamp = datetime.datetime.today().strftime("%Y-%m-%d-%H-%M-%S")
user_inputs = []
search_links = []
recursive_search_array = []


def main():
    serp_string = str(input('Что ищем?: '))
    user_inputs.append(serp_string)
    serp_results = int(input('Сколько результатов найти?: '))
    user_inputs.append(serp_results)
    rec_search = input('Рекурсия? Укажи True or False ')
    user_inputs.append(rec_search)
    search_url: str = ROOT_URL_YA + "text=" + serp_string + "&lr=" + \
                      str(serp_results)
    user_inputs.append(search_url)
    result_type = input('Укажите конечный формат результата: '
                        'json, csv, console ')
    user_inputs.append(result_type)
    filename = str('result--' + date_stamp + '.' + result_type)
    user_inputs.append(filename)
    print('Длина списка - ' + str(len(user_inputs)))
    print(user_inputs)
    print('Рекурсия? ' + str(user_inputs[2]))


def search():
    print('*' * 100)
    print('Первичный поиск запущен!')
    print('*' * 100)
    print('Осуществляем поиск по ссылке: ' + user_inputs[3])
    response = requests.get(user_inputs[3], headers=HEADERS)
    if response.ok:
        soup = bs(response.text, 'html.parser')
        li = soup.find_all('li', class_='serp-item')
        for el in li:
            link = el.find('a').get('href')
            name = el.find('a').get_text()
            result_link = [name, link]
            print(result_link)
            if len(search_links) < user_inputs[1]:
                search_links.append(result_link)
            else:
                break
        print('Длина массива результатов первичного поиска: '
              + str(len(search_links)))
        print('*' * 100)
        print('Первичный поиск завершен!')
        print('*' * 100)
        print(search_links)
    else:
        print('Error! Cant reach search engine!')


def recursive_search():
    for link in search_links:
        look_for = link[1]
        print('Парсим сайт для рекурсивного поиска: '
              + look_for)
        recursive_response = requests.get(look_for, headers=HEADERS)
        if recursive_response.ok:
            recursive_soup = bs(recursive_response.text, 'html.parser')
            for el in recursive_soup.findAll('a'):
                link = str(el.get('href'))
                name = str(el.get_text())
                result_link = [name, link]
                recursive_search_array.append(result_link)
            print(len(recursive_search_array))
        else:
            print('error! cant get response for recursive search')
    print(len(recursive_search_array))


def export_results():
    if user_inputs[4] == 'csv':
        filename = user_inputs[5]
        csv.writer(open(filename, 'w', newline='', encoding='utf-8')) \
            .writerows(search_links)
        csv.writer(open(filename, 'w', newline='', encoding='utf-8')) \
            .writerows(recursive_search_array)
    elif user_inputs[4] == 'json':
        print('Пока не работает :(' + '\n' + (' #' * 50))
    else:
        print('Вывожу результаты в консоль')
        print(search_links)
        print(recursive_search_array)


if __name__ == '__main__':
    main()
    search()
    if user_inputs[2]:
        print('!Начинаем рекурсивный поиск!')
        recursive_search()
    else:
        print('Первичный поиск завершен.')
    export_results()
