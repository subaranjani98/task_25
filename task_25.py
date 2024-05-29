from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *


from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


class IMDBNameSearch:
    def result_practise(self):
        try:
            driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
            driver.get('https://www.imdb.com/search/name/')
            driver.maximize_window()
            driver.implicitly_wait(15)

            # use execute-script:-
            driver.execute_script('window.scrollBy(0, 500)')

            # CLICKING EXPAND ALL :-

            expand_all_element = driver.find_element(By.XPATH,
                                                     '/html/body/div[2]/main/div[2]/div['
                                                     '4]/section/section/div/section/section/div[2]/div/section/div['
                                                     '2]/div[1]/div/button/span')

            expand_all_element.click()

            driver.execute_script('window.scrollBy(0, 500)')

            # creating wait object:-
            wait = WebDriverWait(driver, 15, 1, ignored_exceptions=[NoSuchElementException, TimeoutException,
                                                                    ElementClickInterceptedException])
            # FILLING NAME:-
            name_element = wait.until(EC.visibility_of_element_located((By.ID,
                                                                        "text-input__3")))
            name_element.send_keys('Rahman')

            driver.execute_script('window.scrollBy(0, 500)')

            # Birthdate:-
            Birthdate_input = wait.until(EC.visibility_of_element_located((By.XPATH,
                                                                           "/html/body/div[2]/main/div[2]/div["
                                                                           "4]/section/section/div/section/section/div["
                                                                           "2]/div/section/div[2]/div[1]/section/div/div["
                                                                           "2]/div[2]/div/div/div[1]/div["
                                                                           "1]/div/div/div/input")))
            Birthdate_input.send_keys('11-04-1967')

            # To --(Birthdate):-
            to_element = wait.until(EC.visibility_of_element_located((By.XPATH,
                                                                      "/html/body/div[2]/main/div[2]/div["
                                                                      "4]/section/section/div/section/section/div["
                                                                      "2]/div/section/div[2]/div[1]/section/div/div["
                                                                      "2]/div[2]/div/div/div[1]/div[2]/div/div/div/input")))
            to_element.send_keys('11-04-2024')

            # Awards & recognition:-
            oscar_winning = wait.until(EC.element_to_be_clickable((By.XPATH,
                                                                   '/html/body/div[2]/main/div[2]/div['
                                                                   '4]/section/section/div/section/section/div['
                                                                   '2]/div/section/div[2]/div[1]/section/div/div[4]/div['
                                                                   '2]/div/section/button[14]/span')))
            driver.execute_script("arguments[0].click();", oscar_winning)

            driver.execute_script('window.scrollBy(0, 1000)')

            # Gender Identity(Male):
            gender_male = wait.until(EC.element_to_be_clickable((By.XPATH,
                                                                 '/html/body/div[2]/main/div[2]/div['
                                                                 '4]/section/section/div/section/section/div['
                                                                 '2]/div/section/div[2]/div[1]/section/div/div['
                                                                 '7]/div[2]/div/section/button[1]/span')))
            driver.execute_script("arguments[0].click();", gender_male)

            # Click on See Results:-
            see_results = wait.until(EC.element_to_be_clickable((By.XPATH,
                                                                 '/html/body/div[2]/main/div[2]/div['
                                                                 '4]/section/section/div/section/section/div['
                                                                 '2]/div/section/div[1]/button/span')))
            driver.execute_script("arguments[0].click();", see_results)

            print("IMDB Search Name")
            driver.quit()
        except NoSuchElementException:
            print("Error")


imdb_object = IMDBNameSearch()
imdb_object.result_practise()





