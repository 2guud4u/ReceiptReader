from bs4 import BeautifulSoup
from selenium import webdriver
import time
import json
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import argparse
def Checker(upc,zipcode,stores,output=None):
    ret_dict = {}
    for elem in stores:
        if elem == 'Target':
            url = 'https://brickseek.com/target-inventory-checker'
        elif elem == 'Walmart':
            url = 'https://brickseek.com/walmart-inventory-checker'
        try:
            ret_dict[elem]= store_inventory(upc,zipcode,url)
            print("work")
        except:
            ret_dict[elem] = "No Availible Products"
    with open(output+'.txt','w') as json_file:
        json.dump(ret_dict,json_file,indent=4)

def store_inventory(upc,zipcode,url):
    options1 = webdriver.ChromeOptions()
    options1.add_argument('headless')
    driver = webdriver.Chrome(ChromeDriverManager().install(),options=options1)
    driver.get(url)
    print("work")
    #Selects UPC option
    typeA = driver.find_element_by_xpath('//*[@id="main"]/div/form/div/div[1]/div/div/label[2]')
    typeA.click()
    #Enters upc and zipcode
    upc_in = driver.find_element_by_id('sku')
    upc_in.send_keys(upc)
    searchbar = driver.find_element_by_id('inventory-checker-form-zip')
    searchbar.send_keys(zipcode)
    searchbar.send_keys(Keys.ENTER)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    stores_list = soup.find_all('div',{'class':'table__row'})
    store_dict = {}
    i = 0
    
    return store_dict

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Get the Inventory and Price of Item\'s given a UPC value')
    parser.add_argument('--upc','-u',type=str, metavar='',required=True,help='UPC of the Item')
    parser.add_argument('--zip','-z',type=str, metavar='',required=True,help='Your Current ZipCode')
    parser.add_argument('--stores','-s',type=str, metavar='',required=True,help='Stores You want to search In', choices=['a','w','t'])
    parser.add_argument('--output','-o',type=str, metavar='',help='Output json to a given file')
    args=parser.parse_args()
    stores = []
    if args.stores =='a':
        stores.append('Walmart')
        stores.append('Target')
    elif args.stores == 't':
        stores.append('Target')
    elif args.stores == 'w':
        stores.append('Walmart')
    Checker(args.upc,args.zip,stores,args.output)