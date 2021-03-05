# Bedrock-Homeassistant

Initial commit of a bedrock integration for homeassistant. Not easibly useable as built-in minecraft mcstatus must be updated to at least 5.1.1. I put in an issue and it has been accepted into dev. Hopefully the next release after 2021.3.0 will have it. Untill then, you can add it manually if you really want.
```
ssh in developer mode or the host system
find your docker instance with “docker ps” (for me I am looking for container homeassistant/qemux86-64-homeassistant:2021.3.0
docker exec -it container# /bin/bash (where container# is the id of the homeassistant container)
vi /usr/src/homeassistant/homeassistant/components/minecraft_server/manifest.json
Google how to use vi, because I always forget
Change requirements of mcstatus to 5.1.1 version.
Do the same for the mcstatus entry in /usr/src/homeassistant/homeassistant/requirements.txt (not sure if this is needed
```
Hopefully this capability will be integrated into the built-in Minecraft Server Integration because the format should be almost identical

Place minecraft_server folder in your custom components

Add a new minecraft integration from Configuration->Integrations

You will have to re-add any existing java servers, as ths overwrites the built-in integration
