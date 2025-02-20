import requests 
from bs4 import BeautifulSoup 
from googletrans import Translator #pip install googletrans==4.0.0-rc1

def tran(text):
    translator = Translator()
    translated = translator.translate(text, src='ru', dest='en')
    return translated.text



def usd(): 
    URL = "https://finance.rambler.ru/currencies/USD/"
    HEADERS = { 
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36",
    "accept": "*/*"
    }
    html = requests.get(URL, headers=HEADERS) 

    if html.status_code == 200: 
        soup = BeautifulSoup(html.text, "html.parser") 
        
        soup_info = soup.find('span', class_="_ZXx92_y CVUkSwiH") 
        text = soup_info.get_text() 

        return text 
    else:
        return False 

def perevod(book): 
    URL = "https://www.binance.com/en/price/" + book
    HEADERS = { 
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36",
    "accept": "*/*"
    }
    html = requests.get(URL, headers=HEADERS) 

    if html.status_code == 200: 
        soup = BeautifulSoup(html.text, "html.parser") 
        
        soup_info = soup.find('span', class_="t-subtitle2 text-textPrimary md:t-subtitle1 lg:t-headline5") 
        text = soup_info.get_text() 
        x=text.find("$")+1
        y=text[x:].find(" ")
        text=text[x:]
        text=text[:y]
        text=text.replace(",", "")
        x=float(text)*float(usd())
        return book + " сейчас стоит " + str(round (x, 2)).replace(".", ",") + "₽"
    else:
        return t_perevod(book)

def t_perevod(book): 
    URL = "https://www.binance.com/en/price/" + tran(book)
    HEADERS = { 
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36",
    "accept": "*/*"
    }
    html = requests.get(URL, headers=HEADERS) 

    if html.status_code == 200: 
        soup = BeautifulSoup(html.text, "html.parser") 
        
        soup_info = soup.find('span', class_="t-subtitle2 text-textPrimary md:t-subtitle1 lg:t-headline5") 
        text = soup_info.get_text() 
        x=text.find("$")+2
        y=text[x:].find(" ")
        text=text[x:]
        text=text[:y]
        text=text.replace(",", "")
        x=float(text)*float(usd())
        return tran(book) + " сейчас стоит " + str(round (x, 2)).replace(".", ",") + "₽"
    else:
        return "попробуйте написать по другому"

    

def procent(book): 
    URL = "https://www.binance.com/en/price/" + book
    HEADERS = { 
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36",
    "accept": "*/*"
    }
    html = requests.get(URL, headers=HEADERS) 

    if html.status_code == 200: 
        soup = BeautifulSoup(html.text, "html.parser") 
        try:
            soup_info = soup.find('span', class_="t-subtitle2 md:t-subtitle1 lg:t-headline5 text-buy") 
            text = soup_info.get_text() 
        except:
            soup_info = soup.find('span', class_="t-subtitle2 md:t-subtitle1 lg:t-headline5 text-sell") 
            text = soup_info.get_text()
        if (text[0]=="+"): 
            return "курс " + book + " поднялся на " + text
        elif (text[0]=="-"):
            return "курс " + book + " опустился на " + text
    else:
        return t_procent(book)
    
def t_procent(book): 
    URL = "https://www.binance.com/en/price/" + tran(book)
    HEADERS = { 
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36",
    "accept": "*/*"
    }
    html = requests.get(URL, headers=HEADERS) 

    if html.status_code == 200: 
        soup = BeautifulSoup(html.text, "html.parser") 
        try:
            soup_info = soup.find('span', class_="t-subtitle2 md:t-subtitle1 lg:t-headline5 text-buy") 
            text = soup_info.get_text() 
        except:
            soup_info = soup.find('span', class_="t-subtitle2 md:t-subtitle1 lg:t-headline5 text-sell") 
            text = soup_info.get_text()
        if (text[0]=="+"): 
            return "курс " + tran(book) + " поднялся на " + text
        elif (text[0]=="-"):
            return "курс " + tran(book) + " опустился на " + text
    else:
        return ""
