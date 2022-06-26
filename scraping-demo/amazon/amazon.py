# coding: UTF-8
import time
from threading import Thread
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from subprocess import CREATE_NO_WINDOW
from webdriver_manager.chrome import ChromeDriverManager


class Amazon(Thread):

    def __init__(self):
        super().__init__()

    """ Search Word """
    @property
    def search_word(self):
        return self.__search_word

    @search_word.setter
    def search_word(self, value):
        self.__search_word = value

    def run(self):

        # initialize web driver
        self.init_webdriver(production_mode=False) # デバッグモードで実行

        # search process
        self.search()

    def init_webdriver(self, production_mode=True):
        '''
        initialize web driver
        '''

        # web driver config
        options = Options()
        # 最新のWEBドライバのインストール
        service = Service(ChromeDriverManager().install())

        # production config
        if production_mode:
            # 本番モード
            # ブラウザを表示しない
            options.add_argument('--headless')
            # Seleniumログを出さない
            options.add_experimental_option(
                'excludeSwitches', ['enable-automation', 'enable-logging'])
            # Seleniumの画面を出さない
            service.creationflags = CREATE_NO_WINDOW

        # activation of webdriver
        self.__driver = webdriver.Chrome(service=service, options=options)

    def search(self):
        '''
        search process
        '''

        # go to the top page
        self.__driver.get('https://www.amazon.co.jp/')
        time.sleep(5)

        # input of search word
        WebDriverWait(self.__driver, 20).until(EC.presence_of_element_located((By.ID, 'twotabsearchtextbox'))) # IDがtwotabsearchtextboxの要素が見つかるまで最大20秒待機
        self.__driver.find_element_by_id('twotabsearchtextbox').send_keys(self.search_word) # IDがtwotabsearchtextboxの要素にキーボード入力
        time.sleep(5)

        # search process
        WebDriverWait(self.__driver, 20).until(EC.presence_of_element_located((By.ID, 'nav-search-submit-button')))
        self.__driver.find_element_by_id('nav-search-submit-button').click()
        time.sleep(5)


def main():
    amazon = Amazon()
    amazon.search_word = "SEARCH WORD"
    amazon.start()


if __name__ == "__main__":
    main()
