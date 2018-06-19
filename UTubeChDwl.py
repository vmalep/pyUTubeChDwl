#!/usr/bin/python

# A python program intended to download all a videos of a given YouTube channel.
# Currently, this script IS NOT WORKING PROPERLY (work in progress).
# The authors of the script (still learning python programming) cannot be taken responsible for any damage it may produce if you execute it.

#import mechanize
#import csv
import urllib, re

#print(urllib.request.urlopen(channel_url).getcode()) AttributeError: 'module' object has no attribute 'request'

# The regex substring to search for in the source page:
substr = '\?v\=[A-Za-z0-9]+'

mylines = ""
count = 0
video_id = []
all_lines = ""

# Asking for the url
#channel_url = raw_input("Please enter the YoutTube channel url here ('exit' to stop): ")
channel_url = "https://www.youtube.com/channel/UCXbWsGV_cjG3gOsSnNJPVlg/videos"
# Checking if the url start with https and ends with "videos"
#if channel_url[-6:len(channel_url)] != "videos":
#    channel_url += "/videos"
#if channel_url[0:4] != "http":
#    channel_url = "https://" + channel_url

print "reading " + channel_url

# test if the url works
#try:
mylines = urllib.urlopen(channel_url).readlines()
print "done: " + str(len(mylines)) + " lines copied"
#except:
#    print "Oops!  That was not a valid url.  Try again..."

#print mylines

# Concatenate Read each line and if it matches the substring, add it to the video_id dict
for item in mylines:
    all_lines += item
#print all_lines

video_id = re.findall(substr, all_lines)
print video_id

#for i in video_id[]
#    print i

