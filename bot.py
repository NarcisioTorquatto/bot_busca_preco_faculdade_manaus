from botcity.web import WebBot, Browser, By
from botcity.maestro import *
from webdriver_manager.chrome import ChromeDriverManager
from botcity.core import DesktopBot
import time
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
import webbrowser

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
                console.print(Panel(" Escolha uma opção: ", expand=False, style="bold"), justify="left")
                console.print("1 - Ciência da Computação")
                console.print("2 - Análise e desenvolvimento de Sistemas")
                console.print("9 - Voltar")
                console.print("0 - Sair")
                opcao = input('Escolha uma opção: ')
                if opcao == "1":
                    self.open_site()
                    self.webbot.paste('Ciência da Computação')
                    time.sleep(1)
                    self.webbot.enter()
                    time.sleep(1)
                    self.webbot.find_element('//*[@id="__nuxt"]/div/div/div[1]/div/div/div/div[1]/div[2]/div/div/div/div/div[3]/div[1]/div/button/span/span', By.XPATH).click()
                    time.sleep(2)
                    self.webbot.find_element('//*[@id="__nuxt"]/div/div/div[1]/div/div/div/div[1]/div[2]/div/div/div/div/div[3]/div[2]/div/div/div[1]/span[2]/label/span[2]', By.XPATH).click()
                    time.sleep(2)
                    self.webbot.find_element('//*[@id="__nuxt"]/div/div/div[1]/div/div/div/div[1]/div[2]/div/div/div/div/div[3]/div[2]/div/div/div[2]/button[2]/span', By.XPATH).click()
                    time.sleep(2)
                    self.webbot.find_element('//*[@id="__nuxt"]/div/div/div[1]/div/div/div/div[1]/div[3]/div/div/div[1]/div/button/span[2]', By.XPATH).click()
                    time.sleep(2)
                    self.webbot.find_element('//*[@id="__nuxt"]/div/div/div[1]/div/div/div/div[1]/div[3]/div/div/div[2]/div/div/div[1]/label[2]/span', By.XPATH).click()  
                    time.sleep(2)
                    self.webbot.find_element('//*[@id="__nuxt"]/div/div/div[1]/div/div/div/div[1]/div[3]/div/div/div[2]/div/div/div[2]/button/span', By.XPATH).click()  
                    time.sleep(2)
                    valor1 = self.webbot.find_element('//*[@id="__nuxt"]/div/div/div[1]/div/div/div/div[2]/ul/li[1]/div/div[2]/div[1]/div[3]/div/div/div[2]/span[1]', By.XPATH).text
                    valor1 = float(valor1.replace("R$", "").replace(".", "").replace(",", ".").strip())
                    valor2 = self.webbot.find_element('//*[@id="__nuxt"]/div/div/div[1]/div/div/div/div[2]/ul/li[2]/div/div[2]/div[1]/div[3]/div/div/div[2]/span[1]', By.XPATH).text
                    valor2 = float(valor2.replace("R$", "").replace(".", "").replace(",", ".").strip())
                    valor3 = self.webbot.find_element('//*[@id="__nuxt"]/div/div/div[1]/div/div/div/div[2]/ul/li[3]/div/div[2]/div[1]/div[3]/div/div/div/span[1]', By.XPATH).text
                    valor3 = float(valor3.replace("R$", "").replace(".", "").replace(",", ".").strip())
                    valor4 = self.webbot.find_element('//*[@id="__nuxt"]/div/div/div[1]/div/div/div/div[2]/ul/li[4]/div/div[2]/div[1]/div[3]/div/div/div/span[1]', By.XPATH).text
                    valor4 = float(valor4.replace("R$", "").replace(".", "").replace(",", ".").strip())
                    
                    menor_preco = min(valor1,valor2,valor3,valor4)
                    print(f'Valor R$: {menor_preco}')
                    if menor_preco == valor1:
                        url_01 = 'https://checkout.querobolsa.com.br/pre-matricula/cadastro/660982ad-b6b3-4dd0-a091-eab6b1ae2595?referrer=quero-bolsa'
                        webbrowser.open(url_01)
                        
                    elif menor_preco == valor2:
                        url_02 = 'https://checkout.querobolsa.com.br/pre-matricula/cadastro/eaeea880-9071-4720-a3f8-c76c098e6da0?referrer=quero-bolsa'
                        webbrowser.open(url_02)
                        
                    elif menor_preco == valor3:
                        url_3 = 'https://checkout.querobolsa.com.br/pre-matricula/cadastro/299831b4-d996-4509-897b-97ce2250a9b3?referrer=quero-bolsa'
                        webbrowser.open(url_3)
                        
                    elif menor_preco == valor4:
                        url_04 = 'https://checkout.querobolsa.com.br/pre-matricula/cadastro/e0ac645d-7500-4de2-b81b-416aff6217b3?referrer=quero-bolsa'
                        webbrowser.open(url_04)
                    else:
                        print('Erro ao abrir o navegador')
                            
                elif opcao == "2":
                    self.open_site()
                    self.webbot.paste('Análise e desenvolvimento de Sistemas')
                    time.sleep(1)
                    self.webbot.enter()
                    time.sleep(1)
                    self.webbot.find_element('//*[@id="__nuxt"]/div/div/div[1]/div/div/div/div[1]/div[2]/div/div/div/div/div[3]/div[1]/div/button/span/span', By.XPATH).click()
                    time.sleep(2)
                    self.webbot.find_element('//*[@id="__nuxt"]/div/div/div[1]/div/div/div/div[1]/div[2]/div/div/div/div/div[3]/div[2]/div/div/div[1]/span[2]/label/span[2]', By.XPATH).click()
                    time.sleep(2)
                    self.webbot.find_element('//*[@id="__nuxt"]/div/div/div[1]/div/div/div/div[1]/div[2]/div/div/div/div/div[3]/div[2]/div/div/div[2]/button[2]/span', By.XPATH).click()
                    time.sleep(2)
                    self.webbot.find_element('//*[@id="__nuxt"]/div/div/div[1]/div/div/div/div[1]/div[3]/div/div/div[1]/div/button/span[2]', By.XPATH).click()
                    time.sleep(2)
                    self.webbot.find_element('//*[@id="__nuxt"]/div/div/div[1]/div/div/div/div[1]/div[3]/div/div/div[2]/div/div/div[1]/label[2]/span', By.XPATH).click()  
                    time.sleep(2)
                    self.webbot.find_element('//*[@id="__nuxt"]/div/div/div[1]/div/div/div/div[1]/div[3]/div/div/div[2]/div/div/div[2]/button/span', By.XPATH).click()  
                    time.sleep(2)
                    valor1 = self.webbot.find_element('//*[@id="__nuxt"]/div/div/div[1]/div/div/div/div[2]/ul/li[1]/div/div[2]/div[1]/div[3]/div/div/div[2]/span[1]', By.XPATH).text
                    valor1 = float(valor1.replace("R$", "").replace(".", "").replace(",", ".").strip())
                    valor2 = self.webbot.find_element('//*[@id="__nuxt"]/div/div/div[1]/div/div/div/div[2]/ul/li[2]/div/div[2]/div[1]/div[3]/div/div/div/span[1]', By.XPATH).text
                    valor2 = float(valor2.replace("R$", "").replace(".", "").replace(",", ".").strip())
                    valor3 = self.webbot.find_element('//*[@id="__nuxt"]/div/div/div[1]/div/div/div/div[2]/ul/li[4]/div/div[2]/div[1]/div[3]/div/div/div/span[1]', By.XPATH).text
                    valor3 = float(valor3.replace("R$", "").replace(".", "").replace(",", ".").strip())
                    valor4 = self.webbot.find_element('//*[@id="__nuxt"]/div/div/div[1]/div/div/div/div[2]/ul/li[4]/div/div[2]/div[1]/div[3]/div/div/div[2]/span[1]', By.XPATH).text
                    valor4 = float(valor4.replace("R$", "").replace(".", "").replace(",", ".").strip())
                    
                    menor_preco = min(valor1,valor2,valor3,valor4)
                    print(f'Valor R$: {menor_preco}')

                elif opcao == "9":
                    self.menu()
                elif opcao == "0":
                    console.print("Saindo... Até logo!\n")
                    break
                else:
                    console.print("Opção inválida! Tente novamente.\n")
                   
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
        time.sleep(2)
        self.webbot.find_element('//*[@id="__nuxt"]/div/div/div[1]/div/div[3]/div/div[2]/div/form/div[1]/div[1]/div[3]/label/div/div[2]/button/div/span[2]', By.XPATH).click()
        time.sleep(5)
        self.webbot.find_element('//*[@id="__nuxt"]/div/div/div[1]/div/div[3]/div/div[2]/div/form/div[1]/div[2]/button/span', By.XPATH).click()
        self.webbot.find_element('//*[@id="main-filters-content-course"]', By.XPATH).click()
        time.sleep(1)
        
        
        
        # time.sleep(5)  
        # self.deskbot.tab(wait=1, presses=1)
        # self.webbot.enter()
        # cidade = input('Informe em qual cidade deseja fazer a busca: ')
        # self.webbot.paste(cidade)
        
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
