#!/usr/bin/env python

import urllib
import base64
from xml.dom import minidom
import sys
import os
import flickrapi


api_key = u'c3b794dbbff7715cbab94fc40b8ac720'
api_secret = u'8dd1d6343917e619'

#flickr = flickrapi.FlickrAPI(api_key, api_secret, format = 'parsed-json')
flickr = flickrapi.FlickrAPI(api_key, api_secret)
#photos = flickr.photos.search(user_id='128418753@N06', per_page='10')
setsXML = flickr.photosets.getList(user_id='128418753@N06')

print setsXML.attrib['stat']
#title  = sets['photosets']['photoset'][0]['title']['_content']

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
		
	
#flickr.authenticate_via_browser(perms='read')