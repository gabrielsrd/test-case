#IMPORTANTE: Esse script requer que tenha o chrome instalado
import time
import os
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

#FUNCTIONS
def select_canal(option,driver):
    comercial_selection = driver.find_element(by=By.NAME, value="prod") #geting the comercial element
    select_comercial = Select(comercial_selection)
    select_comercial.select_by_index(option)
    #   select_comercial.select_by_visible_text('Tortilla en Autoservicios') #chosing option

def select_anio(option,driver):
    anio_selection = driver.find_element(by=By.NAME, value="Anio") #geting the year element
    anio_comercial = Select(anio_selection)
    anio_comercial.select_by_visible_text(str(option))

def select_resumen(option,driver):
    resumen_selection = driver.find_element(by=By.NAME, value="preEdo") #geting the resumen element
    resumen_selection = Select(resumen_selection)
    for a in resumen_selection.options: #parsing through select options
        if(str(option) in str(a.text)):
            element=a.text
    resumen_selection.select_by_visible_text(str(element))

def select_formato(option,driver):
    format_selection = driver.find_element(by=By.NAME, value="Formato") #geting the format element
    format_selection = Select(format_selection)
    for a in format_selection.options: #parsing through select options
        if(str(option) in str(a.text)):
            element=a.text
    format_selection.select_by_visible_text(str(element))

def click_submit(driver):
    submit_button = driver.find_element(by=By.NAME, value="submit")
    submit_button.click()

def click_download(driver):
    driver.implicitly_wait(0.5) #waiting for elements to load
    Button=''
    while not Button:
        try:
            Buttons=driver.find_elements(by=By.CLASS_NAME, value='SelIzq')
            for a in Buttons:
                if a.text == "Descargar Archivo Excel":
                    Button = a
            Button.click()
        except:continue

#MAIN
options = webdriver.ChromeOptions()

prefs = {"download.default_directory" : str(os.getcwd())+"/Downloads"}
options.add_experimental_option("prefs",prefs)
#options.add_argument("--headless") #uncomment for invisble run
driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)

driver.get("http://www.economia-sniim.gob.mx/TortillaAnualPorDia.asp") #opens website
print("\n\nAbrindo o site:", driver.title )
    
driver.implicitly_wait(0.5) #waiting for elements to load

#locating elements
for year in range(2022,2023):
    for canal in range(1,3):
        select_canal(canal, driver)#
        select_anio(year, driver)
        select_resumen("Ambos", driver)
        select_formato("Excel", driver)
        click_submit(driver)
        click_download(driver)
        print("Baixando o arquivo de",year,"canal",canal,"...")

print("Terminei!")

time.sleep(300)#wait for file finish download
driver.quit()



