import os
import sys
import dropbox
from dropbox.files import WriteMode

# get an access token, local (from) directory, and Dropbox (to) directory
# from the command-line
access_token = "sl.BAAGe2g8pQG3X-saAzbC_-9n6yJTJZXpvvljajhlAuDQLP3g9Whq_8pjfVBvI7iL-4xOfpHOgcqOSz9BC1UfO87-6ejEz7KmvOGWMJxQ9wJeF0eaiyuHsZy1j3Tz0Sm7yteU8sy2Szc"
local_directory="pro"
dropbox_destination='/pro_dropbox/pro'


dbx = dropbox.Dropbox(access_token)
# enumerate local files recursively
for root, dirs, files in os.walk(local_directory):

    for filename in files:

        # construct the full local path
        local_path = os.path.join(root, filename)

        # construct the full Dropbox path
        relative_path = os.path.relpath(local_path, local_directory)
        dropbox_path = os.path.join(dropbox_destination, relative_path)

        
        with open(local_path, 'rb') as f:
            dbx.files_upload(f.read(), dropbox_path,mode=WriteMode("overwrite"))
print("folder has been moved")           