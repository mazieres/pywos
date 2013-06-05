# PyWoS

This Python script takes in input a folder with [RIS](http://goo.gl/onNO6)-formatted files from a [ISI Web of Science](http://thomsonreuters.com/web-of-science/) (WoS) corpus, and returns a nicely formatted python dictionnary.

It tries to format every entries in a python-friendly manner.

## Dependencies

Uses [gris](https://pypi.python.org/pypi/gris) module.

    sudo easy_install gris

## Usage

    import WoS
    wos = Wos('path/to/the/folder/with/RIS/Files')
