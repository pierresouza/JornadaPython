#Passo a Passo do projeto
#Passo 1: Entrar no sistema da empresa
# https://dlp.hashtagtreinamentos.com/python/intensivao/login
#pip install pyautogui
import pyautogui
import time

pyautogui.PAUSE = 0.5
#pyautogui.hotkey("command" + "space")

# pyautogui.click - > clica em algum lugar
# pyautogui.write - > escreve um texto
# pyautogui.write - > pressionar 1 tecla do teclado

# abrir o navegador
pyautogui.press("win")
pyautogui.write('edge')
pyautogui.press("enter")

#entrar no site
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press("enter")

#dar uma pausa um pouco maior(3 segundos)
time.sleep(3)

#Passo 2: Fazer login
pyautogui.click(x=718, y=388)
pyautogui.write("pierre.s3@hotmail.com")

#escrever sua senha
pyautogui.press("tab")
pyautogui.write("suasenha")

#clicar no botão de logar
pyautogui.click(x=950, y=553)
time.sleep(3)

#Passo 3: Importar a base de dados
#pip install pandas numpy openpyxl
import pandas
tabela = pandas.read_csv("produtos.csv")
print(tabela)

#Passo 4: Cadastrar 1 produto
#para cada linha da minha tabela
for linha in tabela.index:
    #clicar no primeiro campo
    pyautogui.click(x=780, y=269)
    #codigo do produto
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(codigo)
    pyautogui.press("tab")
    #marca
    pyautogui.write(tabela.loc[linha,"marca"])
    pyautogui.press("tab")
    #tipo
    pyautogui.write(tabela.loc[linha,"tipo"])
    pyautogui.press("tab")
    #categoria
    #str() string-> texto
    pyautogui.write(str(tabela.loc[linha,"categoria"]))
    pyautogui.press("tab")
    #preço
    pyautogui.write(str(tabela.loc[linha,"preco_unitario"]))
    pyautogui.press("tab")
    #custo
    pyautogui.write(str(tabela.loc[linha,"custo"]))
    pyautogui.press("tab")
    #obs
    obs = tabela.loc[linha,"obs"]
    if not pandas.isna(obs):
        pyautogui.write()
    pyautogui.press("tab")
    #Enviar
    pyautogui.press("enter")
    pyautogui.scroll(5000)

#Passo 5: Repetir o processo de cadastro até acabar