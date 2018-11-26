import urllib.request, json

def getJSONFrom(urlToGet):
    with urllib.request.urlopen(urlToGet) as response:
        data = json.loads(response.read().decode())
        return data

access_key = "bdf49805e3ef4e4fac1cf6251f5eae5c"
url = "http://data.fixer.io/api/latest?access_key=%s"% (access_key)

print(getJSONFrom(url))
