import requests
from html.parser import HTMLParser
import sys
import nlp_rake

from wordcloud import WordCloud
import matplotlib.pyplot as plt

url = 'https://en.wikipedia.org/wiki/Data_science'

text = requests.get(url).content.decode('utf-8')
print(text[:1000])



class MyHTMLParser(HTMLParser):
    script =  False
    res = ""
    def handle_starttag(self, tag, attrs):
        if tag.lower() in ["script","style"]:
            self.script = True
    def handle_endtag(self,tag):
        if tag.lower() in ["script", "style"]:
            self.script = False
    def handle_data(self, data):
        if str.strip(data)=="" or self.script:
            return
        self.res += ''+data.replace('[edit]','')

parser = MyHTMLParser()
parser.feed(text)
text = parser.res
print(text[:1000])

extractor = nlp_rake.Rake(max_words=2, min_freq=3,min_chars=5)
res = extractor.apply(text)
print(res)

# def plot(pair_list):
#     k,v = zip(*pair_list)
#     plt.bar(range(len(k)),v)
#     plt.xticks(range(len(k)),k,rotation='vertical')
#     plt.show()

# plot(res)

wc = WordCloud(background_color='white',width=800,height=600)
plt.figure(figsize=(15,7))

plt.imshow(wc.generate(text))
wc.generate(text).to_file('./images/ds_wordcloud.png')