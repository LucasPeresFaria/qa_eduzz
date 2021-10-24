from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options  
from selenium.webdriver.common.keys import Keys

chrome_options = Options()
chrome_options.add_argument("--headless") 
wait = WebDriverWait(Chrome, 5)

driver = webdriver.Chrome('/Users/Lucas/anaconda3/chromedriver')

url = 'https://www.google.com/'
browser = Chrome() 
browser.get(url)

#buscando as informações na pagina 
browser.find_element_by_name('q').send_keys("Eduzz")
browser.find_element_by_name('q').send_keys(Keys.RETURN)
texto = browser.find_element_by_xpath('//*[@id="rso"]/div[1]/div/div/div/div/div/div/div[1]/a/h3')

print(texto.text)
frase = 'Vem crescer com a gente.'
validação = frase in texto.text
#print(f'{validação}')

if(validação == True):
    print('Possui no texto a frase (Vem crescer com a gente.)')
else:
    print('Não possui no texto a frase (Vem crescer com a gente.)')