import requests

user = 'alexey'
password = 'styagaylo'
base_url = 'http://httpbin.org/'

def test_my_first_api_test():
   r = requests.post(base_url + 'post', data={'user': user, 'password': password})
   assert r.status_code == 200, "Unexpected status code: {}".format(r.status_code)
   assert r.json()['url'] == base_url + 'post', "Unexpected url: {}".format(r.json()['url'])
   assert r.json()['form']['user'] == user + 'post', "Unexpected user: {}".format(r.json()['form']['user'])
   assert r.json()['form']['password'] == password + 'post', "Unexpected password: {}".format(r.json()['form']['password'])


#3695628848344d43a89273224ff42240
