from selenium import webdriver
import time
import subprocess
import urllib

try:
    import pyautogui
except ImportError:
    subprocess.call(['pip3', 'install', 'pyautogui'])
    import pyautogui

driver = webdriver.Safari()

def login(url, code):
    driver.get(url)
    driver.find_element("xpath", "/html/body/div/div/div[2]/form/input[1]").clear()
    driver.find_element("xpath", "/html/body/div/div/div[2]/form/input[1]").send_keys(code)
    driver.find_element("xpath", "/html/body/div/div/div[2]/form/input[5]").click()
    time.sleep(0.5)
    
    # menu = driver.find_element("xpath", "//*[@id=\"menu\"]/li/a")
    export_button = driver.find_element("xpath", "//*[@id=\"menu\"]/li/ul/li[1]/a")
    
    # Maintenant que le menu est survolé, cliquez sur l'élément du sous-menu
    driver.execute_script("arguments[0].click();", export_button)
    time.sleep(0.5)
    download_button = driver.find_element("xpath", "/html/body/div[2]/form[2]/input[11]").click()
    time.sleep(3)
    pyautogui.press('enter')
    print("Exportation réussie !")

login('https://edt.univ-evry.fr/index.php?disconnect=true', 'M1MIAI')
