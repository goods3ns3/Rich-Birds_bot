from selenium import webdriver
import time
import re
import pickle
from data import login, password

URL_SIGNIN = 'https://rich-birds.com/signin'

options = webdriver.ChromeOptions()
options.add_argument(
    'user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \
    (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36')
options.add_argument(
    'accept=accept: text/html,application/xhtml+xml,application/\
    xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9')
options.add_argument('--disable-blink-features=AutomationControlled')
# options.add_argument('--headless')
# options.headless = True
driver = webdriver.Chrome(
    executable_path=r"C:\Users\Workspace\Desktop\prog_learning\Home_Projects\rich-birds\chromedriver\chromedriver.exe",
    options=options
)

try:
    # Вход на сайт
    driver.get(url=URL_SIGNIN)
    # driver.save_screenshot('insta.png')
    # time.sleep(5)
    driver.implicitly_wait(10)
    # Логин
    email_input = driver.find_element_by_name('log_email')
    email_input.clear()
    email_input.send_keys(login)
    driver.implicitly_wait(10)
    password_input = driver.find_element_by_name('pass')
    password_input.clear()
    password_input.send_keys(password)
    time.sleep(15)
    login_button = driver.find_element_by_tag_name('button').click()
    driver.implicitly_wait(10)
    # Сворачивание окна
    # driver.minimize_window()
    # Дамп куки
    # pickle.dump(driver.get_cookies(), open('rich_bird_cookies', 'wb'))
    # Чтение куки
    # for cookie in pickle.load(open('rich_bird_cookies', 'rb')):
    # 	driver.add_cookie(cookie)
    # time.sleep(5)
    # driver.refresh()
    # driver.implicitly_wait(10)
    # Переход на склад
    sklad = driver.find_element_by_link_text('Склад яиц').click()
    time.sleep(5)
    # Сбор
    sobrat = driver.find_element_by_name('sbor').click()
    time.sleep(5)
    # # Продажа
    prodat = driver.find_element_by_link_text('Продажа яиц').click()
    time.sleep(5)
    prodat_vse = driver.find_element_by_name('sell').click()
    time.sleep(5)
    # Обмен
    print('обмен начался')
    obmen = driver.find_element_by_xpath('/html/body/div[2]/div[4]/div[1]/div/div/div[5]/div[5]').click()
    time.sleep(5)
    amo = driver.find_element_by_xpath('/html/body/div[2]/div[4]/div[1]/div/div/div[2]/div[4]')
    dig = int(re.findall(r"\d+", amo.text)[0]) - 1
    swap = driver.find_element_by_id('sum')
    swap.clear()
    swap.send_keys(dig)
    time.sleep(5)
    swap_button = driver.find_element_by_class_name('btn_kup').click()
    time.sleep(5)
    print('обмен закончился')
    # Покупка птиц
    buy = driver.find_element_by_link_text('Купить птиц').click()
    time.sleep(5)
    print('переход на покупку птиц')
    buy_birds = driver.find_element_by_xpath('/html/body/div[2]/div[4]/div[2]/div[2]/div[6]/form/div[2]/input[2]')
    buy_birds.clear()
    buy_birds.send_keys('100000')
    driver.implicitly_wait(10)

    buy_button = driver.find_element_by_xpath(
        '/html/body/div[2]/div[4]/div[2]/div[2]/div[6]/form/div[2]/input[3]').click()
    driver.implicitly_wait(10)

    amount = driver.find_element_by_xpath('/html/body/div[2]/div[4]/div[1]/div/div/div[2]/div[2]')
    digits = int(re.findall(r"\d+", amount.text)[0])
    number_of_times = digits // 500000 // 100000

    print(number_of_times)

    for i in range(number_of_times):
        driver.refresh()
        driver.implicitly_wait(10)
        print(str(i + 1) + ' of ' + str(number_of_times))

    print('Done!!!')

except Exception as e:
    print(e)
finally:
    driver.close()
    driver.quit()
