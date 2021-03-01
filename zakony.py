from bs4 import BeautifulSoup
from urllib.request import urlopen
import re

def ustanoveniZakona(paragraf, zakon):
    url = f"https://www.zakonyprolidi.cz/cs/{zakon}" # např. "https://www.zakonyprolidi.cz/cs/2012-89"
    page = urlopen(url)
    html = page.read().decode("utf-8")
    soup = BeautifulSoup(html, "html.parser")

    pozadavek = paragraf # např. "§ 3000"
    regex = re.compile('L.')
    uroven = 0

    nacteni = soup.find_all('p')
    vypis = False
    vystup = ""
    for p in nacteni:
        if p.get('class') == None:
            continue
        if ('PARA' in p.get('class') or 'CLANEK' in p.get('class')) and pozadavek == p.getText():
            vypis = True
            uroven = [string for string in p.get('class') if re.match(regex, string)][0]
        elif [string for string in p.get('class') if re.match(regex, string)][0] == uroven and pozadavek != p.getText(): # 'PARA' in p.get('class') and 
            vypis = False     
        if vypis:
            vystup += f"{p.getText()}\n"
    return vystup        
        # print(p.get('class'))
        # print(p.getText())
    # print(z)
    # print(soup.find('p').getText())