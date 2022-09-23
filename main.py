from selenium import webdriver
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
import time

PUBMEDSEARCHTERM = "https://pubmed.ncbi.nlm.nih.gov/?term="
DEFAULTFOLDER = "News_Searches"

userTopic = None
userProjectName = None
listOfDBToSearch = ["Pubmed", "Google Scholar"]
userDBList = None
userFromTime = None
userToTime = None
userInput = None

userTopic = input("-->What topic would you like to search?\n")
userProjectName = input("\n-->What would you like to call this project?\n")
print()
print(listOfDBToSearch)
userInput = input("-->Would you like to add any databases to the above list?\nPress 'y' to add a database, press 'n' if you dont want to add any.\n")
while(userInput.lower()=='y'):
    print("Enter the database names seperated by ','")
    userDBList = input().split(",")
    for x in userDBList:
        if x.strip() not in listOfDBToSearch:
            listOfDBToSearch.append(x.strip())
    userInput = input("\nEnter 'y' if you would like to add more or 'n' to stop\n")
print("Updated search List: {}".format(listOfDBToSearch))

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(PUBMEDSEARCHTERM+userTopic.replace(" ", "+"))
time.sleep(2)
button = driver.find_element_by_xpath('//*[@id="save-results-panel-trigger"]')
button.click()
time.sleep(1)
select = Select(driver.find_element_by_xpath('//*[@id="save-action-selection"]'))
select.select_by_visible_text('All results')
time.sleep(1)
select = Select(driver.find_element_by_xpath('//*[@id="save-action-format"]'))
select.select_by_visible_text('PMID')
time.sleep(1)
button = driver.find_element_by_xpath('//*[@id="save-action-panel-form"]/div[3]/button[1]')
button.click()
time.sleep(2)
