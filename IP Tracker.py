import requests
import argparse
import json

if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument("-i", "--ipaddress", help = "IP Address To Track")
	args = parser.parse_args()
	ip = args.ipaddress
	url = "http://ip-api.com/json/"+ ip
	response = requests.get(url)
	data = json.loads(response.content)
	
	print("\t[+] IP \t", data["query"])
	print("\t[+] CITY \t", data["city"])
	print("\t[+] ISP \t", data["isp"])
	print("\t[+] LOC \t", data["country"])
	print("\t[+] REG \t", data["regionName"])
	print("\t[+] TIME \t", data["timezone"])
	print("\t[+] ZIP \t", data["zip"])
	print("\t[+] LAT \t", data["lat"])
	print("\t[+] LON \t", data["lon"])
