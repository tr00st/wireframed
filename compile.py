#!/usr/bin/env python
try:
    from urllib.parse import quote
except ImportError:
    from urllib import quote

def main():
    bookmarklet_file = open('bookmarklet.js', mode='r')
    bookmarklet = bookmarklet_file.read()
    bookmarklet = "javascript: {}".format(quote(bookmarklet, safe=""))
    output_file = open('compiled.js', mode='w')
    output_file.write(bookmarklet)
    print("New bookmarklet output to compiled.js")

if __name__ == "__main__":
    main()
