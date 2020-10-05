# including requires librarires
import requests
import argparse
import json

# calling main method
if __name__ == "__main__":
	parser = argparse.ArgumentParser()					#argument parser to accept arguments when running script from a shell
	parser.add_argument("-i", "--ipaddress", help = "IP Address To Track")
	args = parser.parse_args()
	ip = args.ipaddress							#taking IP address
	url = "http://ip-api.com/json/"+ ip					#appending IP to domain
	response = requests.get(url)						#getting Response of the Query
	data = json.loads(response.content)					#Getting useful data from the response that we get
	
	print("\t[+] IP \t", data["query"])					#	printing required IP Address
	print("\t[+] CITY \t", data["city"])					#	printing city of the given IP Address
	print("\t[+] ISP \t", data["isp"])					#	printing ISP of the given IP Address
	print("\t[+] LOC \t", data["country"])					#	printing Country of the given IP Address
	print("\t[+] REG \t", data["regionName"])				#	printing Region of the given IP Address
	print("\t[+] TIME \t", data["timezone"])				#	printing Timezone of the given IP Address
	print("\t[+] ZIP \t", data["zip"])					#	printing ZIP Code of the given IP Address
	print("\t[+] LAT \t", data["lat"])					#	printing Latitude of the given IP Address
	print("\t[+] LON \t", data["lon"])					#	printing Longitude of the given IP Address
