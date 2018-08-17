from bs4 import BeautifulSoup
import requests
import json
meme_pages_url = [
    'allindiabakchod/'
    # 'witty_indian/'
] 

insta_url = 'https://www.instagram.com/'

for i in meme_pages_url:
	main_url = insta_url + i
	res = requests.get(main_url)
	soup = BeautifulSoup(res.text,'html.parser')
	script_tag = soup.find('body').find('script')
	raw_string = script_tag.text.strip().replace('window._sharedData =', '').replace(';', '')
	print(json.loads(raw_string)[21:-1])
	
