# Bedrock-Homeassistant

Core-2021.3.1 or later required

[![Stargazers repo roster for @jdeath/Bedrock-Homeassistant](https://git-lister.onrender.com/api/stars/jdeath/Bedrock-Homeassistant?limit=30)](https://github.com/jdeath/Bedrock-Homeassistant/stargazers)

## Installation

### HACS (prefered)

1. Add this repository to HACS as an integration: https://github.com/jdeath/Bedrock-Homeassistant
1. Install the integration
1. Restart your instance

### Manual (not needed if you use HACS)

1. Copy the content of `custom_components/minecraft_server` into `/config/custom_components/minecraft_server` on your system.
1. Restart your instance


Add a new minecraft integration from Configuration->Integrations
Existing Java sensors should be auto migrated to updated integration
Add any Bedrock servers or Java severs. Be sure to specify Server Type (Java or Bedrock) correctly in integration setup

### Old Instructions
```
Place minecraft_server folder in your custom components
Restart homeassistant
Add a new minecraft integration from Configuration->Integrations
Existing Java sensors should be auto migrated to updated integration
Add any Bedrock servers or Java severs. Be sure to specify Server Type (Java or Bedrock) correctly in integration setup
```

Not needed with core-2021.3.1 or later:

Not easibly useable as built-in minecraft mcstatus must be updated to at least 5.1.1. I put in an issue and it has been accepted into dev. 
```
ssh in developer mode or the host system
find your docker instance with “docker ps” (for me I am looking for container homeassistant/qemux86-64-homeassistant:2021.3.0
docker exec -it container# /bin/bash (where container# is the id of the homeassistant container)
vi /usr/src/homeassistant/homeassistant/components/minecraft_server/manifest.json
Google how to use vi, because I always forget
Change requirements of mcstatus to 5.1.1 version.
Do the same for the mcstatus entry in /usr/src/homeassistant/homeassistant/requirements.txt (not sure if this is needed
```


