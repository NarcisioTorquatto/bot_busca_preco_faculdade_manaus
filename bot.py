from botcity.web import WebBot, Browser
from botcity.maestro import *
from webdriver_manager.chrome import ChromeDriverManager
import time

BotMaestroSDK.RAISE_NOT_CONNECTED = False

# Classe MyBotWeb
class MyBotWeb():
    def __init__(self, headless=True):       
        self.webbot = WebBot()
        self.webbot.headless = headless  
        self.webbot.driver_path = ChromeDriverManager().install()
        self.webbot.browser = Browser.CHROME
        self.maestro = BotMaestroSDK.from_sys_args()
    
    def alerts(self):
        execution = self.maestro.get_execution()
        print('Iniciando Navegação...')
        print(f"Task ID is: {execution.task_id}")
        print(f"Task Parameters are: {execution.parameters}") 
    
    def open_site(self):
        self.webbot.browse("https://www.botcity.dev")
        
        # while len(bot.find_elements('//*[@id="globalnav-list"]/li[2]/div/div/div[4]/ul/li[1]/a/span[1]', By.XPATH))<1:
        #     time.sleep(5)
        #     print('Aguardando carregamento completo da página...')
        
        # bot.find_element('//*[@id="chapternav"]/div/ul/li[3]/a/figure', By.XPATH).click()
        
        # bot.find_element('//*[@id="chapternav"]/div/ul/li[3]/a/figure', By.XPATH).click().text

    def run(self):
        #coloque a lógica principal aqui:
        try:
            self.alerts()
            self.open_site()
        except Exception as ex:
            print(ex)
            self.webbot.save_screenshot('erro.png')  
        finally:
            if self.webbot.is_browser_open():
                print('Encerrando Navegador...')
                time.sleep(3)
                self.webbot.stop_browser()

def main():
    bot = MyBotWeb(headless=False)
    bot.run()  # Chama o método run() que irá gerenciar os métodos do bot

if __name__ == '__main__':
    main()
