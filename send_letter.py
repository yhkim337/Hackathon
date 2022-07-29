from audioop import add
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait


options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
s = Service("./chromedriver")
driver = webdriver.Chrome(service=s, options=options)
driver.implicitly_wait(2)
# driver.get('https://www.airforce.mil.kr/user/indexSub.action?codyMenuSeq=156893223&siteId=last2&menuUIType=sub')

name = "박채영"
birthYear = "2002"
birthMonth = "11"
birthDay = "29"
birth = "20021129"
address = "낙성대현대홈타운아파트"
address_detail = "인대전"
sendername = "인대전"
relation = "서비스"
title = "뉴스1"
content = "인편 대신 전해드립니다."
password = "1234"

# driver.implicitly_wait(1)
driver.get('https://www.thecamp.or.kr/missSoldier/viewMissSoldierSearch.do')
select = Select(WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#grpCd"))))
select.select_by_value('0000010003')
# driver.find_element(By.CSS_SELECTOR, "#grpCd").click()

# driver.find_element(By.CSS_SELECTOR, "#btnWrite").click()
# driver.find_element(By.CSS_SELECTOR, "#check").click()
# driver.find_element(By.CSS_SELECTOR, "#btnLetter").click()
# driver.find_element(By.CSS_SELECTOR, "#name").send_keys(name)
# driver.find_element(By.CSS_SELECTOR, "#birth").send_keys(birth)
# driver.implicitly_wait(30)
# driver.find_element(By.CSS_SELECTOR, "#recaptcha-anchor > div.recaptcha-checkbox-border").click()
# driver.implicitly_wait(30)
# driver.find_element(By.CSS_SELECTOR, "#btnSearch").click()
            
# driver.find_element(By.CSS_SELECTOR, "#searchName").send_keys(name)
# driver.find_element(By.CSS_SELECTOR, "#birthYear").send_keys(birthYear)
# driver.find_element(By.CSS_SELECTOR, "#birthMonth").send_keys(birthMonth)
# driver.find_element(By.CSS_SELECTOR, "#birthDay").send_keys(birthDay)
# driver.implicitly_wait(1)

# driver.implicitly_wait(10)
# driver.switch_to.window(driver.window_handles[1])

# driver.find_element(By.CSS_SELECTOR, "#emailPic-container > ul > li > input").click()

# driver.switch_to.window(driver.window_handles[0])
# driver.find_element(By.CSS_SELECTOR, "#btnNext").click()

# driver.implicitly_wait(1)

# driver.find_element(By.CSS_SELECTOR, "#emailPic-container > div.UIbtn > span > input[type=button]").click()

# driver.implicitly_wait(3)

# driver.find_element(By.CSS_SELECTOR, "#emailPic-container > form > div.UIview > table > tbody > tr:nth-child(3) > td > div:nth-child(1) > span > input").click()

# driver.implicitly_wait(3)

# driver.switch_to.window(driver.window_handles[1])

# driver.find_element(By.CSS_SELECTOR, "#proceed-button").click()

# driver.find_element(By.CSS_SELECTOR, "#keyword").send_keys(address)

# driver.find_element(By.CSS_SELECTOR, "#searchContentBox > div.search-wrap > fieldset > span > input[type=button]:nth-child(2)").click()

# driver.find_element(By.CSS_SELECTOR, "#roadAddrTd1 > a").click()

# driver.find_element(By.CSS_SELECTOR, "#rtAddrDetail").send_keys(address_detail)

# driver.find_element(By.CSS_SELECTOR, "#resultData > div > a").click()

# driver.switch_to.window(driver.window_handles[0])

# driver.find_element(By.CSS_SELECTOR, "#senderName").send_keys(sendername)

# driver.find_element(By.CSS_SELECTOR, "#relationship").send_keys(relation)

# driver.find_element(By.CSS_SELECTOR, "#title").send_keys(title)

# driver.find_element(By.CSS_SELECTOR, "#contents").send_keys(content)

# driver.find_element(By.CSS_SELECTOR, "#password").send_keys(password)
