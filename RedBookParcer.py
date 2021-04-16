import requests
from bs4 import BeautifulSoup
import codecs
import pandas as pd

def main():

    #Универсальный код считывания
    #HTML с стр.
    def readPage(url):
        r = requests.get(url)
        htmlCode = r.text
        return htmlCode
        
    #Основная функция распарса
    def pageParce(htmlDoc):
            htmlCode = BeautifulSoup(htmlDoc, 'html.parser')
            #Задаем параметры супа
            return htmlCode.body.find_all('p', attrs={'class': None})

    #Базовый ЮРЛ
    #Из него исходят все  главы 
    #Книжки 
    url = "https://www.marxists.org/reference/archive/mao/works/red-book/ch"

    #Наш ДС для складывания наших цитат
    quotesDs = pd.DataFrame(columns=['quote'])

    for pageNum in range(1, 34): #Всего 33 главы в книжке
        if len(str(pageNum)) == 1:
            html = readPage(url+f'0{pageNum}.htm')#так как главы имеют вид ch01-ch33
            quotes = pageParce(html) #Парс стр
            for td in quotes: #Тк на выходе в quotes получается лист с тэгами
                quote = td.get_text()
                quotesDs = quotesDs.append({'quote' : quote}, ignore_index=True) #Складываем в  наш DS
        else:
            html = readPage(url+f'{pageNum}.htm')
            quotes = pageParce(html)
            for td in quotes:
                quote = td.get_text()
                quotesDs = quotesDs.append({'quote' : quote}, ignore_index=True)
    
    quotesDs.to_csv(r'/Applications/MaoZedong/redbook.csv',index=False)


#Запускаем скрипт 
if __name__ == '__main__':
    main()
