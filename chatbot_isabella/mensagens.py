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
    browser = await playwright.chromium.launch(headless=False)
    context = await browser.new_context()
    #Open nem page
    page = await context.new_page()
    #Indo para o whatsapp
    await page.goto("https://web.whatsapp.com/")
    