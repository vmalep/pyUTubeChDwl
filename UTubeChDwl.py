#!/usr/bin/python

# A python program intended to download all a videos of a given YouTube channel in the current folder.

#import mechanize
#import csv
import urllib, re

#print(urllib.request.urlopen(channel_url).getcode()) AttributeError: 'module' object has no attribute 'request'

mylines = ""

while True:
    try:
        channel_url = raw_input("Please enter the YoutTube channel url here ('exit' to stop): ")
        if channel_url == "exit": break
        if channel_url[-6:len(channel_url)] != "videos":
            channel_url += "/videos"
        if channel_url[0:4] != "http":
            channel_url = "https://" + channel_url
        print "reading " + channel_url
        mylines = urllib.urlopen(channel_url).readlines()
        print "done"
        break
    except:
        print "Oops!  That was not a valid url.  Try again..."

#print mylines

count = 0
for item in mylines:
    count += 1
    video_id = re.findall("['gridVideoRenderer']", item)
#    print("Original string: ",text)
    if video_id: print video_id

print count
    #if 'gridVideoRenderer' in item:
    #    count += 1
    #    print count
    #    print item
    #    #print item[item.index("videoId"):]
