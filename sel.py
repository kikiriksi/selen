from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

lst = []
with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/infiniti_scroll_3/')
    for i in range(1, 6):
        scroll_cont = browser.find_element(By.XPATH, f'//*[@id="scroll-container_{i}"]/div')
        for j in range(10):
            ActionChains(browser).move_to_element(scroll_cont).scroll_by_amount(0, 1000).perform()
        span = sum([float(i.text) for i in
                    browser.find_element(By.ID, f'scroll-wrapper_{i}').find_elements(By.TAG_NAME, 'span')])
        lst.append(span)
print(sum(lst))
