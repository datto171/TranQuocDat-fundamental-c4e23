from gmail import GMail, Message
from random import choice

gmail = GMail("vodoimavuong1701@gmail.com","maulanh171")

sickeness_list = ["thuong han", "kiet li", "tieu chay"]

template = '''
    <p>chao sep,</p>
    <p>hnay em ngu day thay met lam</p>
    <p>oi zoi oi</p>
'''

sick = choice(sickeness_list)
symtom = "kiet li"

content = template.replace("{{symtom}}", symtom).replace("{{sick}}", sick)
message = Message("Don xin nghi hoc", to="dattq1701@gmail.com", html=content)
gmail.send(message)