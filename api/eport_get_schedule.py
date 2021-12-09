
import time, re
from selenium import webdriver
from flask import Blueprint,request,Response,session
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

eport_get_schedule = Blueprint('eport_get_schedule', __name__)

@eport_get_schedule.route('/api/Schedule', methods=['GET'])
def view():
    try:
        username = session.get('username')
        from app import account_driver
        driver = account_driver[username + "_eportfolio"]
        driver.get("https://system8.ntunhs.edu.tw/myNTUNHS_student/Modules/Main/Index_student.aspx")
        time.sleep(1)
        driver.find_element_by_xpath("//div[@onclick=\"javascript:window.open('https://system8.ntunhs.edu.tw/myNTUNHS_student/Modules/Main/Index_student.aspx?lasturl=OVGfeJ71k85Va+5tUAkRpREuBeu/vj73Xq3Nr9sDoY5sDt38lS4gFsKrX0qYogYUVoxr8f++8G+yMZLEa9IDN5SWFS76zmop52j0OW69Fks=','_self');\"]").click()
        time.sleep(1)
        driver.find_element_by_xpath("//div[@onclick=\"javascript:window.open('https://system8.ntunhs.edu.tw/myNTUNHS_student/Modules/Profile/tab/Profile_tab_02.aspx?lasturl=OVGfeJ71k85Va+5tUAkRpREuBeu/vj73Xq3Nr9sDoY5sDt38lS4gFsKrX0qYogYUVoxr8f++8G+yMZLEa9IDN5SWFS76zmop52j0OW69Fks=','_self');\"]").click()
        time.sleep(1)
        for i in range(5):
            try:
                if driver.find_element_by_link_text(u"課表").is_displayed(): 
                    break
                pass
            except: 
                pass
            pass
            time.sleep(1)
        pass
        driver.find_element_by_link_text(u"課表").click()
        for i in range(10):
            try:
                if is_element_present(By.CSS_SELECTOR, "#FormViewSchedule > tbody > tr:nth-child(8) > td:nth-child(3) > div"): 
                    break
                pass
            except: 
                pass
            pass
            time.sleep(1)
        pass
        print(driver.page_source)
        a_text = driver.find_element_by_css_selector("#FormViewSchedule > tbody > tr:nth-child(8) > td:nth-child(3) > div").text
        return a_text,200
    except Exception as ex:
        print("課表取得失敗" + str(ex))
        return "課表取得失敗",400
    pass
pass

def is_element_present(self, how, what):
    try: self.driver.find_element(by=how, value=what)
    except NoSuchElementException as e: return False
    return True
pass