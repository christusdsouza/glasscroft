# glasscroft
Mycroft for Google Glass XE

This is a simple project to access Mycroft from Google Glass.
Basically there's a webserver to translate HTTP requests from Glass into messages on the bus, which are then collected and sent back to the Glass.
The client sends back the request it gets from the server and TTSes them out to the user.
Note this does require some setup.
First clone the repo, then go ahead and edit the server URL in the makeRequest function for the client.
You do need to have some way to connect to a computer capable of running Mycroft that you can access with the Glass, through VPN or public IP.
Next just setup a mycroft_core instance. It doesn't need audio or anything, it can be entirely headless for this. Make sure the server is running after the Mycroft instance is started, and that requests to the server are available to FastAPI. 
There you go. Compile and run the code on Glass and you should be good to go. If you have any trouble submit an issue.
