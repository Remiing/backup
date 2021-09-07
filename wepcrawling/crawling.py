import requests
from bs4 import BeautifulSoup


def slice(kdatag):
    kdatag = kdatag.replace("\n", "")
    kdatag = kdatag.replace("\t", "")
    kdatag = kdatag.replace(" ", "")
    return kdatag


def crawling(link):
    response = requests.get(link)
    soup = BeautifulSoup(response.text, "html.parser")

    result = []
    kda = []
    champ = []

    record = soup.select('div.GameItemWrap')
    for i in record:
        result.append(i.select('div.GameResult')[0].text.strip())
        kdatag = i.select('div.KDA > div.KDA')[0].text
        kda.append(slice(kdatag))
        champ.append(i.select('div.ChampionName')[0].text.strip())


    for i in range(5):
        print('--------')
        print(champ[i])
        print(result[i])
        print(kda[i])


def main():
    url = "https://www.op.gg/summoner/userName="
    nickname = input('Enter your nickname: ')
    link = url+nickname
    crawling(link)


main()
