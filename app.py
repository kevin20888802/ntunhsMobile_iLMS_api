from datetime import timedelta
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import os

from flask import Flask

app = Flask(__name__)
local_test = False
app.config["SESSION_PERMANENT"] = True
app.config["PERMANENT_SESSION_LIFETIME"] = timedelta(days=7)
app.config["SESSION_TYPE"] = "filesystem"

user_agent = 'Chrome/73.0.3683.86'
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument(f'user-agent={user_agent}')
chrome_options.add_argument("--enable-javascript")
if local_test == False:
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    #app.secret_key = os.environ.get("SECRET_KEY")
    app.secret_key = os.urandom(24)
else:
    app.secret_key = os.urandom(24)
pass

def GetNewWebDriver():
    if local_test == True:
        return webdriver.Chrome(executable_path="D:\ChromeWebDriver\chromedriver.exe", chrome_options=chrome_options)
    else:
        return webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)
    pass
pass

account_driver = {}

from login import login_api
app.register_blueprint(login_api)
from api.ilms_recentwork import ilms_recentwork
app.register_blueprint(ilms_recentwork)

if __name__ == "__main__":
    app.run(host='127.0.0.1',port=5001)
pass