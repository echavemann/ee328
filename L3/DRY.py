import itertools
import json
import requests


driver = "fintechclub.ece.northwestern.edu.api.main.nuse"
res1 = requests.get(driver)
res1 = dict(res1)
endpoint = res1[endpoint]
value1 = res1[value]
res2 = requests.get(endpoint)
res2 = dict(res2)
endpointa = res2[endpoint]
value2 = res2[endpoint]
res3 = requests.get(endpointa)
res3 = dict(res3)
...
