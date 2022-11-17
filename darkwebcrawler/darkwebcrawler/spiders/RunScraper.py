# import the actual scraper
import requests

url = "http://ip-api.com/json/"
key = requests.get(url)
# print(key.text)
if "Chennai" in key.text or "Vellore" in key.text or "India" in key.text:
    #print("Your VPN might not be on !!")
    safe = False
else:
    safe = True

if safe == False:
    import ahmiascraper
    ahmiascraper.Scraper()
else:
    print("IP change failed, try again later.")
