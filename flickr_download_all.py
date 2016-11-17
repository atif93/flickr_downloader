#!/usr/bin/env python

import urllib
import sys
import os
import flickrapi
import xml.etree.ElementTree as ET


api_key = u'your-api-key'
api_secret = u'your-api-secret'

nArguments = 3
usageString = "usage: python flickr_download.py <user_id> <access_type>"
download_folder = "flickr_downloads"

if len(sys.argv)!= nArguments:
	print usageString	
	sys.exit()
elif not sys.argv[2] == "private" and not sys.argv[2] == "public":
	print "Error: access_type should be either public or private"
	sys.exit()
else:
	user_id = sys.argv[1]
	access_type = sys.argv[2]
		
flickr = flickrapi.FlickrAPI(api_key, api_secret)
if access_type == "private":
	flickr.authenticate_via_browser(perms='read')	

# create the download directory if not already present
if not os.path.exists(download_folder):
	os.makedirs(download_folder)

# getting all the files of the user
setsXML = flickr.people.getPhotos(user_id=user_id)

if setsXML.attrib['stat'] == 'ok':
	photos = setsXML.findall('.//photo')

	# for each file
	for photo in photos:
		print
		print "             |"
		print "Downloading \|/ "
		
		file_id = photo.attrib['id']
		
		sizesXML = flickr.photos.getSizes(photo_id=file_id)
		original_size = sizesXML.find('.//size[@label="Original"]')

		file_url = original_size.attrib['source']
		file_name = file_url.split('/')[-1]

		# store the metadata of the file
		metadata_file = open(download_folder + "/" + file_name.split('.')[-2] + '.xml','w')
		metadata_file.write(ET.tostring(photo, encoding='utf8', method='xml'))
		metadata_file.close()

		print file_name
		print

		# downloading the file
		urllib.urlretrieve(file_url, download_folder + "/" + file_name)
else:
	print "Flickr error"