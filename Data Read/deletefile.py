#!/usr/bin/python
import os

## Get input ##
myfile= raw_input("Enter file name to delete: ")

## Try to delete the file ##
try:
    os.remove(myfile)
	f = open(myfile, "w+")
	f.write("Place text here")
	f.close()
	
except OSError as e:  ## if failed, report it back to the user ##
    print ("Error: %s - %s." % (e.filename, e.strerror))