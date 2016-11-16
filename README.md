- Create an app and get an API key here: https://www.flickr.com/services/apps/create/

- Put your API key and API secret inside the flickr_download.py script (line 11 and line 12).

- This script uses an API Kit provided here: https://github.com/sybrenstuvel/flickrapi/

- To install this kit, download the project from the url provided and run the following:
python setup.py install

- Now, the script can be run as follows:
python flickr_download.py <user_id> <access_type>

<user_id> is the NSID of the user account from which the files will be downloaded from. Can be seen in the flickr url of the photos page of the user (https://www.flickr.com/photos/<user_id>/).

<access_type> Can be private or public. No authentication is required for downloading public files of any user. Authentication is required for downloading the private files (files which are in camera roll but not in photostream).
When private access_type is chosen, a browser window opens asking the user to authorize the app. This authorization is shown for the user who is logged in at that time on flickr in the browser (not necessarily for the user_id provided). Therefore, you should logout of the flickr account (if it is different from the one for which user_id is provided) from the browser before running the script.
This kind of authorization only needs to be done once for a particular user_id.

- The files are stored in folders corresponding to albums in Flickr. Each folder is named as the folder_id which was returned by the Flickr API. Each folder has a metadata file which contains the properties of the corresponding album as returned by the Flickr API in XML format (this includes the folder name). 

- Each file is named in the following format: 
<originalFilename>_<fileID>.<extension>
Similar to folders each file has a metadata file which contains the properties of that file (this includes the original file name). 