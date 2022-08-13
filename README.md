# Constellations
A web site for guessing constellations based on an image randomly rotated.

## Background
I want to be better at identifying the constellations on the night sky,
so I made this litte app turning it into a game. As of yet, there are
only constellations in the nothern hemisphere, and still not all of them.

# Run
There is a `docker-compose.yml` file, so simply run
```bash
$ git clone git@github.com:DanielAndreasen/constellations.git
$ cd constellations
$ docker-compose up -d
```
and visit `http://localhost:5003`.

# Settings
If it is a bit too complicated (or not challenging enough) with 5 options, then
change the `n = 5` in the `app.py` before running `docker-compose up -d`.

# Side note
I am not a date scientist by trade, and this is just a little project I made
in my spare time. I will greatly appreciate any feedback on the technical part,
as well as any suggestions.
