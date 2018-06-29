


import time,os
from pyvirtualdisplay import Display
from selenium import webdriver
from bs4 import BeautifulSoup as soup
import requests
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.chrome.options import Options

line = "https://www.jobstreet.com.my/"


chrome_options = Options()
chrome_options.add_argument("--headless")
#driver = webdriver.Chrome("D:\chromedriver.exe")
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

driver.maximize_window()
time.sleep(5)

print()
print()
#print(driver.current_url)
print()
print()
#print(driver.page_source)
print()

positions = driver.find_elements_by_class_name("position-title")
#print(positions)
for position in positions:
    posText = position.text
    #print ("job : "+posText)
print()
print()

companies = driver.find_elements_by_css_selector(".info.no-fig.xn.company-name");
#print(positions)
for company in companies:
    comText = company.text
    #print("Position : "+comText)
print()
print()

locations = driver.find_elements_by_css_selector(".info.no-fig.xn.job-location");
#print(positions)
for location in locations:
    locText = location.text
    #print ("location : "+locText)
print()
print()

salary = driver.find_elements_by_css_selector(".info.no-fig.xn.salary.normal-salary");
#print(positions)
for pay in salary:
    payText = pay.text
    #print ("salary : "+payText)
print()
print()

respons = driver.find_elements_by_css_selector(".info.no-fig.xn.job-detail");
#print(positions)
for respon in respons:
    resText = respon.text
    #print ("responsibilities : "+resText)
print()
print()

date = driver.find_elements_by_css_selector(".job-posted-date");
#print(positions)
for dat in date:
    datText = dat.text
    #print ("date posted : "+datText)
print()
print()


ads = driver.find_elements_by_css_selector(".panel-body.job-ad.card-body");
#print(positions)
for ad in ads:
    adText = ad.text
    #print(adText)
    print()
print()
print()

counts = range(22)
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


















# print("page soup : " + str(page_soup))
#my_line = requests.get(driver.page_source)
#page_soup_line = soup(my_line.text, "html.parser")
#print(page_soup_line)

#try:
 #   text1 = driver.find_element_by_xpath("//*[@id=\"position_title_21479029\"]").text
  #  print(text1)
   # time.sleep(5)
#except NoSuchElementException:
 #   print("job btn not found")


#driver.find_element_by_xpath("//*[@id=\"position_title_21479029\"]").click()
#all_data = page_soup_line.find_all('div', class_='panel panel-card')