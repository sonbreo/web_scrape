from os import get_terminal_size, linesep
from typing import Deque
from bs4 import BeautifulSoup
import requests

"""
TODO Features:
- Parse URL
- Notify system (email)
- Parse images
- Fix signature of price_range function
- Improve efficiency of check loop
"""

class WebsiteParse:
    def __init__(self,
                url: str):
        self.url = url
        self.sheet = {}
        self.name = {}

        page = requests.get(self.url)
        self.sheet['Name'] = []
        self.sheet['Price'] = []
        self.soup = BeautifulSoup(page.content, 'html.parser')

    def gumtree_parse(self, wordlist: str):
        wordlist = wordlist.split()
        
        # Parse: Listing/title
        count = 0 
        for line in self.soup.find_all('span', class_='user-ad-row-new-design__title-span'):
            for word in wordlist:
                if word in line.get_text().lower():
                    self.sheet['Name'].append(line.get_text())
                    self.parse_price(count)
            count += 1
                        
            # self.sheet['Name'].append(line.get_text())
    
        """
        TODO: 
        - Input low/high parameters into the signature of the function.
        - Is it possible to put in a two-dimensional array for the signature of the function.
        """
        low = 100
        high = 500
        # self.price_range([low, high])
        self.price_range(low, high)
        self.remove_duplicates()

        # TODO: Implement price velocity/volume
        # self.sheet['Date of Listing'] = []
        # for line in soup.find_all('p', class_='user-ad-row-new-design__age'):
        #     self.sheet['Date of Listing'].append(line.get_text())
        
        # self.csv_output()
        return self.sheet

    def parse_price(self, count: int):
        """
        Parse price values from GumTree website.
        TODO: Implement into GumTree parse function.
        """
        self.sheet['Price'].append(self.soup.find_all('span', class_='user-ad-price-new-design__price')[count].get_text())
        return self.sheet
    
    # def price_range(self, *range: list):
    def price_range(self, low: int, high: int):
        """
        Input: [Low, High] Integer values to specify the dollar range. 
        Output: Update sheet with items within the price range.

        Filter out any items listed outside the price range specified.
        """ 
        
        while True:
            # print('testing...')
            for i in range(len(self.sheet['Price'])):
                try:
                    # If price value is outside of range then remove from dictionary.
                    if low > int(self.sheet['Price'][i].replace('$', '')) or int(self.sheet['Price'][i].replace('$', '')) > high:
                        self.sheet['Price'].pop(i)
                        self.sheet['Name'].pop(i)
                        break
                except ValueError:
                    # If price value is a non-integer than remove from dictionary.
                    self.sheet['Price'].pop(i)
                    self.sheet['Name'].pop(i)
                    break
            
            # When price range filtering finishes, exit out of while loop.
            if i == len(self.sheet['Price']):
                break
        
        return self.sheet

    def remove_duplicates(self):
        """
        Remove duplicate entries from dictionary.
        """    
        
        while True:
            for i in range(len(self.sheet['Name'])):
                if i == 0:
                    continue
                else:
                    if self.sheet['Name'][i] == self.sheet['Name'][i-1]:
                        self.sheet['Name'].pop(i)
                        self.sheet['Price'].pop(i)
                        break
            if i == len(self.sheet['Name']):
                break
        return self.sheet






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


