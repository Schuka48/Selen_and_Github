from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

link = "http://suninjuly.github.io/explicit_wait2.html"
path = "C:\\Users\\My computer\\Desktop\\SeleniumFolder\\chromedriver.exe"

try:
    browser = webdriver.Chrome(path)
    browser.get(link)

    button = browser.find_element_by_id("book")
    WebDriverWait(browser, 15).until(
        EC.text_to_be_present_in_element((By.ID, 'price'), "$100")
    )
    button.click()

    submit = browser.find_element_by_id("solve")
    browser.execute_script("return arguments[0].scrollIntoView(true);", submit)

    element_x = browser.find_element_by_id("input_value")
    x = element_x.text
    y = calc(x)

    input = browser.find_element_by_name("text")
    input.send_keys(y)
    submit.click()

    alert = browser.switch_to.alert
    alert_text = alert.text
    alert.accept()
    answer = alert_text.split(': ')[1]
    print(answer)

    browser.get("https://stepik.org/lesson/181384/step/8")
    browser.implicitly_wait(5)

    browser.find_element_by_css_selector("a#ember61").click()
    log = browser.find_element_by_css_selector("input[name='login']")
    log.send_keys("your_mail@gmail.com")
    passwd = browser.find_element_by_css_selector("input[name='password']")
    passwd.send_keys("your_password")
    browser.find_element_by_css_selector("button.sign-form__btn.button_with-loader ").click()

    cont = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'a.course-page-header__join-btn.ember-link.ember-view'))
    )
    cont.click()

    container = browser.find_element_by_css_selector("div.quiz__statistics")
    browser.execute_script("return arguments[0].scrollIntoView(true);", container)
    time.sleep(2)

    try:
        submit = browser.find_element_by_css_selector("button.submit-submission")
    except Exception as error:
        print(f'Произошла ошибка, вот ее трэйсбек: {error}')
        submit = 1
    finally:
        print('')

    if submit != 1:
        input_answer = browser.find_element_by_css_selector("textarea[placeholder='Напишите ваш ответ здесь...']")
        input_answer.send_keys(answer)
        submit.click()
    else:
        browser.execute_script("alert('Ох, а надо было раньше думать, задание то уже сделали!');")



except Exception as error:
    print(f'Произошла ошибка, вот ее трэйсбек: {error}')

finally:
    time.sleep(10)
    browser.quit()

