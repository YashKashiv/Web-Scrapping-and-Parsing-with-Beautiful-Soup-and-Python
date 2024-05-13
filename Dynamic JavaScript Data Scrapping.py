import sys
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWebEngineWidgets import QWebEngineView
from bs4 import BeautifulSoup

class Client(QWebEngineView):
    def __init__(self, url):
        self.app = QApplication(sys.argv)
        super().__init__()
        self.loadFinished.connect(self.on_page_load)
        self.load(QUrl(url))

    def on_page_load(self):
        self.page().toHtml(self.parse_content)

    def parse_content(self, html):
        soup = BeautifulSoup(html, "html.parser")
        js_test = soup.find("p", class_="jstest")
        if js_test:
            print(js_test.text)
        else:
            print("Element not found")
        self.app.quit()

url = "https://pythonprogramming.net/parsememcparseface/"
client_response = Client(url)
sys.exit(client_response.app.exec_())