import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.by import By
################### CONFIGURANDO O SELENIUM ###################

options = Options()
# options.add_argument('--headless')
options.add_argument('window-size=400,800')

navegador = webdriver.Chrome(options=options)


sleep(1)

navegador.get('https://www.mcdonalds.com.br/cardapio/lancamentos')


################### CONFIGURANDO O SELENIUM ###################

###################  Navegando e clicando nas categorias do cardápio, obs: as categorias ficam num menu lateral esquerdo e não some ################### 

# Verifique se a classe 'mcd-category-menu' existe na página
cardapio = navegador.find_element(By.CLASS_NAME, 'mcd-category-menu')
# Usar um seletor CSS mais específico
categorias = cardapio.find_elements(By.CSS_SELECTOR, '.column.is-narrow-mobile.is-narrow-tablet.is-12-desktop')

ignorar_categoria = ['McLanche Feliz', 'McOferta', 'Méqui Box'] #adicione aqui as categorias que você quer ignorar

# for categoria in categorias:
#     if categoria.text in ignorar_categoria:
#         continue
#     categoria.click()
#     sleep(2)


################### Navegando e clicando nas categorias do cardápio, obs: as categorias ficam num menu lateral esquerdo e não some ###################


################### Após clicar nas categorias, devemos percorrer cada item e clicar nele ################


div_dos_produtos = navegador.find_element(By.CLASS_NAME, 'columns.is-mobile.is-multiline.is-centered.is-gapless')

# Obter a lista de produtos
produto_individual = navegador.find_elements(By.CSS_SELECTOR, '.mcd-category-detail__item')

# Clicando em cada produto
for i in range(len(produto_individual)):
    # Reobter a lista de produtos
    produto_individual = navegador.find_elements(By.CSS_SELECTOR, '.mcd-category-detail__item')
    # Clicar no produto
    produto_individual[i].click()
    sleep(2)

    # Obter o nome do produto
    obter_nome_do_produto = navegador.find_element(By.CSS_SELECTOR, '.mcd-product-detail__summary h1').text
    print(obter_nome_do_produto)  # Imprimir o nome do produto

    # Voltar para a página anterior
    navegador.back()
    sleep(2)

















# Para pegar o html da página, descomente abaixo
# page_content = navegador.page_source
# site = BeautifulSoup(page_content, 'html.parser')
# print(site.prettify())