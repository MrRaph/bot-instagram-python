# -*- coding: utf-8 -*-

'''
Created in 12/2019
@Author: Paulo https://github.com/alpdias
'''

# imported libraries
import os
import art
import random
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

def functionComment(mySystem):

    # check the system
    if mySystem == 'Linux': 
        mySystem = 'clear'

    else:
        mySystem = 'cls'

    # input for config bot
    os.system(mySystem) # for linux user 'clear' and for windows use 'cls'
    art.artName(0)
    print('')
    print('\033[0;32mCONFIGURATION\033[m')
    print('')
    way = str(input('Way: ')) # way to geckodriver
    delay = int(input('Delay (just number): ')) # loading delay time

    # input login for bot 
    os.system(mySystem) # for linux user 'clear' and for windows use 'cls'
    art.artName(0)
    print('')
    print('\033[0;32mLOGIN INFORMATION\033[m')
    print('')
    username = str(input('User: ')) # your user
    password = str(input('Password: ')) # your password

    # input info for bot
    os.system(mySystem) # for linux user 'clear' and for windows use 'cls'
    art.artName(0)
    print('')
    print('\033[0;32mBOT INFORMATION\033[m')
    print('')
    hashtag = str(input('Hashtag: ')) # hashtag
    likes = int(input('Amount: ')) # amount of photos to like
    comment = str(input('Comment: ')) # comment in photos
    print('')
    print('Loading...')
    print('')

    # load browser drive in to var and open
    try:
        #driver = webdriver.Firefox(executable_path=f'{way}/geckodriver') # geckodriver path https://github.com/mozilla/geckodriver/releases/tag/v0.26.0
        user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.50 Safari/537.36'
        chrome_options = Options()  
        chrome_options.add_argument("--headless")  
        chrome_options.binary_location = '/usr/bin/google-chrome'
        chrome_options.add_argument(f'user-agent={user_agent}')
        
        driver = webdriver.Chrome(executable_path='/usr/bin/chromedriver',   options=chrome_options)
        print('loaded chrome')
    except:
        try:
            driver = webdriver.Firefox(executable_path=f'{way}\geckodriver')
        except:
            print('\033[0;31mDRIVER ERROR!\033[m Check installed drive or path.')

    # function to access the login page and log in
    def botlogin (user, pwd):
        username = user # your user
        password = pwd # your password

        driver.get('https://www.instagram.com/') # instagram url
        sleep(delay)

        '''
        this page / button was removed by Instagram
        driver.find_element_by_xpath('//a[@href="/accounts/login/?source=auth_switcher"]').click() # click on the 'connect' button element
        '''
        
        userelement = driver.find_element_by_xpath('//input[@name="username"]') # 'username' input element
        userelement.clear()
        userelement.send_keys(username) # user insertion in 'user' element

        pwdelement = driver.find_element_by_xpath('//input[@name="password"]') # 'password 'input element
        pwdelement.clear()
        pwdelement.send_keys(password) # password insertion in 'password' element

        pwdelement.send_keys(Keys.RETURN) # log in to page
        sleep(delay + 2)


    # function hashtag search page
    def findhashtag(hashtag):
        driver.get(f'https://www.instagram.com/explore/tags/{hashtag}/') # instagram tag page url


    # function to type letter by letter
    def typephrase(comment, field):
        for letter in comment: # commentary and lyrics
            field.send_keys(letter) # type the letter in the field
            sleep(0.09) # input time of each letter


    # function to like the photos
    def likecomment(likes=1, comment=''):
        driver.find_element_by_class_name('v1Nh3').click() # click on photo to open and upload
        
        item = 1

        while item <= likes: # loop with how many photos to like
            
            try:
                sleep(delay)
                driver.find_element_by_class_name('fr66n').click() # click the like button
                driver.find_element_by_class_name('Ypffh').click() # click the field to insert comment
                field = driver.find_element_by_class_name('Ypffh')
                field.clear()
                typephrase(comment, field) # insert comment typing each letter
                sleep(delay)

                # the 'publish' button name changes according to your instagram language
                driver.find_element_by_xpath('//button[contains(text(), "Publicar")]').click() # click the post 'comment' button element
                sleep(random.randint(380, 420)) # break time between likes and comment due to instagram policy against bots
                driver.find_element_by_class_name('coreSpriteRightPaginationArrow').click() # click on next photo button
                item = item + 1

            except:
                sleep(60) # if connection errors occur

        print(f'Number of photos liked and commented: \033[0;33m{item - 1}\033[m')


    # running function for login
    try:
        botlogin(username, password)
    except KeyboardInterrupt:
        print('\033[0;33mProgram terminated by the user!\033[m')
    except:
        print('\033[0;31mUNEXPECTED ERROR ON LOGIN\033[m, please try again and verify your connection!')

    # executing function search hastag
    try:
        findhashtag(hashtag)
    except KeyboardInterrupt:
        print('\033[0;33mProgram terminated by the user!\033[m')
    except:
        print('\033[0;31mUNEXPECTED ERROR ON HASHTAG PAGE\033[m, please try again and verify your connection!')

    # executing function to enjoy and comment
    try:
        likecomment(likes, comment)
    except KeyboardInterrupt:
        print('\033[0;33mProgram terminated by the user!\033[m')
    except:
        print('\033[0;31mUNEXPECTED ERROR ON COMMENT\033[m, please try again and verify your connection!')

    print('')
    print('Finish!')
    print('')

    press = input('\033[0;34mpress "enter" to continue\033[m ')
    os.system(mySystem) 

