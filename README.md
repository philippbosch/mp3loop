mp3duration
===========

A simple web service that returns the duration of an MP3 file given as a URL


### Installation

```shell
$ git clone https://github.com/philippbosch/mp3duration.git
$ cd mp3duration
$ heroku create your-app-name
$ heroku config:set LD_LIBRARY_PATH=/app/.heroku/python/lib
$ git push heroku master
```


### Usage

[`http://mp3duration.herokuapp.com/?url=http://audio-dummies.s3.amazonaws.com/loremipsum.mp3`](http://mp3duration.herokuapp.com/?url=http://audio-dummies.s3.amazonaws.com/loremipsum.mp3)


### Output

```json
{
  "seconds": "34.115918"
}
```
