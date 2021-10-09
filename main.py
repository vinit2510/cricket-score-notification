import time
import requests
from bs4 import BeautifulSoup
from win10toast import ToastNotifier

match_id = str(input("\nEnter Match Id>>> "))
url = 'https://www.cricbuzz.com/live-cricket-scores/' + match_id
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')

title = soup.find('div', class_='cb-nav-main cb-col-100 cb-col cb-bg-white').text
title = list(title.split(","))
title = title[0]
print("\n"+title)

toast = ToastNotifier()
icon = "bat-and-ball.ico"
length = 10


def notification():

    msg = "\n"+score()
    toast.show_toast(title, msg, icon_path=icon, duration=length)


def score():
    try:
        url = 'https://www.cricbuzz.com/live-cricket-scores/' + match_id
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'lxml')
        score_card = soup.find('div', class_='cb-col-100 cb-col cb-col-scores').text
        score_card = list(score_card.split("   "))

        if len(score_card) == 6:
            sc = score_card[2]+"\n"+score_card[-1]
        else:
            sc = score_card[1]

    except:
        sc = soup.find(
            'div', class_='cb-col cb-col-100 cb-min-stts cb-text-complete').text
        print(sc)
        exit()

    return sc


try:
    while True:
        notification()
        time.sleep(30)
except:
    print("\n--Some Error Might Be There!\n")