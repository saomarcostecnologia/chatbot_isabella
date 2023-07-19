import asyncio
import time
from datetime import date, datetime
from playwright.async_api import Playwright, async_playwright, expect 
import mysql.connector 
#----------------------------------------------------------------------
import acesso as cx #conexao
import status as st #pções de atendimento
import mensagens as msg #mensagens a enviar

async def run(playwright: Playwright) -> None:
    browser = await playwright.chromium.launch(headless=True)
    context = await browser.new_context()
    #Open nem page
    page = await context.new_page()
    #Indo para o whatsapp
    await page.goto("https://web.whatsapp.com/")
    
    #no whatsapp
    await page.locator('').click() #Clica no botao de opções
    await page.locator('').click() #Apenas nao lida

    while page: #Mantendo persistente
        time.sleep(5)
        data_atual = date.today()#Data atual para conseguir fazer id (Tel+data)
        try:
            await page.get_by_test_id("icon-unread-count").nth(0).click()
            time.sleep(3)
            #teste conta comercial ou comercial
            nome_real = "~"
            telefone = await page.locator().all_text_contents()
            print(telefone)
            #--------------------------------------------------------------
            #Ajustando telefone
            tel = telefone[0].replace(" ","") #Retirando espaço
            t = tel.replace("-","") #Retirando o espaço
            #Ajustado
            fone = t.replace("+","") #Retirando o espaço +
            print(fone)
            #Obter ultima mensagem da conversa
            time.sleep(3)
            for i in range(1):
                count = await page.get_by_test_id("msg-container").count()
                a = await page.get_by_test_id("msg-container").all_text_contents()#faz lista com as ultimas 17 mensagens

            texto = a[-1]# Extrai a ultima mensagem da lista
            ultimamensagem = str(texto[0:-10])# elimina os dados de horario (10 caracteres depois do texto)
            print(ultimamensagem)

