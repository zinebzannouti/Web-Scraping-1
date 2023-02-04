from selenium import webdriver
import time
from bs4 import BeautifulSoup as soup
from selenium.webdriver.common.by import By
import json
import pandas as pd
df_vin=pd.read_csv('C:/Users/User/Downloads/vin_11.csv')
vin=[]
def web_scrap():
    for i in df_vin['vin_11'][0:20]:
        driver = webdriver.Chrome(executable_path='C:\Drivers\chromedriver_win32\chromedriver.exe')
        driver.get('https://www.autodna.com/')
        search= driver.find_element(By.CLASS_NAME,'vin-input')
        search.send_keys(i+'123456')
        driver.find_element(By.CLASS_NAME,'vin-btn').click()
        time.sleep(10)
        S = soup(driver.page_source, "html.parser")
        t=str(S.title).split(' | ')[1].split(' - ')[0].split(' ')
        d={'vin_11':i,
                'Make':t[0],
                'Model':' '.join(t[1:])}
        print(d)
        vin.append(d)
        driver.quit()
    with open('data-vin.json', 'w') as outfile:
        json.dump(vin, outfile)
    df = pd.read_json('data-vin.json')
    df.to_csv('data-vin.csv')
if __name__ == "__main__":
    web_scrap()
