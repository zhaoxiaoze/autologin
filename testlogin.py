import re
from selenium import webdriver
from PIL import Image, ImageEnhance
import time
import pytesseract
import urllib 
import urllib.request
import ssl


url="https://sso.lnzwfw.gov.cn/ids/admin/abc.code"
num=12

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://sso.lnzwfw.gov.cn/ids/custom/liaoning/login.jsp?coAppName=aWRzY2VudGVy&gb=1&surl=aHR0cDovL2NlbnRlci5sbnp3ZncuZ292LmNuL2FwaS8=&coSessionId=RjIwODA2Q0I4MTE4Mjg3NEVBQjAxQkFENTYwQTI1QTY=&gSessionId=OUFGODU1NkRBMzk1MzRBNTgyODgzRjgyNEVEMDM3NEMtMTkyLjE2OC4yMDEuMjg=")
driver.implicitly_wait(30)

driver.find_element_by_name('loginKey').send_keys('15950494266')
driver.find_element_by_name('password').send_keys('zhaoze13')

driver.find_element_by_name("verifycode").clear()

ssl._create_default_https_context = ssl._create_unverified_context
urllib.request.urlretrieve(url,r'./Image/%d.png'%(int(num)))
#url="https://sso.lnzwfw.gov.cn/ids/custom/liaoning/login.jsp?coAppName=aWRzY2VudGVy&gb=1&surl=aHR0cDovL2NlbnRlci5sbnp3ZncuZ292LmNuL2FwaS8=&coSessionId=RjIwODA2Q0I4MTE4Mjg3NEVBQjAxQkFENTYwQTI1QTY=&gSessionId=OUFGODU1NkRBMzk1MzRBNTgyODgzRjgyNEVEMDM3NEMtMTkyLjE2OC4yMDEuMjg="

'''
driver.set_window_position(200,200)
driver.set_window_size(480,800)

screenImg = "./Image/9.png"
driver.get_screenshot_as_file(screenImg)
location = driver.find_element_by_id('verifyCodeImg').location
size = driver.find_element_by_id('verifyCodeImg').size

print(location)
print('\n')
print(size)
'''
image="./Image/abc.png"
img = Image.open(r'./Image/%d.png'%(num))
img = img.convert('RGBA')  # 转换模式：L | RGB
img = img.convert('L')  # 转换模式：L | RGB
img = ImageEnhance.Contrast(img)  # 增强对比度
img = img.enhance(2.0) 

img.save(image)


code = pytesseract.image_to_string(image)
print(code)
b=''
for i in code.strip():
    pattern = re.compile(r'[0-9]')
    m = pattern.search(i)
    if m!=None:
        b+=i
    #输出去特殊符号以后的验证码
print (b)

driver.find_element_by_name("verifycode").send_key(b)
driver.find_element_by_class_name('submitLoginBtn').click()
time.sleep(5)
