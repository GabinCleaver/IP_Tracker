import requests
import sys
from colorama import Fore, init

init()

def locate():
    data = requests.get("http://ip-api.com/json/" + ip + "?fields=status,message,continent,continentCode,country,countryCode,region,regionName,city,district,zip,lat,lon,timezone,currency,isp,as,mobile,proxy")
    resp = data.json()
    print(Fore.YELLOW + "\nRésultas:\n")
    print(Fore.GREEN + "Status: " + resp["status"])
    if resp["status"] == "fail":
        print(Fore.RED + "Fail: " + resp["message"])
        sys.exit()
    print(Fore.GREEN + "Continent: " + resp["continent"])
    print("Continent Code: " + resp["continentCode"])
    print("Pays: " + resp["country"])
    print("Pays Code: " + resp["countryCode"])
    print("Region: " + resp["region"])
    print("Region Nom: " + resp["regionName"])
    print("Ville: " + resp["city"])
    print("Districte: " + resp["district"])
    print("Code Postal: " + resp["zip"])
    print("Latitude: " + str(resp["lat"]))
    print("Longitude: " + str(resp["lon"]))
    print("Timezone: " + resp["timezone"])
    print("Monnaie: " + resp["currency"])
    print("Opérateur: " + resp["isp"])
    print("AS: " + resp["as"])
    print("Mobile: " + str(resp["mobile"]))
    print("Proxy: " + str(resp["proxy"]))

print(Fore.LIGHTCYAN_EX + "Bienvenue sur l'IP Tracker")
ip = input(Fore.LIGHTCYAN_EX + "Entrez l'IP :\n[>] ")
locate()