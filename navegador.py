from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome()

driver.get('https://proway.com.br/')
sleep(2)
driver.find_element(By.ID, 'termoBuscaCurso').send_keys('python'+Keys.ENTER)
sleep(2)
cursos = driver.find_elements(By.CLASS_NAME, 'nome')
for curso in cursos:
    print(curso.text)
# driver.find_element(By.NAME, 'buscar').click()

input()
driver.quit()
