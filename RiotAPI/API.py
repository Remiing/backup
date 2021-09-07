import requests
import json
import pandas as pd
#from pandas import Series, DataFrame

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

api_key = "RGAPI-e4a9d93e-6cf1-47a1-af1d-399f92748ade"


def summoner_summoners(summonerName):
    url = "https://kr.api.riotgames.com/lol/summoner/v4/summoners/by-name/" + summonerName
    response = requests.get(url, headers={"X-Riot-Token": api_key})
    if response.status_code == 200:
        summoners = json.loads(response.text)
        return summoners
    else:
        print("error")


def match_matchlists(encryptedAccountId):
    url = "https://kr.api.riotgames.com/lol/match/v4/matchlists/by-account/" + encryptedAccountId
    response = requests.get(url, headers={"X-Riot-Token": api_key})
    if response.status_code == 200:
        matchlists = json.loads(response.text)
        return(matchlists)
    else:
        print("error")


def match_matches(matchId):
    url = "https://kr.api.riotgames.com/lol/match/v4/matches/" + str(matchId)
    response = requests.get(url, headers={"X-Riot-Token": api_key})
    if response.status_code == 200:
        matches = json.loads(response.text)
        print_dict(matches)

        print('teams---------------------------')
        print_list_dict(matches['teams'])
        print('participants---------------------------')
        print_list_dict(matches['participants'])
        print('participantIdentities---------------------------')
        print_list_dict(matches['participantIdentities'])

        print('df teams---------------------------')
        teams_df = pd.DataFrame(matches['teams'])
        print(teams_df)
        print('df participants---------------------------')
        participants_df = pd.DataFrame(matches['participants'])
        print(participants_df)
        print('df participantIdentities---------------------------')
        participantIdentities_df = pd.DataFrame(matches['participantIdentities'])
        print(participantIdentities_df)

        print('participants_stats_df---------------------------')
        participants_stats_df = pd.DataFrame(dict(participants_df['stats']))
        participants_stats_df = participants_stats_df.transpose()
        #participants_df = pd.concat([participants_df, participants_stats_df], axis=1)
        print(participants_stats_df)

        return matches
    else:
        print("error")

def match_timeline(matchId):
    url = "https://kr.api.riotgames.com/lol/match/v4/timelines/by-match/" + str(matchId)
    response = requests.get(url, headers={"X-Riot-Token": api_key})
    if response.status_code == 200:
        timeline = json.loads(response.text)
        return timeline
    else:
        print("error")

def league_entries(encryptedSummonerId):
    url = "https://kr.api.riotgames.com/lol/league/v4/entries/by-summoner/" + encryptedSummonerId
    response = requests.get(url, headers={"X-Riot-Token": api_key})
    if response.status_code == 200:
        entries = json.loads(response.text)
        print(entries)
        return entries
    else:
        print("error")

def temp(summonerName):
    summoner_info = summoner_summoners(summonerName)
    # print(summoner_info)
    summoner_matches = match_matchlists(summoner_info['accountId'])
    # print(summoner_matches)
    matches = summoner_matches['matches']
    # print(len(matches))
    last_match = summoner_matches['matches'][0]
    # print(last_match)
    match_info = match_timeline(last_match['gameId'])
    # print(match_info)

    print('-----------[ dict match_info ]---------------------------')
    for key, value in match_info.items():
        print(key, '\t', value)

    print('-----------[ len(participantFrames) ]---------------------------')
    participantFrames = match_info['frames']
    print(len(participantFrames))

    print('-----------[ list participantFrames ]---------------------------')
    for frame in participantFrames:
        print(frame)

    print('-----------[ dict match_info ]---------------------------')
    for key, value in participantFrames[0].items():
        print(key, '\t', value)

    print('-----------[  ]---------------------------')
    for frame in participantFrames:
        for key, value in frame.items():
            print(key, '\t', value)
        print('\n')

    summonerName = "너와떠나는여행"
    summoner_info = summoner_summoners(summonerName)
    summoner_matches = match_matchlists(summoner_info['accountId'])
    matches = summoner_matches['matches']
    last_match = summoner_matches['matches'][0]['gameId']
    match_info = match_matches(last_match)
    #print(summoner_info)
    #print(summoner_matches)
    #print(matches)
    #print(last_match)


def print_dict(dictionary):
    for key, value in dictionary.items():
        print(key, '\t', value)


def print_list_dict(list_dict):
    for dictionary in list_dict:
        for key, value in dictionary.items():
            print(key, '\t', value)

def main():
    summonerName = "너와떠나는여행"
    summoner_info = summoner_summoners(summonerName)
    encryptedSummonerId = summoner_info['id']
    encryptedPUUID = summoner_info['puuid']
    encryptedaccountID = summoner_info['accountId']

    print(encryptedSummonerId)
    entry = league_entries(encryptedSummonerId)





main()
