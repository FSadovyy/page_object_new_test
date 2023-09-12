class BasePage:
    def __init__(self, browser, url):
        self.browser, self.url = browser, url

    def open(self):
        self.browser.get(self.url)