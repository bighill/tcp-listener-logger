# tcp-listener-logger #

Very simple tool to listen on a TCP port and log incoming messagas.

## requirements ##

python 2.x

## usage ##

1. Start the listener at a command line terminal:
* `cd tcp-listener-logger`
* `python tcp-listener-logger.py`

2a. Configure an application to send data to the localhost on port 8888

2b. Or test locally with `nc`. In another terminal, use something like this:
`echo 'important message' | nc localhost 8888`

3. Results are logged in log.txt: `tail -f log.txt`