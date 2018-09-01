from selenium import webdriver
import time

Driver = webdriver.Firefox()
Driver.get('https://www.twitter.com')

time.sleep(5)

print('\n')

print('1. Default')
print('2. New')

print('\n')

Choice = int (input('Enter the Choice : '))

if Choice is 1:
    Username = 'SeleniumAutoT'
    Password = 'SeleniumAutomation'
    Tweet = 'This is the testing of Selenium Automation using Python in Twitter. Have a Good Day !'

elif Choice is 2:
    Username = input('Enter the Username : ')
    Password = input('Enter the Password : ')
    Tweet = input('Enter the Tweet : ')

else:
    print('Invalid')

print('\n')

input('Start')

time.sleep(5)

LogInElement = Driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[1]/div[2]/div[2]/div/a[2]')
LogInElement.click()

time.sleep(5)

UsernameElement = Driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/div[1]/form/fieldset/div[1]/input')
UsernameElement.clear()
UsernameElement.send_keys(Username)

time.sleep(5)

PasswordElement = Driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/div[1]/form/fieldset/div[2]/input')
PasswordElement.clear()
PasswordElement.send_keys(Password)

time.sleep(5)

LogInNElement = Driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/div[1]/form/div[2]/button')
LogInNElement.click()

time.sleep(5)

TweetBoxElement = Driver.find_element_by_xpath('//*[@id="tweet-box-home-timeline"]')
TweetBoxElement.send_keys(Tweet)

time.sleep(5)

TweetButtonElement = Driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div[2]/div[2]/div/form/div[3]/div[2]/button')
TweetButtonElement.click()





