#!/usr/bin/env python

import urllib
import base64
from xml.dom import minidom
import sys
import os
import flickrapi


api_key = u'c3b794dbbff7715cbab94fc40b8ac720'
api_secret = u'8dd1d6343917e619'
#api_key = u'your-api-key'
#api_secret = u'your-api-secret'

nArguments = 3
usageString = "usage: python flickr_download.py <user_id> <access_type>"

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

setsXML = flickr.photosets.getList(user_id=user_id)

if setsXML.attrib['stat'] == 'ok':
	sets = setsXML.find('photosets').findall('photoset')

	for set in sets:
		print
		print "             |"
		print "Downloading \|/ "
		print set.find('title').text
		print

		id = set.attrib['id']
		if not os.path.exists(id):
			os.makedirs(id)
		photosXML = flickr.photosets.getPhotos(photoset_id=id)
		photos = photosXML.find('photoset').findall('photo')

		for photo in photos:
			photo_id = photo.attrib['id']
			
			sizesXML = flickr.photos.getSizes(photo_id=photo_id)
			sizes = sizesXML.find('sizes').findall('size')

			for size in sizes:
				if size.attrib['label'] == 'Original':
					photo_url = size.attrib['source']

			photo_name = photo_url.split('/')[-1]
			print "		" + photo_name
			
			urllib.urlretrieve(photo_url, id + "/" + photo_name)
else:
	print "Flickr error"