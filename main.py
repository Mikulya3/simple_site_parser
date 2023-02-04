import requests
from bs4 import BeautifulSoup
from lxml import html
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import datetime
import time
import json

headers = {
    'accept': '*/*',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
}

def get_source_html(url):
    driver = webdriver.Chrome(executable_path='/home/hello/Desktop/py24/django/parsing/chromedriver')
    try:
        driver.get(url=url)
        time.sleep(6)
        while True:
            find_more_element=driver.find_elements_by_class_name('clearfix')
            # if driver.find_elements_by_class_name('date-posted'):
            with open('parsing.html', 'w') as file:
                file.write(driver.page_source)
            break
        else:
            actions = ActionChains(driver)
            actions.move_to_element(find_more_element).perform()
    except Exception as e:
        print(e)
    finally:
        driver.close()
        driver.quit()

def get_items_urls(file_path):
    with open(file_path) as file:
        src = file.read()
    soup=BeautifulSoup(src, 'lxml')
    items_divs = soup.find_all('div', class_='left-col')
    urls = []
    for item in items_divs:
        item_url = item.find("div", class_="image").find('img').get('data-src')
        urls.append(item_url)

    with open('items_urls.txt', 'w') as file:
        for url in urls:
            file.write(f'{url}\n')
    return '[info] collected successfully'
def get_price(file_path):
    with open(file_path) as file:
        src = file.read()
        soup = BeautifulSoup(src, 'lxml')
        items_divs = soup.find_all('div', class_='info-container')
        prices = []
    for item in items_divs:
        item_price = item.find("div", class_="price").text.strip()
        prices.append(item_price)

    with open('the_price.txt', 'w') as file:
        for price in prices:
            file.write(f'{price}\n')
    return '[info] collected successfully'

def get_date(file_path):
    with open(file_path) as file:
        src = file.read()
        soup = BeautifulSoup(src, 'lxml')
        items_divs = soup.find_all('div', class_='info')
        dates = []
    for item in items_divs:
        item_date = item.find("span", class_="date-posted").text.strip()
        dates.append(item_date)
        # date_ = datetime.datetime.strptime(*dates, '%d/%m/%Y')

    with open('the_date.txt', 'w') as file:
        for date in dates:
            file.write(f'{date}\n')
    return '[info] collected successfully'

# def get_data(file_path):
#     with open(file_path) as file:
#         url_list = [url.strip for url in file.readlines()]
#
#     result_list = []
#
#     for url in url_list:
#         response = requests.get(url=url, headers=headers)
#         soup = BeautifulSoup(response.text, 'lxml')
#
#         try:
#             item_price=soup.find('div', class_='price').text.strip()
#         except Exception as e:
#             item_price=None
#
#         date_list=[]
#         try:
#             item_date=soup.find('div', class_='info').find_all('span', class_='date-posted').text.strip()
#             for date in item_date:
#                 date_list.append(date)
#         except Exception as e:
#             date_list=None
#         image_list=[]
#         try:
#             item_image=soup.find('div', class_='left-col').find_all('span', class_='image').find('img').get('data-src').text.strip()
#             for image in item_image:
#                 image_list.append(image)
#         except Exception as e:
#             image_list=None
#
#         result_list.append(
#             {
#                 'item_image': item_image,
#                 'item_price': item_price,
#                 'item_date': item_date,
#             }
#         )
#     with open('parsing/result.json', 'w') as file:
#         json.dump(result_list, file, indent=4, ensure_ascii=False)
#
#     return '[info] data collected successfully'





def main():
    # get_source_html(url='https://www.kijiji.ca/b-apartments-condos/city-of-toronto/c37l1700273')
    # print(get_items_urls(file_path="/home/hello/Desktop/py24/django/parsing/parsing.html"))
    # print(get_price(file_path="/home/hello/Desktop/py24/django/parsing/parsing.html"))
    print(get_date(file_path="/home/hello/Desktop/py24/django/parsing/parsing.html"))

if __name__ == '__main__':
    main()


