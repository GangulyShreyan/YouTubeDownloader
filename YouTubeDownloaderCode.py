import webbrowser
import requests
import bs4
from selenium import webdriver
import time

print("Do you you enter URL or video name?")
print("Enter 1 for URL, and 2 for  video name:")
choice=int(input())


if(choice==1):
    print("Enter Youtube video link:")
    link=input()
    if(link[0:5]=='https'):
        dlink=link[0:5]+'://ss'+link[12:]
    else:
        dlink=dlink='https://ss'+link[4:]
    
    
if(choice==2):
    print("Enter video name:")
    videoname=input()
    query=videoname.replace(' ','+')
    link='https://www.youtube.com/results?search_query='+query
    res=requests.get(link)
    soup=bs4.BeautifulSoup(res.text, 'lxml')
    video = soup.findAll('div', {'class': 'yt-lockup-video'})
    video = video[0].contents[0].contents[0].contents[0]
    url=video['href']
    link='www.youtube.com'+url
    dlink='https://ss'+link[4:]
    


driver=webdriver.Firefox()
driver.get(dlink)
time.sleep(4)
driver.find_element_by_class_name('def-btn-box').click()