# SOA Messenger


### Usage:

To start/stop the project, run:
```bash
./run up
./run down
```
This will build images and start intances with ports:
- 8000 : talkative web server
- 80 and 443: receiver webserver

In browser, open talkative web server at `http://localhost:8000`
From this, we can test sending message to receiver server:
```bash
curl -k --data "text=foo-bar" https://localhost:443/
```
We should see the message "foo-bar" appears on talkative web page.
