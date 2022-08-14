import selenium.webdriver
import time
import ddddocr
from PIL import Image

# 打卡接口地址
target_url = "https://mobilehall.jxvtc.edu.cn/ReportServer?formlet=xxkj%2Fmobile%2Fbpa%2Fbpa.frm&op=h5#/form"
# Chrome驱动路径
chrome_diver_path = "/Users/kalimokai/Downloads/chromedriver"
# 账号密码文件目录
account_path = "./account.txt"
# 验证码保存路径
veriy_code_img_path = "./"

def VeriyCode():

    # 截取验证码
    img_code_tag = driver.find_element_by_id("veriyCodeImg")
    img_code_tag.screenshot(veriy_code_img_path + 'VeriyCodeImg.png')

    # 读取验证码
    ocr = ddddocr.DdddOcr()
    with open(veriy_code_img_path + 'VeriyCodeImg.png', 'rb') as f:
        img_bytes = f.read()
    imgCode = ocr.classification(img_bytes)

    return imgCode
    

driver = selenium.webdriver.Chrome(executable_path=chrome_diver_path)

# account.txt是用来存放账号和密码的，一行一个账号和密码，账号和密码用逗号隔开
fs = open(account_path, 'r')
num = fs.readlines()
for i in num:

        time.sleep(1)

        driver.get(target_url)
        time.sleep(3)

        driver.delete_all_cookies()
        driver.get(target_url) # 进入登录界面
        lst = i.strip().split(",")
        time.sleep(3)

        veriyCode = VeriyCode()
        driver.find_element_by_id("username").send_keys(lst[0])
        driver.find_element_by_id("password").send_keys(lst[1])
        driver.find_element_by_id("veriyCode").send_keys(veriyCode)
        driver.find_element_by_tag_name("button").click()
        time.sleep(5)

        driver.find_elements_by_xpath('//*[@id="app"]/div/div/div/div/div/div/div/div[2]/div/div[1]/div/div[1]/div/div[6]/div[1]/div/div/div[2]/div[1]/div/div').click()
        time.sleep(5)

        driver.find_element_by_xpath("//*[@id='app']/div/div/div[2]/div/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[2]/div[1]/div[11]/div").click()
        time.sleep(5)

        driver.find_element_by_xpath("//*[@id='app']/div/div/div/div/div/div/div/div[2]/div/div[1]/div/div[1]/div/div[8]/div[1]/div/div/div[6]/div[1]/div/div/div/div/div[2]/div/div").click()

        driver.find_element_by_xpath("//*[@id='app']/div/div/div/div/div/div/div/div[2]/div/div[1]/div/div[1]/div/div[20]/div[1]/div/div/div[1]/div[1]").click()
        time.sleep(5)

fs.close()
driver.quit()
