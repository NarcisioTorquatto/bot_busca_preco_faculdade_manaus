from botcity.web import WebBot, Browser, By
from botcity.maestro import *
from webdriver_manager.chrome import ChromeDriverManager
from botcity.core import DesktopBot
import time
from rich.console import Console
from rich.panel import Panel
from rich.text import Text

BotMaestroSDK.RAISE_NOT_CONNECTED = False

# Classe MyBotWeb
class MyBotWeb():
    def __init__(self, headless=True):       
        self.webbot = WebBot()
        self.webbot.headless = headless  
        self.webbot.driver_path = ChromeDriverManager().install()
        self.webbot.browser = Browser.CHROME
        self.maestro = BotMaestroSDK.from_sys_args()
        self.deskbot = DesktopBot()
    
    def alerts(self):
        execution = self.maestro.get_execution()
        print('Iniciando Navegação...')
        print(f"Task ID is: {execution.task_id}")
        print(f"Task Parameters are: {execution.parameters}") 
    
    def menu(self):
        console = Console()
        
        console.print(Panel(" MENU PRINCIPAL ", expand=False, style="bold"), justify="left")
        console.print("1 - Buscar melhores preços Graduação")
        console.print("2 - Buscar melhores preços Pós-Graduação")
        console.print("0 - Sair")

        while True:
        
            escolha = console.input("\nEscolha uma opção ➜ ").strip()

            if escolha == "1":
                self.open_site()
            elif escolha == "2":
                console.print("Você escolheu a Opção 2.\n")
            elif escolha == "3":
                console.print("Você escolheu a Opção 3.\n")
            elif escolha == "0":
                console.print("Saindo... Até logo!\n")
                break
            else:
                console.print("Opção inválida! Tente novamente.\n")

    def open_site(self):
        self.webbot.browse("https://querobolsa.com.br/")
        
        while len(self.webbot.find_elements('//*[@id="__nuxt"]/div/div/div[1]/div/div[3]/div/div[2]/div/form/div[1]/div[1]/div[3]/label/div', By.XPATH))<1:
            time.sleep(5)
            print('Aguardando carregamento completo da página...')
        time.sleep(2)
        self.webbot.find_element('//*[@id="__nuxt"]/div/div/div[1]/div/div[3]/div/div[2]/div/form/div[1]/div[1]/div[3]/label/div', By.XPATH).click()
        print('Clique realizado na barra de pesquisa da cidade')
        
        time.sleep(5)  
        self.deskbot.tab(wait=1, presses=1)
        self.webbot.enter()
        cidade = input('Informe em qual cidade deseja fazer a busca: ')
        self.webbot.paste(cidade)
        
    def run(self):
        #coloque a lógica principal aqui:
        try:
            self.alerts()
            self.menu()
        except Exception as ex:
            print(ex)
            self.webbot.save_screenshot('erro.png')  
        finally:
                print('Encerrando Navegador...')
                time.sleep(3)
                self.webbot.stop_browser()

def main():
    bot = MyBotWeb(headless=False)
    bot.run()  # Chama o método run() que irá gerenciar os métodos do bot

if __name__ == '__main__':
    main()
