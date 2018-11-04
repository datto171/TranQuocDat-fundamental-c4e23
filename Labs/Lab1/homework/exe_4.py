from pymongo import MongoClient
from matplotlib import pyplot

uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"
client = MongoClient(uri)
db = client.get_database()
customers = db["customers"]
customers_list = customers.find()

customers_number = 0
customer_ref_type = []
customer_ref_count = []

for i in customers_list:
    customers_number += 1
    if i['ref'] not in customer_ref_type:
        customer_ref_type.append(i['ref'])
        customer_ref_count.append(1)
    else: 
        for k in range(len(customer_ref_type)):
            if i['ref'] == customer_ref_type[k]:
                customer_ref_count[k] +=1

pyplot.pie(customer_ref_count, labels=customer_ref_type, autopct="%.1f%%", shadow=True)
pyplot.title("Customer's references")
pyplot.axis('equal')
pyplot.show()

#6 dong connect
client.close()