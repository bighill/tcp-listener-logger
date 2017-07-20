# tcp-listener-logger #

Very simple tool to listen on a TCP port and log incoming messagas.

## Requirements ##

python 2.x

## Usage ##

Start the listener at a command line terminal:
* `cd tcp-listener-logger`
* `python tcp-listener-logger.py`

Configure an application to send data to the host on port 8888.

Also you can test locally with `nc`. In another terminal, use something like this:
`echo 'important message' | nc localhost 8888`

Results are logged in log.txt: `tail -f log.txt`