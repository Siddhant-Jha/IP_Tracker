# including requires librarires
import requests
import argparse
import json

# Making a function of get_ip to increase resuability and also adding some condiiional checks for error and boundary conditions

def get_ip(ipAddress):									#taking IP address
	try:
		url = "http://ip-api.com/json/"+ ipAddress			#appending IP to domain
		response = requests.get(url)						#getting Response of the Query
		data = json.loads(response.content)					#Getting useful data from the response that we get
		if data['status'] == "fail":
			return "Fail"
		else:
			return data
	except Exception as e:
		return "Exception Ocurred: {}".format(e)
		

def main():
	parser = argparse.ArgumentParser()					#argument parser to accept arguments when running script from a shell
	parser.add_argument("ipaddress", help = "IP Address To Track") # Made IP Address a compulsory argument
	args = parser.parse_args()
	data = get_ip(args.ipaddress)
	if (data == "Fail") or ("Exception" in data):
		print(data)
		return
	else:
		if data.get("zip") == "":
			data["zip"] = "Not Found / Not Applicable"
		print("[+] IP Found\n[+] Fetching Details....\n")
		print("\t[+] IP \t", data.get("query", "Not Found")) 				# Adding the dict.get() method to display a Not found message in case of any field not found or blank					#
		print("\t[+] CITY \t", data.get("city", "Not Found"))				#
		print("\t[+] ISP \t", data.get("isp", "Not Found"))					#
		print("\t[+] LOC \t", data.get("country", "Not Found"))				#	
		print("\t[+] REG \t", data.get("regionName", "Not Found"))			#     printing required data about given IP Address
		print("\t[+] TIME \t", data.get("timezone", "Not Found"))			#
		print("\t[+] ZIP \t", data.get("zip", "Not Found"))					#
		print("\t[+] LAT \t", data.get("lat", "Not Found"))					#
		print("\t[+] LON \t", data.get("lon", "Not Found"))	


# calling main method
if __name__ == "__main__":
	main()