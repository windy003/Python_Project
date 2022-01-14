from selenium import webdriver  
import time
from bs4 import BeautifulSoup

# 添加屏蔽navigator的代码
options = webdriver.ChromeOptions() 
options.add_argument('--disable-blink-features=AutomationControlled')
driver = webdriver.Chrome(options=options)


# 最大画界面,并访问网站
driver.maximize_window()
driver.get("https://www.taobao.com")



# 点击第一个登陆按钮
login_btn1=driver.find_element_by_class_name("h")
login_btn1.click()


# 常用命令
# print(driver.title)
# print(driver.current_url)

# 进行登陆页操作
driver.find_element_by_name("fm-login-id").send_keys("windy4601")
driver.find_element_by_name("fm-login-password").send_keys("ALLrise258023")

# 点击第二个登陆按钮
login_btn2=driver.find_element_by_xpath("//*[@id='login-form']/div[4]/button")
login_btn2.click()

# 点击我的淘宝页面,等一秒让页面完全加载下来
time.sleep(1)
driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/ul[2]/li[2]/div[1]/a").click()

# 点击已买到的宝贝
driver.find_element_by_xpath("//*[@id='bought']").click()


# ----------------------------------------------------------------
# 到此已经到了我的宝贝页面

print(driver.page_source)
# soup = BeautifulSoup(driver.page_source, "lxml")
# print(soup)

