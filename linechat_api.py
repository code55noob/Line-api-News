import requests
import time 
from bs4 import BeautifulSoup

url = "https://notify-api.line.me/api/notify"
token = "Your Token"
headres = {'content-type':'application/x-www-form-urlencoded','Authorization':'Bearer ' + token}
data = ''

while True:
    r = requests.get('http://www.thairsc.com/th/BigAccidentAll.aspx?l=th')
    soup = BeautifulSoup(r.text,'html.parser')
    results = soup.find_all('table',attrs={'class':'gv-list'})
    
    for result in results:
        new_data = result.find('a').text[2:-1].lstrip()
        if new_data != data:
            data = new_data
            requests.post(url,headers=headres, data={'message':data})
    
    time.sleep(60)
