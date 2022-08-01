# add -> commit
# git push -u origin main

from selenium import webdriver
import time
from openpyxl import Workbook
import pandas as pd
from selenium.webdriver.common.keys import Keys

wb = Workbook(write_only=True)
ws = wb.create_sheet()

driver = webdriver.Chrome()
driver.get("https://www.instagram.com/accounts/login/?next=%2Fp%2FCfk_BBKPk1k%2F&source=desktop_nav")
driver.implicitly_wait(3)


# 로그인
driver.find_element_by_css_selector("#loginForm > div > div:nth-child(1) > div > label > input").send_keys("shxorxxs_")
driver.find_element_by_css_selector("#loginForm > div > div:nth-child(2) > div > label > input").send_keys("Wisdom6974!")
driver.find_element_by_css_selector("#loginForm > div > div:nth-child(3) > button > div").click()
time.sleep(1)

# 팝업 종료
driver.find_element_by_css_selector("#react-root > section > main > div > div > div > div > button").click()
time.sleep(1)
#driver.find_element_by_class_name('_a9--._a9_1').click()
#time.sleep(1)

# 댓글 플러스 버튼 누르기
while True:
    try:
        button = driver.find_element_by_class_name('_abl-')
    except:
        pass

    if button is not None:
        try:
            driver.find_element_by_class_name('_abl-').click()
        except:
            break

# 대댓글 버튼 누르기
buttons = driver.find_elements_by_css_selector('li > ul > li > div > button')

for button in buttons:
    button.send_keys(Keys.ENTER)

# 댓글 내용 추출
id_f = []
rp_f = []

ids  = driver.find_elements_by_css_selector('div.C4VMK > h3 > div > span > a')
replies = driver.find_elements_by_css_selector('div.C7I1f > div.C4VMK > span')

for id, reply in zip(ids, replies):
    id_a = id.text.strip()
    id_f.append(id_a)

    rp_a = reply.text.strip()
    rp_f.append(rp_a)


    data = {"아이디": id_f, "코멘트": rp_f}

df = pd.DataFrame(data)
df.to_excel('result.xlsx')

driver.quit()