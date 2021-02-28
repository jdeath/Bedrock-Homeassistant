# Bedrock-Homeassistant

Initial commit of a bedrock integration for homeassistant. Not easibly useable as built-in minecraft mcstatus must be updated to at least 5.1.1. I put in an issue. 
Hopefully this capability will be integrated into the built-in Minecraft Server because the format should be almost identical

Place bedrock folder in your custom components

For your configuration.yaml
```
Sensor:
- platform: bedrock
    url: '192.168.1.xx'
    port: '19132' #(port is not used right now, must be default)
```

For your lovelace
```
type: entities
entities:
  - entity: sensor.bedrock
    name: Users Online
    icon: 'mdi:account-multiple'
  - type: attribute
    name: MOTD
    entity: sensor.bedrock
    attribute: motd
    icon: 'mdi:message-text'
  - type: attribute
    name: Map
    entity: sensor.bedrock
    attribute: map
    icon: 'mdi:map'
  - type: attribute
    name: Game Mode
    entity: sensor.bedrock
    attribute: gamemode
  - type: attribute
    name: Latency
    icon: 'mdi:signal'
    entity: sensor.bedrock
    attribute: latency
  - type: attribute
    name: Protocol
    entity: sensor.bedrock
    attribute: protocol
    icon: 'mdi:numeric'
  - type: attribute
    name: Type
    entity: sensor.bedrock
    attribute: brand


```
