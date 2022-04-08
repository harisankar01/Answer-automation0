import time
import unicodedata
import lxml as lxml
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

from selenium.webdriver.common.by import By
# from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import requests
import re
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class automatic:

    def __init__(self):
        print("hello")
    def scrape(self):
        li = list()
        page = requests.get(
            "").text #scrape website
        soup = BeautifulSoup(page, 'lxml')
        buttons = soup.find_all('button', class_="acc active")
        ans = soup.find_all('div', class_="pnl")
        xa = u'\xa0'
        for i in ans :
            wer = i.find('p').text
            x = re.split("\s", wer, 2)
            var = x[2 :3]
            dir = var[0]
            # new_str = unicodedata.normalize("NFKD", var)
            dar = dir.replace('\xa0', '')
            # car=list(dar.split(" "))
            # print(car)
            li.append(dar)
        print(li)
        path = Service("C:\python\drivers\chromedriver.exe")
        opy = webdriver.ChromeOptions()
        drive = webdriver.Chrome(service=path, options=opy)
        drive.delete_all_cookies()
        drive.implicitly_wait(10)
        drive.get(
        )  # website to which answering is performed
        # print(drive.title)
        # print(drive.page_source)
        username = #eneter your username
        password = #eneter your password
        drive.find_element(By.ID, "logonIdentifier").send_keys(username)
        drive.find_element(By.ID, "password").send_keys(password)
        element = WebDriverWait(drive, 10).until(
            EC.presence_of_element_located((By.ID, "next"))
        )
        element.click()
        # drive.find_element(By.ID,"next").click()
        time.sleep(10)
        drive.find_element(By.CSS_SELECTOR, ".dropdown> a[href='#']").click()
        elem = WebDriverWait(drive, 5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "ul.dropdown-menu li:nth-of-type(1)"))
        )
        elem.click()
        time.sleep(5)
        drive.find_element(By.CSS_SELECTOR, ".pull-right > a").click()
        time.sleep(5)  # toggleSubUnitNavBar("subunit_navbar_16")
        # button[@onclick=\"toggleSubUnitNavBar('subunit_navbar_16')\"
        drive.find_element(By.CSS_SELECTOR, "div.unit_heading#unit_heading_16").click()
        ele = WebDriverWait(drive, 5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "ul.subunit_navbar_current li:nth-of-type(1)"))
        )
        ele.click()
        time.sleep(5)  # 8tRhYVO8PffT.1.5912200043560960.0
        # question 1
        # instead of 10 for loop we can add all random option values to a list and iterate over it --|--
        for i in range(0, 4) :
            txt = drive.find_element(By.XPATH, "//label[@for='8tRhYVO8PffT.0.5229585321951232.{}']".format(i)).text
            xe = re.split("\s", txt, 1)
            res = xe[1 : :]
            stri = " ".join(map(str, res))
            if li[0] == stri :
                drive.find_element(By.XPATH, "//input[@id='8tRhYVO8PffT.0.5229585321951232.{}']".format(i)).click()
                break
        # question 2
        time.sleep(1)
        for i in range(0, 4) :
            txt = drive.find_element(By.XPATH, "//label[@for='8tRhYVO8PffT.1.5912200043560960.{}']".format(i)).text
            xe = re.split("\s", txt, 1)
            res = xe[1 : :]
            stri = " ".join(map(str, res))
            print(stri)
            if li[1] == stri :
                drive.find_element(By.XPATH, "//input[@id='8tRhYVO8PffT.1.5912200043560960.{}']".format(i)).click()
                break
        # question3   8tRhYVO8PffT.2.4895177557671936.0   8tRhYVO8PffT.2.4895177557671936.0

        for i in range(0, 4) :
            txt = drive.find_element(By.XPATH, "//label[@for='8tRhYVO8PffT.2.4895177557671936.{}']".format(i)).text
            print(txt)
            xe = re.split("\s", txt, 1)
            res = xe[1 : :]
            stri = " ".join(map(str, res))
            print(stri)
            if li[2] == stri :
                element = WebDriverWait(drive, 1).until(
                    EC.presence_of_element_located((By.XPATH, "//input[@id='8tRhYVO8PffT.2.4895177557671936.{}']".format(i)))
                )
                element.click()
                break

        time.sleep(1)
        # ques4  8tRhYVO8PffT.3.4782147171778560.0
        for i in range(0, 4) :
            txt = drive.find_element(By.XPATH, "//label[@for='8tRhYVO8PffT.3.4782147171778560.{}']".format(i)).text
            xe = re.split("\s", txt, 1)
            res = xe[1 : :]
            stri = " ".join(map(str, res))
            print(stri)
            if li[3] == stri :
                drive.find_element(By.XPATH, "//input[@id='8tRhYVO8PffT.3.4782147171778560.{}']".format(i)).click()
                break
        # ques5  8tRhYVO8PffT.4.5613871506128896.0
        time.sleep(1)

        for i in range(0, 4) :
            txt = drive.find_element(By.XPATH, "//label[@for='8tRhYVO8PffT.4.5613871506128896.{}']".format(i)).text
            xe = re.split("\s", txt, 1)
            res = xe[1 : :]
            stri = " ".join(map(str, res))
            if li[4] == stri :
                drive.find_element(By.XPATH, "//input[@id='8tRhYVO8PffT.4.5613871506128896.{}']".format(i)).click()
                break
        # ques6  8tRhYVO8PffT.5.5556699854274560.0
        time.sleep(1)

        for i in range(0, 4) :
            txt = drive.find_element(By.XPATH, "//label[@for='8tRhYVO8PffT.5.5556699854274560.{}']".format(i)).text
            xe = re.split("\s", txt, 1)
            res = xe[1 : :]
            stri = " ".join(map(str, res))
            if li[5] == stri :
                drive.find_element(By.XPATH, "//input[@id='8tRhYVO8PffT.5.5556699854274560.{}']".format(i)).click()
                break
        # question7   8tRhYVO8PffT.6.6703787312939008.0
        for i in range(0, 4) :
            txt = drive.find_element(By.XPATH, "//label[@for='8tRhYVO8PffT.6.6703787312939008.{}']".format(i)).text
            xe = re.split("\s", txt, 1)
            res = xe[1 : :]
            stri = " ".join(map(str, res))
            if li[6] == stri :
                element = WebDriverWait(drive, 10).until(
                    EC.presence_of_element_located((By.XPATH, "//input[@id='8tRhYVO8PffT.6.6703787312939008.{}']".format(i)))
                )
                element.click()
                break
        # question8  8tRhYVO8PffT.7.6348469198389248.0
        time.sleep(1)

        for i in range(0, 4) :
            txt = drive.find_element(By.XPATH, "//label[@for='8tRhYVO8PffT.7.6348469198389248.{}']".format(i)).text
            xe = re.split("\s", txt, 1)
            res = xe[1 : :]
            stri = " ".join(map(str, res))
            if li[7] == stri :
                drive.find_element(By.XPATH, "//input[@id='8tRhYVO8PffT.7.6348469198389248.{}']".format(i)).click()
                break

        # question9  8tRhYVO8PffT.8.6334318019346432.0
        time.sleep(1)

        for i in range(0, 4) :
            try :
                txt = drive.find_element(By.XPATH, "//label[@for='8tRhYVO8PffT.8.6334318019346432.{}']".format(i)).text
                xe = re.split("\s", txt, 1)
                res = xe[1 : :]
                stri = " ".join(map(str, res))
                if li[8] in stri :
                    drive.find_element(By.XPATH, "//input[@id='8tRhYVO8PffT.8.6334318019346432.{}']".format(i)).click()
                    break
            except NoSuchElementException :
                break
        # question10  8tRhYVO8PffT.9.6295468026888192.0
        time.sleep(1)

        for i in range(0, 4) :
            try :
                txt = drive.find_element(By.XPATH, "//label[@for='8tRhYVO8PffT.9.6295468026888192.{}']".format(i)).text
                xe = re.split("\s", txt, 1)
                res = xe[1 : :]
                stri = " ".join(map(str, res))
                if li[9] == stri :
                    drive.find_element(By.XPATH, "//input[@id='8tRhYVO8PffT.9.6295468026888192.{}']".format(i)).click()
                    break
            except NoSuchElementException :
                break
        time.sleep(3)
        final = WebDriverWait(drive, 10).until(
            EC.presence_of_element_located((By.ID, "checkAnswerButton"))
            )
        final.click()
        time.sleep(15)
        drive.quit()
        # print(first, end="")
        # first.click()

        # a=drive.find_element(By.XPATH, "//input[@id='logonIdentifier']")div[@class='entry']/div[@class='entry-item']/input[@id='logonIdentifier']")
        # print(a)
        # drive.find_element(By.NAME,"Password").send_keys(password)
        # drive.find_element(By.CLASS_NAME,"entry")


        # a_string = soup.find(string="Show Answer")
        # print(a_string)
        # b_st=a_string.find_parents('button')
        # print(b_st,end="\n")

        # wer=ans.find('p')
        # for i in buttons:
        #     print(i,end="\n")
        # print(buttons, end="\n")
        # print(ans,end="\n")
