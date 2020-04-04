import datetime
from keys import ROOT_URL_YA, HEADERS
import requests
from bs4 import BeautifulSoup as bs


date_stamp = datetime.datetime.today().strftime("%Y-%m-%d-%H-%M-%S")
user_inputs = []
search_links = []
recursive_search_array = []


def main():
    # Сначала ищем в Яндекс
    serp_string = str(input('Что ищем?: '))
    user_inputs.append(serp_string)
    serp_results = int(input('Сколько результатов найти?: '))
    user_inputs.append(serp_results)
    rec_search = True
    user_inputs.append(rec_search)
    search_url = ROOT_URL_YA + 'text=' + serp_string + '&lr=' + str(serp_results)
    user_inputs.append(search_url)
    # result_type = input('Укажите конечный формат для результата: json, csv, console ')
    result_type = 'csv'
    user_inputs.append(result_type)
    filename = str('result--' + date_stamp + '.' + result_type)
    print(len(user_inputs))
    print(user_inputs)
    print(user_inputs[2])


def Request():
    print('*' * 100)
    print('Первичный поиск запущен!')
    print('*' * 100)
    print(user_inputs[3])
    response = requests.get(user_inputs[3], headers=HEADERS)
    # response.encoding = 'cp1251'
    if response.ok:
        soup = bs(response.text, 'html.parser')
        li = soup.find_all('li', class_='serp-item')
        for el in li:
            link = el.find('a').get('href')
            name = el.find('a').get_text()
            result_link = [name, link]
            print(result_link)
            search_links.append(result_link)
            # csv.writer(open(result_file_serp, "w", newline='')).writerows(search_links)
        print(len(search_links))
        print('Первичный поиск завершен!')
        print('*' * 100)
        print(search_links)
    else:
        print('Error! Cant reach search engine!')


def recursive_search():
    i = 0
    length = len(search_links)
    while i < length:
        look_for = search_links[0]['i']
        print('Парсим сайт для рекурсивного поиска: ' + look_for)
        recursive_response = requests.get(look_for, headers=HEADERS)
        if recursive_response.ok:
            recursive_soup = bs(recursive_response.text, 'html.parser')
            # a_list = recursive_soup("a")
            # print(a_list)
            for el in recursive_soup.findAll('a'):
                link = str(el.get('href'))
                name = str(el.get_text())
                result_link = [name, link]
                recursive_search_array.append(result_link)
                #print(result_link)
                # csv.writer(open(result_file_recursive, "w", newline='')).writerows(recursive_search_array)
            print(len(recursive_search_array))
        else:
            print('error! cant get response for recursive search')
        i = i + 1
    print(len(recursive_search_array))


def export_results():
    pass


if __name__ == '__main__':
    main()
    Request()
    if user_inputs[2] == True:
        recursive_search()
    else:
        print('Поиск завершен.')
    export_results()



