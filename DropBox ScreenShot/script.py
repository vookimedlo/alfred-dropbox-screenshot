import os
import sys
import urllib
from AppKit import NSPasteboard, NSArray

def clipboard(link):
    pb = NSPasteboard.generalPasteboard()
    pb.clearContents()
    array = NSArray.arrayWithObject_(link)
    pb.writeObjects_(array)


if len(sys.argv) != 5:
    print "Not enough arguments" 
    sys.exit(1)

# File path
input_file = str(sys.argv[1])

# UID
db_uid = str(sys.argv[2])

# Dropbox public dir 
db_public = str(sys.argv[3])

# Dropbox directory (final dir: $db_public/$db_directory) 
db_directory = str(sys.argv[4])



# quit if directory is moved
if os.path.isdir(input_file):
    sys.exit(1)

# Get the name of the file without full path
filename = input_file.split('/')[-1]

# move the file from its location to the Dropbox Public Folder
os.rename(input_file, os.path.join(db_public, db_directory, filename))
print "Screenshot moved to Dropbox folder"

filename = urllib.pathname2url(filename)
public_link = 'http://dl.dropbox.com/u/%s/%s/%s' % (db_uid, db_directory, filename)
clipboard(public_link)
print "Link for sceenshot copied to clipboard"
