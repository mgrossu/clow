#### _IPK Project 1: Client for OpenWeatherMap API_

Name and surname: Marius Iustin Grossu

Login: xgross10

#### _Implementace_
Due to the assignment where we had to choose a programming language in which we can write a client for ** OpenWeatherMap **, so I chose _Python_. From the beginning, I created a network socket and checked whether it is possible to communicate with the server via HTTP port (80) using the socket library in _Python_. If the connection is successful, a ** GET request ** is created and sent to the servers. Upon receipt of the response, it processes the message so that it receives a status code from the header, which shows us that everything is OK. Unnecessary information is left and transferred to ** JSON **, for better handling using the json library. Subsequently, based on the JSON we obtained, it looks for individual items that need to be displayed as specified. This lightweight client displays city name, temperature, humidity, pressure, wind direction and speed after entering:
> $ make run api_key = <API_KEY> city = <CITY>

Not knowing how to handle this client, I extended the functionality,
> $ make help

where it shows how to start this client properly.
You must always enter a valid API key, which will be obtained by registering for free with [OpenWeatherMap] (https://openweathermap.org/).
If any information is missing, N / A is displayed.
> temp: N / A
humidity: N / A
 pressure: N / A

* example of missing information
