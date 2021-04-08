import requests
from bs4 import BeautifulSoup

def find(url, teg, class_):
    source = requests.get(url)
    main_text = source.text
    soup = BeautifulSoup(main_text, "html.parser")
    link = soup.find(teg, {'class': class_})
    return link.text
find('https://habr.com/ru/search/?q=python#h', 'a', 'post__title_link')
find('https://career.habr.com/vacancies?type=all', 'div', 'vacancy_banner__title')
find('https://www.ts.kg/show/python_razrabotka_s_nulya_do_professionala', 'div', 'app-show-header')
