#!/usr/bin/env python3

'''
Parse feeds based on search from subreddit        
Author: G3Dx5                                                   
Date: SEP2022                                              
Version:  1.1                                               
'''

import feedparser
import sys
import time


# Set command line arguments for the subsequent search term
if len(sys.argv) != 2:
    print('ERROR: You must specify a search term eg: python3 reddParseFunc.py <searchterm>')
    sys.exit(0)

redprefix = 'http://www.reddit.com/r/'
searterm = sys.argv[1]
exten = '.rss'

# Parse the feed. Subredit is '/r' by default, can be changed
r = feedparser.parse(redprefix+searterm+exten)
#print r.entries
print(r['feed']['title'])
print(r.feed.subtitle)

# Print out search time / date
print("\n")
print("=================================================")
print("Search Time:", time.strftime("%A %d %B %Y %I:%M %p"))
print("=================================================\n")

def runparse() -> None:
    count = 1
    if count % 100 == 1:
        for post in r.entries:
            print(post.title)
            print(post.link)
            print(post.date)
            try:
                print("Author:", post.author + "\n")
            except:
                continue
            count += 1

runparse()
