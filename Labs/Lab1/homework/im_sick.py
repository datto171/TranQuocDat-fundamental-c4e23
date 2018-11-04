from gmail import GMail, Message
from random import choice
import datetime

gmail = GMail("vodoimavuong1701@gmail.com","maulanh171")

now = datetime.datetime.now()
# print(now.year, now.month, now.day, now.hour, now.minute, now.second)


while True:
    if now.hour == 7 and now.minute == 0 and now.second == 0:
        content = "Em chào sếp, hôm nay em thấy người không được khỏe sếp cho em nghỉ nha"
        message = Message("Đơn xin nghỉ làm", to="dattq1701@gmail.com", html=content)
        gmail.send(message)

        break
