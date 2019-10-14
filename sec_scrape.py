from urllib.request import urlopen
import re,csv
url="http://quotes.toscrape.com/"
response=urlopen(url)
html_res=response.read().decode()
res_div="<div class=\"quote\" itemscope itemtype=\"http://schema.org/CreativeWork\">(.*?)</div>"
res_quotes=" <span class=\"text\" itemprop=\"text\">(.*?)</span>"
res_authors="<small class=\"author\" itemprop=\"author\">(.*?)</small>"
res_keys="<a class=\"tag\".*?>(.*?)</a>"
divs=re.findall(res_div,html_res,re.M|re.S|re.I)
with open("quote.csv","wt",newline="") as f:
    w=csv.writer(f)
    for i in divs:
        r1=re.search(res_quotes,i).group(1)
        r2=re.search(res_authors,i).group(1)
        r3=",".join(re.findall(res_keys,i))
        temp=[r1,r2,r3]
        print(temp)
        w.writerow(temp)