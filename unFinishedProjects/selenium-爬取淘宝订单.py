
from selenium import webdriver  

driver=webdriver.Chrome()
driver.get("https://www.taobao.com")



login_btn=driver.find_element_by_class_name("h")
login_btn.click()

# print(driver.title)
# print(driver.current_url)

driver.find_element_by_name("fm-login-id").send_keys("windy4601")
driver.find_element_by_name("fm-login-password").send_keys("ALLrise258023")



# 淘宝卡在要拖动滑块，才能登陆进入，暂时无解





