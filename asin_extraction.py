import concurrent.futures
import requests
from bs4 import BeautifulSoup
from collections import Counter
import json
import concurrent.futures
import time
import requests
import re
NUM_THREADS = 50

def get_player_links(url):
  links=[]
  resp = requests.get(url,headers={"User-Agent": "Mozilla/5.0 (X11; CrOS x86_64 12871.102.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.141 Safari/537.36"})
  soup = BeautifulSoup(resp.content, 'html.parser')
  #soup = BeautifulSoup(html_page, "lxml")
  for link in soup.findAll('a'):
    common_link = link.get('href')
    if "www.amazon" in common_link:
      links.append(common_link)
  return(links)

def asins(url):
  asins = re.findall(r'/dp/(\w{10})|/product/(\w{10})', url)
  return(asins)


def inputurls():
  a=1
  with open("/content/urls.txt",'r') as urllist:
    for url in urllist.readlines():
      data = get_player_links(url)
      with open('output.txt','w') as outfile:
        for link in data:
          json.dump(link,outfile)
          outfile.write("\n")
      v=[]
      with open("/content/output.txt",'r') as urllist:
        for url in urllist.readlines():
          #print(url)
          rr = asins(url) 
          #print(rr)
          v.append(rr)
      with open('output1.txt','a') as outfile:
        j=1
        outfile.write("The ASIN number of the products found on link ")
        json.dump(a,outfile)
        outfile.write(" are as follows: ")
        outfile.write("\n")
        for i in v:
          outfile.write("\n")
          outfile.write("The ASIN number of product ")
          json.dump(j,outfile)
          j=j+1
          json.dump(i[0][0],outfile)
          outfile.write("\n")
        outfile.write("\n\n\n")
        a=a+1



start_time = time.time() 
#inputurls()
with concurrent.futures.ThreadPoolExecutor(max_workers=NUM_THREADS) as executor:
  executor.map(inputurls())

total_time = time.time() - start_time
print(total_time)
