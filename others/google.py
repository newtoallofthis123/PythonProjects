#! /usr/bin/env python3

# Name of the Project : ddg.py
# Written by NoobScience : https://github.com/newtoallofthis123
# Modules Used : sys, urllib, webbrowser 

"""Script to search with Duckduckgo

Usage:
    python3 ddg.py [search terms]
"""

# importing necessary Modules
import sys
import urllib.parse
import webbrowser

# Defining a funtion main
def main(args):
    def quote(arg):
        if ' ' in arg:
            arg = '"%s"' % arg
        return urllib.parse.quote_plus(arg)

    # Getting the argument used and applying usage to duckduckgo
    qstring = '+'.join(quote(arg) for arg in args)
    url = urllib.parse.urljoin('https://www.duckduckgo.com/search', '?q=' + qstring)
    webbrowser.open(url)

# running the function main
if __name__ == '__main__':
    main(sys.argv[1:])

# Enjoy
