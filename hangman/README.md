## Synopsis

This is popular Hangman game. It invokes REST API to download a word dictionary, picks up a word and then lets player guess the work correctly.
Player can enter the game in either kid or adult mode. Kid mode generates the smaller words (3 or 4 letters).

## Code Example


## Motivation

Fun game to be pythonic

## Installation
Download and run locally. You need to have requests API. Depending which version of Python you are using, you will have to install the module.
E.g. download and install pip first (if not yet installed):
$ curl -O https://bootstrap.pypa.io/get-pip.py
$ sudo python3 get-pip.py
or
$ sudo easy_install pip
After installing pip, install requests module.
$ pip install requests //python 2
$ pip3 install requests //python 3



## API Reference

requests API invokes REST API. Data comes in bytes and is decoded to UTF-8.


## License
Navin Kumar
