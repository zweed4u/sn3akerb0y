#!/usr/bin/env python
'''
SS16ADYZ38 - Pirate black yeezy boost 350 190
SS16ADID25 - yellow nmd 170 
SS16ADID26 - nice kicks red nmd 170
'''
import requests,os;
from selenium import webdriver;
from requests.utils import dict_from_cookiejar
url='http://www.sneakerboy.com/includes/data_cart.php';


style=raw_input('Style Code? ')
size=raw_input('Size? ')
def main():
	session=requests.Session();
	session.cookies.clear();

	#in payload--- '-US11' could also be '-EU44'
	data={'a': 'add',
		'productstyle': style,
		'sku': style+'-US'+size,
		'qty': '1'};
	response=session.post(url,data=data);
	if response.content=='':
		print 'Empty response'
		main()
	else:
		print response.content
		cookies = dict_from_cookiejar(response.cookies)
		driver=webdriver.Chrome(os.getcwd()+'/chromedriver')
		driver.get('http://sneakerboy.com/cart')
		driver.delete_all_cookies()
		for key, value in cookies.items():
		    driver.add_cookie({'name': key, 'value': value})
		driver.refresh()
main()
