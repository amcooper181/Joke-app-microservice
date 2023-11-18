# Joke Generating App Microservice

## Pre-requirements

The [JokeAPI Python Wrapper](https://github.com/leet-hakker/JokeAPI-Python) must be installed.

The [Requests library](https://pypi.org/project/requests/) must be installed.

## Startup

In order to use the microservice, it must be launched first. Launch a terminal or command prompt window at the directory containing the joke_requester_v2.py file, and run:

`$ python3.11 joke_requester_v2.py`

This will start the service. The following should be displayed in the terminal, confirming the service is running:

`Server started at http://localhost:8080`

## Requesting Data

The Requests library is used to interact with this service. Paste the following at the top of your Python file, or into your Python console:

`import requests`

Now, you can request a new joke using a GET request as follows:

`response = requests.get('http://localhost:8080')`

## Receiving/Accessing the joke

Accessing the joke can be done easily:

`new_joke = response.text`
