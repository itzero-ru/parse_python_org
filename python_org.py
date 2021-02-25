import requests
from requests.exceptions import Timeout, ConnectionError
from bs4 import BeautifulSoup

def find_elements(soup, tag, attribute, value):
    """Поиск элементов в html"""
    result = soup.find_all(tag, {attribute: value})
    return result if result else exit('Тег "{}" c "{}:{}" не найден'.format(tag, attribute, value))

def parse_site(url):

    try:
        response  = requests.get(url, timeout=10)
    except ConnectionError as e:
        print(e)
        exit('Error: ConnectionError')

    html = response.content if response.status_code == 200 else exit('ERROR: response status code = {}'.format(response.status_code))

    soup = BeautifulSoup(html, 'lxml')
    div_events = find_elements(soup, 'div', 'class', 'medium-widget event-widget last')[0]
    h2 = find_elements(div_events, 'h2', 'class', 'widget-title')[0].text
    list_events = find_elements(div_events, 'li', '', '')

    print('\n<< {} >>\n'.format(h2))

    for num, string_line in enumerate(list_events):
        date_text = find_elements(string_line, 'time', '', '')[0].text
        name_post = string_line.find('a').text
        print('{}) {} (beginning: {})'.format(num+1, name_post, date_text))


def main():
    url = 'https://www.python.org'
    parse_site(url)
    print('\n')
    

if __name__ == '__main__':
    main()
