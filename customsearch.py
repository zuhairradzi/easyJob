import time,os
from pyvirtualdisplay import Display
from selenium import webdriver

from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup as soup
import requests
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.chrome.options import Options

line = "https://www.jobstreet.com.my/"



chrome_options = Options()
chrome_options.add_argument("--headless")
#driver = webdriver.Chrome("D:\chromedriver.exe")
#,   chrome_options=chrome_options
driver = webdriver.Chrome(executable_path=os.path.abspath("D:\chromedriver.exe"),   chrome_options=chrome_options)

headers = {'User-Agent':'Mozilla/5.0'}
driver.get(line)
try:
    driver.find_element_by_id("header-login-button").click()
    #print("login click")
    time.sleep(2)
except WebDriverException:
    print("login not found")

try:
    driver.find_element_by_id("header-login-button").click()
    #print("login click")
    time.sleep(2)
except WebDriverException:
    print("login not found")

try:
    driver.find_element_by_id("header-login-button").click()
    #print("login click")
    time.sleep(1)
except WebDriverException:
    print("login not found")

try:
    driver.find_element_by_id("login-email").send_keys("mohdzuhair360@gmail.com")
    #print("email entered")
    time.sleep(1)
except NoSuchElementException:
    print("email not found")

try:
    driver.find_element_by_id("login-password").send_keys("SYl@r120")
    #print("pw entered")
    time.sleep(1)
except NoSuchElementException:
    print("pw not found")

try:
    driver.find_element_by_id("login_btn").click()
   # print("login click")
    time.sleep(5)
except NoSuchElementException:
    print("login btn not found")

time.sleep(5)

driver.get("https://www.jobstreet.com.my/en/job-search/advanced.php?")
driver.find_element_by_id("key").click()
driver.find_element_by_id("key").clear()
driver.find_element_by_id("key").send_keys("software development")
driver.find_element_by_id("page").click()
driver.find_element_by_xpath("//div[@id='tbLocOpen']/div").click()
driver.find_element_by_xpath("//div[@id='optLocState']/div/ul/li[4]/label").click()
driver.find_element_by_xpath("//div[@id='optLocState']/div[2]/ul/li[3]/label").click()
driver.find_element_by_xpath("//div[@id='optLocState']/div[2]/ul/li/label").click()
driver.find_element_by_xpath("//div[@id='optLocState']/div[2]/ul/li[7]/label").click()
driver.find_element_by_xpath("//div[@id='optLocState']/div/ul/li[2]/label").click()
driver.find_element_by_xpath("//div[@id='optLocState']/div[2]/ul/li[4]/label").click()
driver.find_element_by_xpath("//div[@id='optLocState']/div[2]/ul/li[2]/label").click()
driver.find_element_by_id("locConBtn").click()
#driver.find_element_by_xpath("//div[@id='tbSpeOpen']/div").click()
#driver.find_element_by_xpath("//div[@id='TB_ajaxContent']/div/div/ul[5]/li[4]/label").click()
#driver.find_element_by_id("speConBtn").click()
driver.find_element_by_id("salary").send_keys("2,500")
driver.find_element_by_id("salary-max").send_keys("4,000")
time.sleep(2)
driver.find_element_by_id("position6").click()
driver.find_element_by_id("position5").click()
driver.find_element_by_id("position4").click()
driver.find_element_by_id("showExtraTog").click()
time.sleep(2)
driver.find_element_by_id("job-type5").click()
time.sleep(2)
driver.find_element_by_id("experience-min").click()
Select(driver.find_element_by_id("experience-min")).select_by_visible_text("0 year")
driver.find_element_by_id("experience-min").click()
driver.find_element_by_id("experience-max").click()
Select(driver.find_element_by_id("experience-max")).select_by_visible_text("3 years")
driver.find_element_by_id("experience-max").click()
driver.find_element_by_class_name("btnQsSearch").click()
#driver.find_element_by_id("job-posted1").click()
#driver.find_element_by_id("job-posted0").click()
#driver.find_element_by_xpath("(//input[@value='Search Jobs'])[2]").click()

time.sleep(2)
positions = driver.find_elements_by_class_name("position-title-link")
time.sleep(2)
companies = driver.find_elements_by_class_name("company-name")
time.sleep(2)
locations = driver.find_elements_by_class_name("job-location")
time.sleep(2)
salary = driver.find_elements_by_css_selector(".under-expected-salary")
time.sleep(2)
respons = driver.find_elements_by_css_selector(".list-unstyled.hidden-xs")
time.sleep(2)
date = driver.find_elements_by_css_selector(".job-date-text.text-muted")
time.sleep(2)

counts = range(40)
for count, position, company, location, pay, respon, dat in zip(counts, positions, companies, locations, salary, respons, date):
    print("No : "+str(count))
    posText = position.text
    print("Job : " + posText)
    comText = company.text
    print("Company : " + comText)
    locText = location.text
    print("Location : " + locText)
    payText = pay.text
    print("Pay : " + payText)
    resText = respon.text
    print("Responsibilities : " + resText)
    datText = dat.text
    print("Date posted : "+datText)
    print()
    print()