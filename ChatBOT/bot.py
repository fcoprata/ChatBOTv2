from multiprocessing.connection import wait
from time import sleep
from botcity.core import DesktopBot

class Bot(DesktopBot):
    def action(self, execution=None):

        self.execute("C:/Users/fcopr/AppData/Local/WhatsApp/WhatsApp.exe")

        if not self.find( "search", matching=0.97, waiting_time=30000):
            self.not_found("search")
        self.click()

        self.paste("Thiago Viana")

        if not self.find( "user", matching=0.97, waiting_time=30000):
            self.not_found("user")
        self.click()

        if not self.find( "text", matching=0.97, waiting_time=10000):
            self.not_found("text")
        self.click()

        self.paste("teste teste teste")

        if not self.find("send", matching=0.97, waiting_time=10000):
            self.not_found("send")
        self.click()
        sleep(5)
        self.alt_f4()

        self.execute("C:/Users/fcopr/AppData/Local/WhatsApp/WhatsApp.exe")


    def not_found(self, label):
        print(f"Element not found: {label}")


if __name__ == '__main__':
    Bot.main()
