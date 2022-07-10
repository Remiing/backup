import requests
from bs4 import BeautifulSoup
from selenium import webdriver as wd
import time
import urllib.request
import multiprocessing


def crawling(url):
    driver = wd.Chrome(executable_path="chromedriver.exe")
    driver.get(url)
    time.sleep(100.0)
    html_source = driver.page_source
    driver.close()
    soup = BeautifulSoup(html_source, 'html.parser')

    clip123 = []

    clips = soup.select('div.home__lower-content > div > div > div > div:nth-child(2) > div > div > div > div > div > div > div')
    del clips[-20:]
    for i in clips:
        toss=[]
        name = i.select('h3')[0].text
        name = name.replace('/', '')
        #print(name)
        #clip_link.append(name)
        toss.append(name)

        link = i.select('a')[0]['href']
        #print(link)
        #clip_name.append(link)
        toss.append(link)
        clip123.append(toss)

    print(clip123)

    with open('clip.txt', 'w', -1, 'utf-8') as file:
        for i in clip123:
            data = i[0] + ',' + i[1] + '\n'
            file.write(data)


def crawling2(toss):
    name = toss[0]
    name = name.replace('\\', '')
    name = name.replace('/', '')
    name = name.replace(':', '')
    name = name.replace('*', '')
    name = name.replace('?', '')
    name = name.replace('"', '')
    name = name.replace('<', '')
    name = name.replace('>', '')
    name = name.replace('|', '')
    name = name.replace("'", "")
    name = 'E:/ming/video/twitch/clip/' + name + '.mp4'
    url = toss[1].replace('\n', '')
    full_url = 'https://www.twitch.tv/saddummy/clip' + url
    driver = wd.Chrome(executable_path="chromedriver.exe")
    driver.get(full_url)
    time.sleep(1.0)
    html_source = driver.page_source
    driver.close()
    soup = BeautifulSoup(html_source, 'html.parser')
    clip_down_link = soup.select('div.video-player > div > video')[0]['src']
    urllib.request.urlretrieve(clip_down_link, name)
    print(name)



def url():
    clip_url = ""
    return clip_url


def main():
    #totla_clip_url = url()
    #crawling(totla_clip_url)
    start = time.time()
    clips = []
    with open('clip.txt', 'r', -1, 'utf-8') as file:
        for text in file:
            list1 = text.split(',/saddummy/clip')
            clips.append(list1)
    for i in clips:
        crawling2(i)

    print(time.time()-start)


main()
