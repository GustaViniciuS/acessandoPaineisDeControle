from selenium import webdriver # learn more: https://python.org/pypi/selenium
from selenium.webdriver.common.keys import Keys
from gsearch.googlesearch import search
import requests 
from bs4 import BeautifulSoup
import time


#Funcao fazer login, recebe uma pagina, e os inputs dela, onde colocaremos um login e uma senha
#e ele tentara fazer o login
def fazerLogin(p, inputs = []):
  browser = webdriver.Firefox()
  browser.get(p)
  time.sleep(10)
  
  username = browser.find_element_by_name (inputs[0])
  password = browser.find_element_by_name (inputs[1])
  
  username.send_keys ('Admin')
  password.send_keys ('Admin')
  
  login_attempt = browser.find_element_by_name (inputs[2])
  login_attempt.submit()
  
#Funçao para descobrir os inputs para cada pagina, para consiguimos fazer o login com a funçao acima.
def descobrirInputs(p):
  inputs = []
  page = requests.get(p)
  soup = BeautifulSoup(page.content, "html.parser")
  
  print ('DESCOBRINDO INPUTS')
  for x in soup.find('form').find_all('input'):
    inputs.append (x['name'])
    
  return inputs
  
 
#funçao para preencher o nosso vetor com nosso paineis de login  encontrandos em uma busca no Google
def preencherVetor():  
  paginas = ['']
  for resultado in search("inurl admin/login.php", num_results=100):
     paginas.append (resultado[1])
  return paginas


   
paginas = []
paginas = preencherVetor()
print (paginas[32])   
inputs = descobrirInputs(paginas[32])
print (inputs)
##fazerLogin(paginas[1], inputs)



