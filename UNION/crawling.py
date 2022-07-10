import requests
from bs4 import BeautifulSoup
import operator


def take_level_starforce(nicknames):
    union = []
    search = "https://maplestory.nexon.com/Ranking/World/Total?c="

    for nickname in nicknames:
        url = search + nickname

        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")

        info_url = soup.select('#container > div > div > div > div.rank_table_wrap > table > tbody > tr.search_com_chk > td.left > dl > dt > a')
        url = 'https://maplestory.nexon.com/' + info_url[0].attrs['href']

        level = int(soup.select('#container > div > div > div:nth-child(4) > div.rank_table_wrap > table > tbody > tr.search_com_chk > td:nth-child(3)')[0].text.replace('Lv.', ''))

        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        starforce = int(soup.select('#container > div.con_wrap > div.contents_wrap > div > div.tab01_con_wrap > table:nth-child(4) > tbody > tr:nth-child(8) > td:nth-child(4) > span')[0].text)

        #union[nickname] = [level, starforce]
        union.append((nickname, level, starforce))

    return union


def union_level_power(nickname):

    url = 'https://maplestory.nexon.com/Ranking/Union?c=' + nickname
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    union_level = int(soup.select('#container > div > div > div:nth-child(4) > table > tbody > tr.search_com_chk > td:nth-child(3)')[0].text.replace(',', ''))
    union_power = int(soup.select('#container > div > div > div:nth-child(4) > table > tbody > tr.search_com_chk > td:nth-child(4)')[0].text.replace(',', ''))
    return [union_level, union_power]

def main():

    '''
    search = "https://maplestory.nexon.com/Ranking/World/Total?c="
    nicknames = []
    mapleM = []

    union = take_level_starforce(nicknames)
    union.sort(key=lambda x: (x[1], x[2]), reverse=True)
    print(union, type(union))
    print(union[1], type(union[1]))

    write_data = open('union.txt', 'w')
    for character in union:
        data = '%s,%d,%d\n' % (character[0], character[1], character[2])
        write_data.write(data)
    write_data.close()

    '''

    read_data = open('union.txt', 'r')
    union = []
    while True:
        line = read_data.readline()
        if not line: break
        data = line.replace('\n', '').split(',')
        data[1], data[2] = int(data[1]), int(data[2])
        union.append(tuple(data))
    read_data.close()

    union.sort(key=lambda x: (x[1], x[2]), reverse=True)
    #print(union, type(union))
    #print(union[1], type(union[1]))

    union_level = union_level_power(union[0][0])
    print(union_level)


main()
