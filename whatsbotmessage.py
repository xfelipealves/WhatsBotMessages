# Importar as bibliotecas

from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import os

# Buscar contatos/grupos
def buscar_contato(contato):
    #campo_pesquisa = driver.find_element_by_xpath(
     #   '//div[contains(@title, "Caixa de texto de pesquisa")]')
    #time.sleep(1.5)
    campo_pesquisa.click()
    campo_pesquisa.send_keys(contato)
    #campo_pesquisa.send_keys(Keys.ENTER)

def enviar_mensagem(mensagem):
    #campo_mensagem = driver.find_elements_by_xpath(
     #   '//div[contains(@class, "copyable-text selectable-text")]')
    #time.sleep(1.5)
    campo_mensagem[1].click()
    campo_mensagem[1].send_keys(mensagem)
    campo_mensagem[1].send_keys(Keys.ENTER)

def enviar_midia(midia):
    driver.find_element(By.CSS_SELECTOR, "span[data-icon='clip']").click()
    attach = driver.find_element(By.CSS_SELECTOR, "input[type='file']")
    attach.send_keys(midia)
    time.sleep(2)
    send = driver.find_element(By.XPATH, "//div[contains(@class, '_33pCO')]")
    send.click()

# Definir contatos e grupos e mensagem a ser enviados

cwd = os. getcwd()
contatos = open("contatos.txt", "r")
mensagem = open("mensagem.txt", "r")
mediamp4 = cwd + "\\midia.mp4"
mediajpg = cwd + "\\midia.jpg"

v = os.path.exists('midia.mp4')
img = os.path.exists('midia.jpg')

textoo = mensagem.read()

# Navegar até o whatsapp web 

driver = webdriver.Chrome('./chromedriver')
driver.get('https://web.whatsapp.com/')
time.sleep(20)

campo_pesquisa = driver.find_element(By.XPATH,
        '//div[contains(@title, "Caixa de texto de pesquisa")]')
time.sleep(1.5)

start_time = time.time()

# Créditos

print("\nWhatsBotMessages desenvolvido por: automacao113@gmail.com\nVersão BETA\n")

# First Out
primeirin = contatos.readline()
buscar_contato(primeirin)
campo_mensagem = driver.find_elements(By.XPATH,
        '//div[contains(@class, "copyable-text selectable-text")]')
time.sleep(1.5)
campo_mensagem[1].click()
campo_mensagem[1].send_keys(textoo)
campo_mensagem[1].send_keys(Keys.ENTER)
if (v):
    enviar_midia(mediamp4)
if (img):
    enviar_midia(mediajpg)
#End First Out
i=1
print("Mensagem enviada para '{}' usuarios ".format(i))
for contato in contatos.readlines():
    i = i + 1
    buscar_contato(contato)
    enviar_mensagem(textoo)
    if (v):
        enviar_midia(mediamp4)
    if (img):
        enviar_midia(mediajpg)
    print("Mensagem enviada para '{}' usuarios ".format(i))


print("\nMensagens enviadas com sucesso!")
print("Tempo de execução: " + "--- %s segundos ---" % (time.time() - start_time))
print("\nWhatsBotMessages desenvolvido por: automacao113@gmail.com\nVersão BETA\n")

time.sleep(3)
driver.close()
# Campo de pesquisa 'copyable-text selectable-text'
# Campo de mensagem privada 'copyable-text selectable-text'