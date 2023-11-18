from jokeapi import Jokes # Import the Jokes class
from http.server import BaseHTTPRequestHandler, HTTPServer
import time
import asyncio

hostName = "localhost"
serverPort = 8080

class JokeServer(BaseHTTPRequestHandler):
    def do_GET(self):
        return_val = asyncio.run(self.return_joke())
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        if type(return_val) is str:
            self.wfile.write(bytes(return_val, encoding='utf-8'))
        else:
            part_1, part_2 = return_val
            self.wfile.write(bytes(part_1, encoding='utf-8'))
            self.wfile.write(bytes(part_2, encoding='utf-8'))
  


    async def return_joke(self):
        j = await Jokes()  # Initialise the class
        joke = await j.get_joke(blacklist = ['nsfw', 'racist', 'sexist', 'religious', 'political'], joke_type = "single")  # Retrieve a random joke
        joke_to_return = str(joke["joke"])
        return joke_to_return


if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), JokeServer)
    print("Server started at http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")

# Source: https://pypi.org/project/requests/
# Source: https://github.com/leet-hakker/JokeAPI-Python
