class Newspaper():

    def logging(self,s):
        import logging as lg
        lg.basicConfig(filename="News.log", level=lg.INFO, format='%(asctime)s %(message)s')
        lg.info(str(s))

    def readMe(self,str):
        from win32com.client import Dispatch
        try:
            speak=Dispatch("SAPI.SpVoice")
            speak.Speak(str)
        except Exception as e:
            self.logging(e)

    def getNews(self):
        import requests
        import json
        try:
            # Get api key from newsapi.org and sourse too
            url = ('https://newsapi.org/v2/top-headlines?sources=the-times-of-india&apiKey=cf553a03aa824d08a699a794dbfdb815')
            # converting request in text form
            news = requests.get(url).text
            news_dt = json.loads(news)
            articles = news_dt['articles']
            for i in articles:
                self.readMe(i['title'])

        except Exception as e:
            self.logging(e)

if __name__ == '__main__':
    obj1=Newspaper()
    obj1.readMe("News in India")
    obj1.getNews()
    obj1.readMe("Thanks for listening news.")