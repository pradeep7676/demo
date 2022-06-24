from selenium.webdriver.common.by import By


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    title = (By.XPATH, "//h3[@class='home-intro-post-title']")
    authors = (By.XPATH, "//div[@class='home-intro-post-meta']")
    descriptions = (By.CSS_SELECTOR, "a[class='home-posts'] p")


    def getTitle(self):
        return self.driver.find_elements(*HomePage.title)

    def getauthors(self):
        return self.driver.find_elements(*HomePage.authors)

    def getdescriptions(self):
        return self.driver.find_elements(*HomePage.authors)

