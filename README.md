# SimpleHue
💡Simple Python wrapper for interacting with Phillips Hue 

## Example code
```python

hue = SimpleHUE('http://your-hue-bridge-ip', 'some-username')
# Turn on the light with ID 1 
hue.turn_on(1)
# Turn off the light
hue.turn_off(1)
# Set the colors of a light (id, saturation, brightness, hue)
hue.set_color(1, 254, 254, 10000)
```

# FAQ

## How do I get a username?
Check out Phillip Hue's [Getting started](http://www.developers.meethue.com/documentation/getting-started) guide 

## How do I find the Hue Bridge IP?
Log into your router and find the IP for the hostname 'phillips-hue'. You could also use an app like [Fing](https://geo.itunes.apple.com/dk/app/fing-network-scanner/id430921107)


