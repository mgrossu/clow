################################################################
#autor: Marius Iustin Grossu (mgrossu) #
#Client for OpenWeatherMap interface
################################################################

import sys
import socket
import json

"Variables"
errors=sys.stderr

sok = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

if not sok:
    print ("Failed to create a socket.", errors)
    exit(1)
try:    
    sok.connect(("api.openweathermap.org", 80))
except socket.error as fail:   
    print ("Failed to connect!", errors)
    exit(2)

if len(sys.argv) < 2:
    print ("You need to insert an argument. For more please type \"make help\"!")
    exit(0)
elif len(sys.argv) == 2:
    if sys.argv[1] == "--help":
        print("To start the program please introduce the right api key and the city in format \"make run api_key=<API KEY> city=<CITY>\". If the city name is formed from more words please introduce in this format city=\"<CITY>\". ")
        exit(0)
    else:
        print("An argument is missing! For more type \"make help\".")
        exit(0)
elif  len(sys.argv) == 3:
    print(sys.argv[2])
    if not sys.argv[2].isalpha and sys.argv[2].isspace:
       print ("Wrong city name, or is missing, type just letters please! For more \"make help\"", errors)
       exit(3)
request = ("GET /data/2.5/weather?q="+sys.argv[2]+"&APPID="+sys.argv[1]+"&units=metric HTTP/1.1\r\nHost: api.openweathermap.org\r\n\r\n")
request_bytes = str.encode(request)
sok.sendall(request_bytes)
response = sok.recv(4096)
string = response.decode('utf-8')
string_result = string.split('\r\n\r\n')
json_data = json.loads(string_result[1])
if (int(json_data["cod"])) == 401:
    print("Invalid API key! Introduce the valid API key!", errors)
    exit(4)
if 'name' in json_data: 
    print(str(json_data['name']))
else:
    print("The name of the city does not exist!", errors)
    exit(5)
if ('weather' in json_data) or ('description' in json_data["weather"][0]):
    print(str(json_data["weather"][0]["description"]))
else:
    print('N/A')
if ('main' in json_data): 
    if ('temp' in json_data["main"]):
        print("temp: "+str(json_data['main']['temp'])+" °C")
    else: 
        print('temp: N/A') 
    if ('humidity' in json_data["main"]):
        print("humidity: "+str(json_data['main']['humidity'])+" %")
    else: 
        print('humidity: N/A') 
    if ('pressure' in json_data["main"]):
        print("pressure: "+str(json_data['main']['pressure'])+" hPa")
    else: 
        print('pressure: N/A')
else:
    print('temp: N/A')
    print('humidity: N/A')
    print('pressure: N/A')
if ('wind' in json_data):
    if ('speed' in json_data["wind"]) and ('deg' in json_data["wind"]):  
        print("wind-speed: "+str(json_data['wind']['speed'])+" km/h")
        print("wind-deg: "+str(json_data['wind']['deg']))
    elif ('speed' in json_data["wind"]) and ('deg' not in json_data["wind"]):
        print("wind-speed: "+str(json_data['wind']['speed'])+" km/h")
        print('widn-deg: N/A')
    elif ('speed' not in json_data["wind"]) and ('deg' in json_data["w    ind"]):
        print('wind-speed: N/A')
        print("wind-speed: "+str(json_data['wind']['speed'])+" km/h")
else:
    print('wind-speed: N/A')
    print('widn-deg: N/A')
