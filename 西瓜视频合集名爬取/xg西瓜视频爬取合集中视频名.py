import requests

f=open('txt.txt','r')
r_f=f.readlines()
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4662.6 Safari/537.36',
           'referer': r_f[0].strip()}
def r_s():
    url = r_f[1]
    r_t = requests.get(url=url, headers=headers).json()
    # print(r_t)
    for data in r_t['data']:
        print(data['title'])
r_s()