from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel
from collections import OrderedDict

#1. connect toi trang web 
url = "http://s.cafef.vn/bao-cao-tai-chinh/VNM/IncSta/2017/3/0/0/ket-qua-hoat-dong-kinh-doanh-cong-ty-co-phan-sua-viet-nam.chn"
conn = urlopen(url)

#2. download content web page
raw_data = conn.read()
page_content = raw_data.decode("utf-8")
#3. Luu file
with open("cafe.html", "wb") as file:
    file.write(raw_data)

# 4. Find ROI region
soup = BeautifulSoup(page_content, "html.parser")
table = soup.find("table", id="tableContent") #href ="", id=""

# #5. Extract data 
tr_list = table.find_all("tr")
# -------->>>>>>>>>>> quy luật là 0 3 6 9 12 ... 
new_list = []

for tr in range(0, len(tr_list), 3):
    number = tr_list[tr].find_next()
    quy4_2016 = number.find_next()
    quy1_2017 = quy4_2016.find_next()
    quy2_2017 = quy1_2017.find_next()
    quy3_2017 = quy2_2017.find_next()
    
    stt = number.string.replace("\r\n                \xa0\xa0\r\n                ", "").replace("\r\n            ", "")
    data_quy4_2016 = quy4_2016.string
    data_quy1_2017 = quy1_2017.string
    data_quy2_2017 = quy2_2017.string
    data_quy3_2017 = quy2_2017.string

    new = {
        "number"    : stt,
        "quy4_2016" : data_quy4_2016,
        "quy1_2017" : data_quy1_2017,
        "quy2_2017" : data_quy2_2017,
        "quy3_2017" : data_quy3_2017,
    }
    new_list.append(new)

pyexcel.save_as(records=new_list, dest_file_name="cafe.xls")