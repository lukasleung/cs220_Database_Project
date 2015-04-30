#!/usr/bin/python

print "Content-Type: text/html"
print  # a blank line must follow the last HTTP headers

import cgi
import cgitb
cgitb.enable()
import WebPages



if __name__ == "__main__":
    form = cgi.FieldStorage()
    
