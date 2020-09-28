import requests

url = "https://api.openweathermap.org/data/2.5/weather"
api_key = "f591ccda7b2dd33507868b4e201fae7c"

def beginMenu():
	print("")
	print("Welcome to the Python Weather App!")
	print("")


def mainfunc():
	beginMenu()
	againTest = "0"
	while againTest != "Q":
		testNum = "0"
		cityZip = "0"
		while testNum != "200":
			print("Please list a city or ZIP Code you would like to search, or Q to quit. You can list")
			print("a city name or city, two-letter state code if in the US, and two-letter country code")
			cityZip = input("Example, Springfield, NE, US or Toronto, CA: ")
			againTest = str.upper(cityZip)
			if againTest == "Q":
				print("")
				exit("Thank you for using the Python Weather App.")
			if cityZip.isnumeric() == True:
				payload = {'zip': cityZip, 'units': 'imperial', 'appid': api_key}
			elif cityZip.isnumeric() == False:
				cityString = str.upper(cityZip)
				payload = {'q': cityZip, 'units': 'imperial', 'appid': api_key}
				print("")
			print (f"URL: {url}")
			print("")
			response = requests.get(url, params=payload)
			data = response.json()
			testNum = str(data['cod'])
			if testNum == "404":
				print("I'm sorry, that city or ZIP code isn't showing. Please try another one.")
				print("")
		main = data['main']
		sys = data['sys']
		cityName = data['name']
		countryName = sys['country']
		cityTemp = main['temp']
		cityPressure = main['pressure']
		cityHumidity = main['humidity']
		report = data['weather']
		weather_description = report[0]['description']
		print()
		print("For " + str(cityName) + ", " + str(countryName) + ":")
		print("The temperature is " + str(cityTemp))
		print("The atmospheric pressure is " + str(cityPressure))
		print("The humidity is " + str(cityHumidity))
		print("The sky is " + weather_description)	
		print("")


mainfunc()




#.format(cityZip)
#api_key = "f591ccda7b2dd33507868b4e201fae7c"
#, 'appid': api_key