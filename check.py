# @author Mikolaj Figurski
# This is an app meant to check the FX market for arbitrage opportunities.
# In reality, these opportunites mostly cannot be taken advantage of due to the fee for converting currency

# Market data comes from https://api.exchangeratesapi.io

import urllib.request, json

def getJSONFrom(urlToGet):
    with urllib.request.urlopen(urlToGet) as response:
        data = json.loads(response.read().decode())
        return data

base_url = "https://api.exchangeratesapi.io/latest"
cur_to_check = ["USD", "EUR", "BGN", "CAD", "PLN", "AUD"]

rates = {}
for pos, cur in enumerate(cur_to_check):
    # url = base_url + "?base=" + cur + "&symbols=" + ",".join(cur_to_check)
    url = base_url + "?base=" + cur
    print(url)
    base_rate = getJSONFrom(url)["rates"];
    print(base_rate.keys())
