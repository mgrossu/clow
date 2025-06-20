# _Client for OpenWeatherMap API_

### _Implementation_
A network socket is created, and it checks whether it is possible to communicate with the server via the HTTP port (80) using Python’s 'socket' library. If the connection is successful, a GET request is constructed and sent to the server. Upon receiving the response, the program processes the message to extract the HTTP status code from the header, confirming that the request was successful.

Unnecessary parts of the response are discarded, and the remaining data (usually JSON) is parsed using Python’s 'json' library for easier handling. Based on the parsed JSON, the program extracts specific items to display, as specified.

This lightweight client displays the city name, temperature, humidity, pressure, wind direction, and wind speed after the user inputs a city name:

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
