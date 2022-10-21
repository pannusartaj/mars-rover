# Mars Rover with Python
# How it works ?
The python program run inside the python docker image. 

While building, unit test will run, <b>build will fail in case test cases fail</b>.

# Running test cases in local
```bash
$ python3 -m unittest
```
# How it runs

In compose file, it will run the inputs (input.json) given to the program.

More inputs can be added by editing the above said json file.

```bash
$ docker-compose up
```
