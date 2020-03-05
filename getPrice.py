import time
from playsound import playsound
from selenium import webdriver

#change to desired price
alertPrice =  

#change path to wherever you placed chromedriver.exe
chrome_path = r"YOUR/CHROMEDRIVER/PATH/"
driver = webdriver.Chrome(chrome_path)

#change to which ever ticker you are watching
#link must begin with https://www.tradingview.com/symbols/
driver.get("https://www.tradingview.com/symbols/YOUR-TICKER-HERE") 

while True:
    price = driver.find_element_by_xpath("""/html/body/div[2]/div[4]/div/header/div/div[3]/div[1]/div/div/div/div[1]/div[1]""").text
    print(price)
    parsedFloat = float(price)
    time.sleep(0.0625)

    if parsedFloat > alertPrice:
        #change path to wherever you placed your desired alert sound
        playsound(r'/YOUR/SOUND/PATH/')



    
