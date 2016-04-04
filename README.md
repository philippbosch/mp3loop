mp3loop
=======

A simple web service that creates an MP3 file of a given length that is the
result of looping another MP3 file as many times as necessary.


### Installation

```shell
$ git clone https://github.com/philippbosch/mp3loop.git
$ cd mp3loop
$ heroku create your-app-name
$ heroku config:set LD_LIBRARY_PATH=/app/.heroku/python/lib
$ git push heroku master
```


### Usage

[http://your-app-name.herokuapp.com/?duration=600](http://mp3loop.herokuapp.com/?duration=600)

Replace `audio.mp3` in the root directory with the file you want to loop.
