import urllib.request

def reqURL(url):
    with urllib.request.urlopen(url) as response:
        res = response.read()
        return res
