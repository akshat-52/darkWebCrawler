import sys
import os


def torSearcher(url):

    import requests
    import random

    def get_tor_session():
        session = requests.session()
        session.proxies = {'http':  'socks5h://127.0.0.1:9050',
                           'https': 'socks5h://127.0.0.1:9050'}
        return session

    session = get_tor_session()

    print("Getting ...", url)
    result = session.get(url).text

    import string
    filename = ''.join(random.choice(string.ascii_lowercase)
                       for i in range(16))
    with open(f"{filename}.txt", "w+", encoding="utf-8") as newthing:
        newthing.write(result)


programname = os.path.basename(sys.argv[0])

try:
    thelist = sys.argv[1]
    print("Opening ...", thelist)
    with open(thelist, "r", encoding="utf-8") as newfile:
        data = newfile.readlines()
        try:
            #
            for k in data:
                k = k.replace("\n", "")
                k = "http://" + k
                torSearcher(k)
        except Exception as E:
            print(E)
except:
    print("Usage : {} <newlineSeperatedList.txt>".format(programname))
