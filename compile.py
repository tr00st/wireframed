#!/usr/bin/env python
try:
    from urllib.parse import quote
except ImportError:
    from urllib import quote

def main():
    bookmarklet_file = open('bookmarklet.js', mode='r')
    bookmarklet = bookmarklet_file.read()
    bookmarklet = "javascript: {}".format(quote(bookmarklet, safe=""))
    print(bookmarklet)

if __name__ == "__main__":
    main()
