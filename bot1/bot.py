#1-entrar no nite
#2-fazer o login
#3-cadastrar os produtos
#4-repetir o processo

import pyautogui
import time

pyautogui.PAUSE = 1

pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')

time.sleep(1)

pyautogui.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
pyautogui.press('enter')

time.sleep(1)

pyautogui.click(x=887, y=407)

pyautogui.write('test@gmail.com')
pyautogui.press('tab')
pyautogui.write('senha')
pyautogui.press('enter')

time.sleep(1)

import pandas as pd

tabela = pd.read_csv('produtos.csv')

print(tabela)

for linha in tabela.index:
    pyautogui.click(x=730, y=294)
    codigo = tabela.loc[linha, 'codigo']
    pyautogui.write(str(codigo))
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    obs = tabela.loc[linha, "obs"]
    if not pd.isna(obs):
        pyautogui.write(str(tabela.loc[linha, "obs"]))
    pyautogui.press("tab")
    pyautogui.press("enter")

    pyautogui.scroll(5000)
