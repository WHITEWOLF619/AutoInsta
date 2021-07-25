
import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from credentials import username as usr, password as passw


class Bot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        
        profile = webdriver.FirefoxProfile()
       
        self.bot = webdriver.Firefox(profile, executable_path="geckodriver.exe")
        self.bot.set_window_size(1920, 1080)
        with open(r'tags.txt', 'r') as f:
            tagsl = [line.strip() for line in f]
        self.tags = tagsl
        self.urls = []

    def check_exists_by_xpath(driver, xpath):
        try:
            driver.find_element_by_xpath(xpath)
        except NoSuchElementException:
            return True

        return False    

    def exit(self):
        bot = self.bot
        bot.quit()

    def login(self):
        bot = self.bot
        bot.get('https://www.instagram.com/accounts/login/')
        time.sleep(3)
        email = bot.find_element_by_name('username').send_keys(self.username)
        password = bot.find_element_by_name('password').send_keys(self.password)
        time.sleep(1)
        bot.find_element_by_name('password').send_keys(Keys.RETURN)
        time.sleep(7)

        
    def findwhotofollow(self, number_of_followers):
        bot = self.bot
        bot = self.bot
        
        
        accounts_array =[]
        with open("tags.txt", "r") as f:
            line =f.readline()
            while line:
                line =f.readline()
                line = line.strip()
                accounts_array.append(str(line))   
                
            while("" in accounts_array):
                accounts_array.remove("")    
         
        #accounts_array = ['mmashouts','gamespot','gamenewsplusnet','gamestop','gameinformermagazine','markiplier','gamingbible','linustech','rainbow6__','pcmasterrace_official']
        
        print(accounts_array)
        
        followers_arrayxd = []
        
        for accounts in accounts_array:
            
            bot.get('https://instagram.com/' + accounts )
            time.sleep(4)
    
            bot.find_element_by_xpath('//a[@href="/' + accounts + '/followers/"]').click()
    
            time.sleep(1)
    
            popup = bot.find_element_by_class_name('isgrP')
    
            x=0
    
            i = 1
            
            followers_array = []
    
            while len(followers_array) <= number_of_followers:
                bot.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight', popup)
                time.sleep(0.4)
    
                followers = bot.find_elements_by_class_name('FPmhX')
    
                for follower in followers:
                    if follower not in followers_arrayxd:
                        followers_arrayxd.append(follower.text)
                        followers_array.append(follower.text)
                        x=x+1
                    if x==20:
                        break
                i+=1
    
        print(followers_arrayxd)
        print(len(followers_arrayxd))
        self.followers = followers_arrayxd

        
        followers_arrayxd.sort()
        final_array=[]
        for ele in followers_arrayxd:
            if ele not in final_array:
                final_array.append(ele)
                    
        print(final_array)
        print(len(final_array))                
                    
        data = final_array
        random.shuffle(data)

        with open("peopletofollow.txt", "w") as txt_file:
            for line in data:
                txt_file.write("".join(line) + "\n")

    def myfollowerstounfollow(self,number_of_unfollowers):
        bot = self.bot
        bot.get('https://instagram.com/' + self.username )
        time.sleep(2)

        bot.find_element_by_xpath('//a[@href="/' + self.username + '/following/"]').click()

        time.sleep(1)

        popup = bot.find_element_by_class_name('isgrP')

        x=0

        i = 1
        
        unfollowers_array = []
        unfollowers_arrayxd = []
        
        while len(unfollowers_arrayxd) <= number_of_unfollowers:
            bot.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight', popup)
            time.sleep(2)

            unfollowers = bot.find_elements_by_class_name('FPmhX')

            for unfollower in unfollowers:
                if unfollower not in unfollowers_arrayxd:
                    unfollowers_arrayxd.append(unfollower.text)
                    unfollowers_array.append(unfollower.text)
                    x=x+1
                if x==400:
                    break
            i+=1

        print(unfollowers_arrayxd)
        print(len(unfollowers_arrayxd))

    
        unfollowers_arrayxd.sort()
        
        definal_array=[]
        for ele in unfollowers_arrayxd:
            if ele not in definal_array:
                definal_array.append(ele)
                
        print(definal_array)
        print(len(definal_array))                
                
        dedata = definal_array
        random.shuffle(dedata)

        with open("peopletounfollow.txt", "w") as txt_file:
            for line in dedata:
                txt_file.write("".join(line) + "\n")
        
        

        
        






run = Bot(usr, passw)
run.login()
run.myfollowerstounfollow(2000)
run.findwhotofollow(12)




