Title: Posting to Pushbullet with NodeMCU
Date: 2016-08-24 8:00
Modified: 2016-08-24 8:00
Category: Embedded Systems
Tags: lua, nodemcu, esp, pushbullet
Slug: nodemcu-pushbullet-notifiocation

With [NodeMCU HTTP Module](https://nodemcu.readthedocs.io/en/master/en/modules/http/) we can GET/POST/PUT/DELETE over HTTP(S), as well as customized requests. If you ever used any other programming language you know how easy is to make an HTTP request.

Today, we're going to call [Pushbullet](https://www.pushbullet.com) API. So, what's Pushbullet?

> Pushbullet bridges the gap between your phone, tablet, and computer, enabling them to work better together. From seeing your phone's notifications on your computer, to easily transferring links, files, and more between devices.

Pushbullet is a great tool to get notifications on your phone. Let's assume we have a fire sensor at home. If the fire sensor detects something, it would be good to be notified if we aren't at home. We can do this over Pushbullet or another platform.

The sample code below shows how to send the current IP.

```lua
-- your setup.
PUSHBULLET_TOKEN = ''
WIFI_SSID = ''
WIFI_PASSWORD = ''

wifi.setmode(wifi.STATION)

-- on connect send the current IP to pushbullet.
wifi.sta.eventMonReg(wifi.STA_GOTIP, function()
    ip = wifi.sta.getip()

    http.post('https://api.pushbullet.com/v2/pushes',
              'Content-Type: application/json\r\nAccess-Token: '.. PUSHBULLET_TOKEN ..'\r\n',
              '{"body":"IP: '.. ip ..'", "title":"ESP Connected", "type":"note"}',
    function (code, data)
        -- print the response code. 200 if success.
        print(code)
    end)
end)

-- configure wifi and connect.
wifi.sta.config(WIFI_SSID, WIFI_PASSWORD)
wifi.sta.connect()
```

This is a very simple example but is good enough for testing purpose.

**Reference**

- [Pushbullet API](https://docs.pushbullet.com/)
- [NodeMCU HTTP Module](https://nodemcu.readthedocs.io/en/master/en/modules/http/)
