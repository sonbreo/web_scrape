from os import get_terminal_size, linesep
from bs4 import BeautifulSoup
import requests
import csv

class WebsiteParse:
    def __init__(self,
                url: str):
        self.url = url
        self.sheet = {}
        self.name = {}

        page = requests.get(self.url)
        self.sheet['Price'] = []
        self.soup = BeautifulSoup(page.content, 'html.parser')

    def gumtree_parse(self, wordlist: str):
        wordlist = wordlist.split()
        # for line in soup.find_all('span', class_='user-ad-price-new-design__price'):
        #     self.sheet['Price'].append(line.get_text())
        
        self.sheet['Name'] = []
        # Parse: Listing/title
        count = 0 
        for line in self.soup.find_all('span', class_='user-ad-row-new-design__title-span'):
            for word in wordlist:
                if word in line.get_text().lower():
                    self.sheet['Name'].append(line.get_text())
                    self.parse_price(count)
            count += 1
                        
            # self.sheet['Name'].append(line.get_text())
        low = 100
        high = 500
        # self.price_range([low, high])
        self.price_range(low, high)

        # TODO: Implement price velocity/volume
        # self.sheet['Date of Listing'] = []
        # for line in soup.find_all('p', class_='user-ad-row-new-design__age'):
        #     self.sheet['Date of Listing'].append(line.get_text())
        
        # self.csv_output()
        return self.sheet

    def parse_price(self, count: int):
        self.sheet['Price'].append(self.soup.find_all('span', class_='user-ad-price-new-design__price')[count].get_text())
        return self.sheet
    
    # def price_range(self, *range: list):
    def price_range(self, low: int, high: int):
        """
        Input: [Low, High] Integer values to specify the dollar range. 
        Output: Update sheet with items within the price range.

        Filter out any items listed outside the price range specified.

        TODO:
        - Loop through the dictionary
        - Check if 'price' is within 'range'
        - If yes, then do nothing
        - If no, then pop item off the dictionary list for BOTH name and price
        """
        import pprint
        pprint.pprint(self.sheet['Price'])
        print('='*30)
        
        """
        TODO: The list gets updated everytime it finds a value that shouldn't belong to the list and we need to update the loop
        or a better way to work around this.
        """
        # for i in len(self.sheet['Price']):
            # try:
                # if low > int(self.sheet['Price'][i])



        # for line in self.sheet['Price']:
        #     try:
        #         if low > int(line.replace('$', '')) or int(line.replace('$', '')) > high:
        #             temp.append(self.sheet['Price'].index(line))
        #             # self.sheet['Price'].pop(self.sheet['Price'].index(line))  
        #     except ValueError:
        #         temp.append(self.sheet['Price'].index(line))
        #         # self.sheet['Price'].pop(self.sheet['Price'].index(line))
        # for i in temp:
        #     self.sheet['Price'].pop(temp[i])
        # pprint.pprint(self.sheet['Price'])










    # def csv_output(self):
    #     with open('gumtree_data.csv', 'r+', newline='') as csvfile:
    #         writer = csv.writer(csvfile)
    #         for line in csvfile:
    #             if 'Price' in line:
    #                 print('ye')
    #                 with open('gumtree_data.csv', 'a+', newline='') as csvfile:
    #                     writer.writerows(zip(*self.sheet.values()))
    #             else:
    #                 with open('gumtree_data.csv', 'a+', newline='') as csvfile:
    #                     writer.writerow(self.sheet.keys())
    #                     writer.writerows(zip(*self.sheet.values()))


