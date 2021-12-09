import time, re
from selenium import webdriver
from flask import Blueprint,request,Response,session

login_api = Blueprint('account_api', __name__)

@login_api.route('/login', methods=['POST','GET'])
def view():
    try:
        # 取得使用者傳入的post 帳號密碼
        if request.method == 'POST':
            username = request.form.get('username', default = '', type = str)
            password = request.form.get('password', default = '', type = str)
        else:
            username = request.args.get('username', default = '', type = str)
            password = request.args.get('password', default = '', type = str)
        pass
        session['username'] = username
        session.modified = True
        print("Login User:"+session['username'] )

        # 開瀏覽器
        from app import account_driver,GetNewWebDriver
        #if not (username+"_eportfolio") in account_driver:
        #    account_driver[username+"_eportfolio"] = GetNewWebDriver()
        pass
        if not (username+"_ilms") in account_driver:
            account_driver[username+"_ilms"] = GetNewWebDriver()
        pass
        #driver = account_driver[username+"_eportfolio"]

        # 登入eportfolio
        #driver.get("https://system8.ntunhs.edu.tw/myNTUNHS_student/Modules/Main/Index_student.aspx?first=true")
        #driver.get("https://system8.ntunhs.edu.tw/myNTUNHS_student/Modules/Main/Index_student.aspx?first=true")
        #driver.find_element_by_id("ctl00_loginModule1_txtLOGINID").click()
        #driver.find_element_by_id("ctl00_loginModule1_txtLOGINID").clear()
        #driver.find_element_by_id("ctl00_loginModule1_txtLOGINID").send_keys(username)
        #driver.find_element_by_id("ctl00_loginModule1_txtLOGINPWD").click()
        #driver.find_element_by_id("ctl00_loginModule1_txtLOGINPWD").clear()
        #driver.find_element_by_id("ctl00_loginModule1_txtLOGINPWD").send_keys(password)
        #driver.find_element_by_id("btnLogin").click()

        # 登入ilms
        driver = account_driver[username+"_ilms"]
        driver.get("https://ilms.ntunhs.edu.tw/")
        print(driver.page_source)
        driver.find_element_by_id("login").click()
        driver.find_element_by_link_text(u"登入").click()
        driver.find_element_by_id("loginAccount").click()
        driver.find_element_by_id("loginAccount").clear()
        driver.find_element_by_id("loginAccount").send_keys(username)
        driver.find_element_by_id("loginPasswd").clear()
        driver.find_element_by_id("loginPasswd").send_keys(password)
        driver.find_element_by_xpath(u"//input[@value='確定']").click()
        
        print("Login Finished : " + username)
        return "Login Finished : " + username,200
    except Exception as ex:
        print("Login Failed : " + username + "," + str(ex))
        return "Login Failed : " + username,400
    pass
pass