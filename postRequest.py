import requests

form_data2 = {'username': 'Masha', 'password' : '12345678!'}

url2 = 'http://127.0.0.1:8000/login/'
r2 = requests.post(url2, data=form_data2)
print(r2.status_code, r2.text)

form_data = {'waiter-id':1, 'item-ids':'1-2', 'item-counts':'9-10', 'username' : 'Masha', 'password' : '12345678!'}
url = 'http://127.0.0.1:8000/order/create/'
r = requests.post(url, data=form_data)
print(r.status_code, r.text)

form_data3 = {'username' : 'Masha', 'password' : '12345678!'}
url3 = 'http://127.0.0.1:8000/menu/'
r3 = requests.post(url3, data=form_data3)
print(r3.status_code, r3.text)