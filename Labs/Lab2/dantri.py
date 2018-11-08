from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel
from collections import OrderedDict

#1. connect toi trang web 
url = "https://dantri.com.vn"
conn = urlopen(url)

#2. download content web page
raw_data = conn.read()
page_content = raw_data.decode("utf-8")

#3. Luu file
# with open("dantri.html", "wb") as file:
#     file.write(raw_data)

#4. Find ROI region
soup = BeautifulSoup(page_content, "html.parser")
ul = soup.find("ul", "ul1 ulnew") #href ="", id=""
print(ul.prettify())

#5. Extract data 
li_list = ul.find_all("li")

new_list = []
for li in li_list:
    a = li.h4.a
    title =  a.string
    link = url + a['href']
    news = OrderedDict({
        "title" : title,
        "link"  : link,
    })
    new_list.append(news)
print(new_list)

# #6. Save data
# pyexcel.save_as(records=new_list, dest_file_name="dantri.xls")
