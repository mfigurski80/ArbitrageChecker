# @author Mikolaj Figurski
# This is an app meant to check the FX market for arbitrage opportunities.
# In reality, these opportunites mostly cannot be taken advantage of due to the fee for converting currency

# Market data comes from https://api.exchangeratesapi.io
# Notice: it only gets updated once every day

import urllib.request, json

def getJSONFrom(urlToGet):
    with urllib.request.urlopen(urlToGet) as response:
        data = json.loads(response.read().decode())
        return data

base_url = "https://api.exchangeratesapi.io/latest"
cur_to_check = ["USD", "EUR", "CAD", "GBP", "PLN", "RUB"]

# 2x2 dict for storing all exchange rates
rates = {}
for pos, cur in enumerate(cur_to_check):
    url = base_url + "?base=" + cur
    base_rate = getJSONFrom(url)["rates"];
    base_rate = {exch:base_rate[exch] for exch in base_rate if exch in cur_to_check and exch != cur}
    base_rate[cur] = 1
    rates[cur] = base_rate

# print(rates)



# Actual checker
maxVal = 0
maxTriangle = ""

for i, base in enumerate(cur_to_check):
    for j, second in enumerate(cur_to_check):
        for third in cur_to_check:
            val = 1*rates[base][second]*rates[second][third]*rates[third][base]
            if val > maxVal:
                maxVal = val
                maxTriangle = base + " -> " + second + " -> " + third + " -> " + base

# print max
print("MAXIMUM ARBITRAGE OPPORTUNITY:")
print(maxTriangle,":",maxVal)
