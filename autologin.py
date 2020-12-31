import re
from selenium import webdriver
from PIL import Image, ImageEnhance
import time
import pytesseract
import urllib 
import urllib.request
import ssl


#verifyUrl="https://sso.lnzwfw.gov.cn/ids/admin/abc.code"
#url="https://sso.lnzwfw.gov.cn/ids/custom/liaoning/login.jsp?coAppName=aWRzY2VudGVy&gb=1&surl=aHR0cDovL2NlbnRlci5sbnp3ZncuZ292LmNuL2FwaS8=&coSessionId=RjIwODA2Q0I4MTE4Mjg3NEVBQjAxQkFENTYwQTI1QTY=&gSessionId=OUFGODU1NkRBMzk1MzRBNTgyODgzRjgyNEVEMDM3NEMtMTkyLjE2OC4yMDEuMjg="

def fill_info(username,password):
    driver.find_element_by_name('loginKey').send_keys(username)
    driver.find_element_by_name('password').send_keys(password)

def open_web(url):
    driver.maximize_window()
    driver.get(url)
    driver.implicitly_wait(30)

def get_vercode(verifyUrl,num):
    ssl._create_default_https_context = ssl._create_unverified_context
    urllib.request.urlretrieve(verifyUrl,r'./Image/%d.png'%(num))  

def preimg(image,num):
    img = Image.open(r'./Image/%d.png'%(num))
    img = img.convert('RGBA')  # 转换模式：L | RGB
    img = img.convert('L')  # 转换模式：L | RGB
    img = ImageEnhance.Contrast(img)  # 增强对比度
    img = img.enhance(2.0) 
    img.save(image)

def cv(image,vercode):
    vercode=vercode

def vercode_submit(vercode):
    driver.find_element_by_name("verifycode").send_keys(vercode)
    driver.find_element_by_id('submitLoginBtn').click()
    time.sleep(5)



if __name__ == "__main__":
    driver=webdriver.Chrome()
    verifyUrl="https://sso.lnzwfw.gov.cn/ids/admin/abc.code"
    url="https://sso.lnzwfw.gov.cn/ids/custom/liaoning/login.jsp?coAppName=aWRzY2VudGVy&gb=1&surl=aHR0cDovL2NlbnRlci5sbnp3ZncuZ292LmNuL2FwaS8=&coSessionId=RjIwODA2Q0I4MTE4Mjg3NEVBQjAxQkFENTYwQTI1QTY=&gSessionId=OUFGODU1NkRBMzk1MzRBNTgyODgzRjgyNEVEMDM3NEMtMTkyLjE2OC4yMDEuMjg="
    username='15950494266'
    password='12345678'
    num = 0
    image="./Image/abc.png"
    vercode=''
    open_web(url)
    fill_info(username,password)
    while True:
        num=num+1
        get_vercode(verifyUrl,num)  
        preimg(image,num)  
        cv(image,vercode)
        vercode_submit(vercode)
        if num>2:
            break
