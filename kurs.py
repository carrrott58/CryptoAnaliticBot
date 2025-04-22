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
    URL = "https://cryptorank.io/ru/price/" + book.lower() 
    HEADERS = { 
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36",
    "accept": "*/*"
    }
    html = requests.get(URL, headers=HEADERS) 

    if html.status_code == 200: 
        soup = BeautifulSoup(html.text, "html.parser") 
        
        soup_info = soup.find('div', class_="sc-14478310-0 eIGtXx") 
        text = soup_info.get_text() 
        text=text.replace(",", "")
        text=text.replace("$", "")
        text = float(text)*float(usd())
        return book.lower() + " сейчас стоит " + str(round (text, 2)).replace(".", ",") + "₽"
    else:
        return c_perevod(book)

def c_perevod(book): 
    URL = "https://cryptorank.io/ru/price/" + book.lower() + "coin"
    HEADERS = { 
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36",
    "accept": "*/*"
    }
    html = requests.get(URL, headers=HEADERS) 

    if html.status_code == 200: 
        soup = BeautifulSoup(html.text, "html.parser") 
        
        soup_info = soup.find('div', class_="sc-14478310-0 eIGtXx") 
        text = soup_info.get_text() 
        text=text.replace(",", "")
        text=text.replace("$", "")
        text = float(text)*float(usd())
        return book.lower() + "coin сейчас стоит " + str(round (text, 2)).replace(".", ",") + "₽"
    else:
        return t_perevod(book)

def t_perevod(book): 
    URL = "https://cryptorank.io/ru/price/" + tran(book).lower()
    HEADERS = { 
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36",
    "accept": "*/*"
    }
    html = requests.get(URL, headers=HEADERS) 

    if html.status_code == 200: 
        soup = BeautifulSoup(html.text, "html.parser") 
        
        soup_info = soup.find('div', class_="sc-14478310-0 eIGtXx") 
        text = soup_info.get_text() 
        text=text.replace(",", "")
        text=text.replace("$", "")
        text = float(text)*float(usd())
        return tran(book).lower() + " сейчас стоит " + str(round (text, 2)).replace(".", ",") + "₽"
    else:
        return "попробуйте написать по другому"

    

def procent(book): 
    URL = "https://cryptorank.io/ru/price/" + book.lower()
    HEADERS = { 
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36",
    "accept": "*/*"
    }
    html = requests.get(URL, headers=HEADERS) 

    if html.status_code == 200: 
        soup = BeautifulSoup(html.text, "html.parser") 
        soup_info = soup.find('div', class_="sc-8b95f51a-0 ewpiKe") 
        text = soup_info.get_text() 
        return "цена изменилась на " + text
    else:
        return c_procent(book)

def c_procent(book): 
    URL = "https://cryptorank.io/ru/price/" + book.lower() + "coin"
    HEADERS = { 
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36",
    "accept": "*/*"
    }
    html = requests.get(URL, headers=HEADERS) 

    if html.status_code == 200: 
        soup = BeautifulSoup(html.text, "html.parser") 
        soup_info = soup.find('div', class_="sc-8b95f51a-0 ewpiKe") 
        text = soup_info.get_text() 
        return "цена изменилась на " + text
    else:
        return t_procent(book)

def t_procent(book): 
    URL = "https://cryptorank.io/ru/price/" + tran(book).lower()
    HEADERS = { 
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36",
    "accept": "*/*"
    }
    html = requests.get(URL, headers=HEADERS) 

    if html.status_code == 200: 
        soup = BeautifulSoup(html.text, "html.parser") 
        soup_info = soup.find('div', class_="sc-8b95f51a-0 ewpiKe") 
        text = soup_info.get_text() 
        return "цена изменилась на " + text
    else:
        return "" 
