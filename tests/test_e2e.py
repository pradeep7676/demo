import csv

from pageObjects.homePage import HomePage
from utilities.baseClass import BaseClass


class Test_GetDetails(BaseClass):

    def test_details(self):
        homePage = HomePage(self.driver)
        list_of_data = []

        titles = homePage.getTitle()
        authors = homePage.getauthors()
        descriptions = homePage.getdescriptions()

        i = 0
        while i < (len(descriptions)):
            list_of_data.append((titles[i].text, authors[i].text, descriptions[i].text))
            if i == 8:
                break
            i = i+1


        f = open('data.csv', 'w', encoding='UTF8')
        writer = csv.writer(f)
        for line in list_of_data:
            writer.writerow(line)
            f.close()

        print(list_of_data)





