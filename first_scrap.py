from urllib.request import  urlopen
import re,csv
url="https://www.lagou.com/gongsi/"
response=urlopen(url)
html_text=response.read().decode()
res_url="<a.*?href=\"(http.*?)\".*?>"
r=re.findall(res_url,html_text,re.M|re.S|re.I)

with open("lagou.csv","wt",newline="") as f:
    w=csv.writer(f)
    for i in r:
        w.writerow([i])



img_url="https://www.baidu.com/img/bd_logo1.png?where=super"
response_img=urlopen(img_url)
with open("1.jpg","wb") as f1:
    f1.write(response_img.read())
