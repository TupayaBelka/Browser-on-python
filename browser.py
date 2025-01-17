import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *

class Browser(QMainWindow):
    def __init__(self):
        super().__init__()

        self.tabs = QTabWidget()
        self.setCentralWidget(self.tabs)

        self.add_new_tab()

        self.create_ui()

        self.setWindowTitle("Крутой Браузер с Вкладками")
        self.setGeometry(100, 100, 1024, 768)

    def create_ui(self):
        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.load_url)

        back_button = QPushButton("Назад")
        forward_button = QPushButton("Вперед")
        reload_button = QPushButton("Перезагрузить")
        new_tab_button = QPushButton("Новая вкладка")

        back_button.clicked.connect(self.go_back)
        forward_button.clicked.connect(self.go_forward)
        reload_button.clicked.connect(self.reload_page)
        new_tab_button.clicked.connect(self.add_new_tab)

        nav_layout = QHBoxLayout()
        nav_layout.addWidget(back_button)
        nav_layout.addWidget(forward_button)
        nav_layout.addWidget(reload_button)
        nav_layout.addWidget(new_tab_button)

        main_layout = QVBoxLayout()
        main_layout.addWidget(self.url_bar)
        main_layout.addLayout(nav_layout)

        central_widget = QWidget()
        central_widget.setLayout(main_layout)
        self.setMenuWidget(central_widget)

    def add_new_tab(self):
        """ Добавление новой вкладки """
        browser_tab = QWebEngineView()
        browser_tab.setUrl(QUrl("http://www.google.com"))

        index = self.tabs.addTab(browser_tab, "Новая вкладка")
        self.tabs.setCurrentIndex(index)
        browser_tab.urlChanged.connect(self.update_url) 

    def update_url(self, q):
        """ Обновляем строку URL при изменении страницы """
        self.url_bar.setText(q.toString())

    def load_url(self):
        """ Загружаем URL из строки ввода """
        url = self.url_bar.text()
        current_browser = self.tabs.currentWidget()
        current_browser.setUrl(QUrl(url))

    def go_back(self):
        """ Назад """
        current_browser = self.tabs.currentWidget()
        if current_browser.history().canGoBack():
            current_browser.back()

    def go_forward(self):
        """ Вперед """
        current_browser = self.tabs.currentWidget()
        if current_browser.history().canGoForward():
            current_browser.forward()

    def reload_page(self):
        """ Перезагрузка страницы """
        current_browser = self.tabs.currentWidget()
        current_browser.reload()

def main():
    app = QApplication(sys.argv)
    browser = Browser()
    browser.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
