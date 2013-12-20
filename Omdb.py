#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import sys
import urllib2

"""
Class to get a film's information from imdb.com using the omdapi.com site.
Written by Paul Kelly <nRage>.
"""

class GetInfo(object):
    """Uses unique imdb id to get the film's details."""
    def __init__(self, imdbID):
        try:
            self.data = json.load(urllib2.urlopen('http://www.omdbapi.com/?i=%s' % (imdbID)))
        except urllib2.URLError:
            print 'Error connecting to omdbapi.com'
            sys.exit(1)

    def getTitle(self):
        """Returns film title."""
        return self.data['Title']

    def getPlot(self):
        """Returns film plot."""
        return self.data['Plot']

    def getRating(self):
        """Returns film rating."""
        return self.data['imdbRating']

    def getReleaseDate(self):
        """Returns film release date."""
        return self.data['Released']

    def getReleaseYear(self):
        """Returns film release year"""
        return self.data['Year']

    def getGenre(self):
        """Returns film genre."""
        return self.data['Genre']

    def getDirector(self):
        """Returns film director."""
        return self.data['Director']

    def getRuntime(self):
        """Returns film runtime."""
        return self.data['Runtime']

    def getWriter(self):
        """Returns film writer."""
        return self.data['Writer']

    def getActors(self):
        """Returns some of the films main actors."""
        return self.data['Actors']

    def getCertification(self):
        """Returns film certification. E.g. 'R'."""
        return self.data['Rated']

    def getPosterLink(self):
        """Returns link for poster of film."""
        return self.data['Poster']

    def downloadPoster(self):
        """Download poster image."""
        if self.getPosterLink() == 'N/A':
            print 'Poster not available'
            return 0
        else:
            image = urllib2.urlopen(self.getPosterLink()).read()
            w = open(self.getTitle()[:-1] + self.getPosterLink()[-4:], "wb")
            w.write(image)
            w.close()
            return 1





