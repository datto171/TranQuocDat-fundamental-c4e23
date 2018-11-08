from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel
from collections import OrderedDict

#1. connect toi trang web 
url = "https://www.apple.com/itunes/charts/songs"
conn = urlopen(url)

#2. download content web page
raw_data = conn.read()
page_content = raw_data.decode("utf-8")

#3. Luu file
# with open("itunes.html", "wb") as file:
#     file.write(raw_data)

#4. Find ROI region
soup = BeautifulSoup(page_content, "html.parser")
section = soup.find("section", "section chart-grid") #href ="", id=""
# print(section.prettify())

# #5. Extract data 
li_list = section.ul.find_all("li")

song_list = []
for li in li_list:
    a = li.h4.a
    name =  li.h3.string
    artist = li.h4.string
    song = OrderedDict({
        "name"   : name,
        "artist" : artist,
    })
    song_list.append(song)
# print(song_list)

# #6. Save data
pyexcel.save_as(records=song_list, dest_file_name="itunes.xls")
