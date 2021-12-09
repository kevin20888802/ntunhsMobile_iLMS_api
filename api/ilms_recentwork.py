from flask import Blueprint,request,Response,session
import json

ilms_recentwork = Blueprint('ilms_recentwork', __name__)

@ilms_recentwork.route('/api/courselist', methods=['GET'])
def courseList():
    try:
        username = session.get('username')
        from app import account_driver
        driver = account_driver[username + "_ilms"]
        driver.get("https://ilms.ntunhs.edu.tw/home.php")
        courseListCount = len(driver.find_elements_by_xpath(".//div[@id='left']/div[2]/div[2]/*"))
        o_data = {}
        for i in range(2,courseListCount):
            tmp = driver.find_element_by_xpath(".//div[@id='left']/div[2]/div[2]/div["+str(i)+"]")
            if tmp.get_attribute("class") != "mnuItem":
                continue
            elif tmp.get_attribute("style") == "margin-top:5px;":
                break
            pass
            course_name = driver.find_element_by_xpath(".//div[@id='left']/div[2]/div[2]/div["+str(i)+"]/a").text
            not_course = ["成績查詢"]
            if course_name not in not_course:
                o_data[str(i)] = course_name
            pass
        pass
        print(o_data)
        return json.dumps(o_data, ensure_ascii=False),200
    except Exception as ex:
        print("作業列表取得失敗" + str(ex))
        return "作業列表取得失敗",400
    pass
pass


@ilms_recentwork.route('/api/getworklist', methods=['GET'])
def getworklist():
    try:
        username = session.get('username')
        from app import account_driver
        driver = account_driver[username + "_ilms"]
        driver.get("https://ilms.ntunhs.edu.tw/home.php")
        o_data = {}
        course_name = request.args.get('course_name', default = '', type = str)
        driver.find_element_by_link_text(course_name).click()
        driver.find_element_by_link_text(u"作業").click()
        o_data[course_name] = {}
        workcount = len(driver.find_elements_by_xpath("//div[@id='main']/div[2]/table/tbody/tr"))
        for j in range(2,workcount + 1):
            driver.find_element_by_xpath("//div[@id='main']/div[2]/table/tbody/tr["+str(j)+"]/td[2]/a").click()
            driver.find_element_by_link_text(u"作業資訊").click()
            work_data = {}
            work_data["title"] = driver.find_element_by_xpath("//div[@id='main']/div/span").text
            work_data["description"] = ""
            try:
                work_data["description"] += driver.find_element_by_xpath("//div[@id='main']/div[2]/div/table/tbody/tr[8]/td[2]/div").text
            except:
                pass
            for t in driver.find_elements_by_xpath("//div[@id='main']/div[2]/div/table/tbody/tr[8]/td[2]/div/*"):
                try:
                    work_data["description"] += t.text
                except:
                    pass
            pass
            work_data["term"] = driver.find_element_by_xpath("//div[@id='main']/div[2]/div/table/tbody/tr[6]/td[2]/div").text
            work_data["type"] = driver.find_element_by_xpath("//div[@id='main']/div[2]/div/table/tbody/tr[4]/td[2]").text
            work_data["percent"] = driver.find_element_by_xpath("//div[@id='main']/div[2]/div/table/tbody/tr[5]/td[2]").text
            work_data["link"] = driver.current_url
            o_data[course_name][work_data["title"]] = work_data
            driver.find_element_by_link_text(u"作業").click()
        pass
        driver.get("https://ilms.ntunhs.edu.tw/home.php")
        print(o_data)
        return json.dumps(o_data, ensure_ascii=False),200
    except Exception as ex:
        print("作業列表取得失敗" + str(ex))
        return "作業列表取得失敗",400
    pass
pass

@ilms_recentwork.route('/api/allworks', methods=['GET'])
def view():
    try:
        username = session.get('username')
        from app import account_driver
        driver = account_driver[username + "_ilms"]
        driver.get("https://ilms.ntunhs.edu.tw/home.php")
        courseListCount = len(driver.find_elements_by_xpath(".//div[@id='left']/div[2]/div[2]/*"))
        o_data = {}
        for i in range(2,courseListCount):
            tmp = driver.find_element_by_xpath(".//div[@id='left']/div[2]/div[2]/div["+str(i)+"]")
            if tmp.get_attribute("class") != "mnuItem":
                continue
            elif tmp.get_attribute("style") == "margin-top:5px;":
                break
            pass
            course_name = driver.find_element_by_xpath(".//div[@id='left']/div[2]/div[2]/div["+str(i)+"]/a").text
            driver.find_element_by_xpath(".//div[@id='left']/div[2]/div[2]/div["+str(i)+"]/a").click()
            driver.find_element_by_link_text(u"作業").click()
            o_data[course_name] = {}
            workcount = len(driver.find_elements_by_xpath("//div[@id='main']/div[2]/table/tbody/tr"))
            for j in range(2,workcount):
                driver.find_element_by_xpath("//div[@id='main']/div[2]/table/tbody/tr["+str(j)+"]/td[2]/a").click()
                driver.find_element_by_link_text(u"作業資訊").click()
                work_data = {}
                work_data["title"] = driver.find_element_by_xpath("//div[@id='main']/div/span").text
                work_data["description"] = ""
                try:
                    work_data["description"] += driver.find_element_by_xpath("//div[@id='main']/div[2]/div/table/tbody/tr[8]/td[2]/div").text
                except:
                    pass
                for t in driver.find_elements_by_xpath("//div[@id='main']/div[2]/div/table/tbody/tr[8]/td[2]/div/*"):
                    try:
                        work_data["description"] += t.text
                    except:
                        pass
                pass
                work_data["term"] = driver.find_element_by_xpath("//div[@id='main']/div[2]/div/table/tbody/tr[6]/td[2]/div").text
                work_data["type"] = driver.find_element_by_xpath("//div[@id='main']/div[2]/div/table/tbody/tr[4]/td[2]").text
                work_data["percent"] = driver.find_element_by_xpath("//div[@id='main']/div[2]/div/table/tbody/tr[5]/td[2]").text
                work_data["link"] = driver.current_url
                o_data[course_name][work_data["title"]] = work_data
                driver.find_element_by_link_text(u"作業").click()
            pass
            driver.get("https://ilms.ntunhs.edu.tw/home.php")
        pass
        print(o_data)
        return json.dumps(o_data, ensure_ascii=False),200
    except Exception as ex:
        print("作業取得失敗" + str(ex))
        return "作業取得失敗",400
    pass
pass