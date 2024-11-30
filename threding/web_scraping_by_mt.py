'''https://python.langchain.com/v0.2/docs/introduct

https://python.langchain.com/v0.2/docs/concepts/

https://python.langchain.com/v0.2/docs/tutorials.
'''
import threading
import requests
from bs4 import BeautifulSoup

urls=[
    'https://python.langchain.com/v0.2/docs/introduct',
    'https://python.langchain.com/v0.2/docs/concepts/',
    'https://python.langchain.com/v0.2/docs/tutorials.'
]

def fatch_contant(urls):
    response=requests.get(urls)
    soup=BeautifulSoup(response.content,'html.parser')
    print(f'Facted {len(soup.text)} characters from {urls}')
threads=[]
for url in urls:
    thread=threading.Thread(target=fatch_contant,args=(url,))
    threads.append(thread)
    thread.start()
for thread in threads:
    thread.join()
print('All web pages facthed ')