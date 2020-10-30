# Codeforces rating

Codeforces is large platform for training in olympiadic programming.
This project automizes process of making rating for groups in Codeforces.
Project is realized using Codeforces API and Google Drive API. 
* It fetches information from successes of group's participants.
* Forms rating in excel format. 
* And then it posts it on your Google Drive.


Firstly, run specify_meta_information.py and type information you will be asked:
* Group name
* Desirable name for eventual xlsx file
* API_KEY from Codeforces platform API
* SECRET from Codeforces platform API

Note, Group name can be any of your liking, but in all your group's competetions you are to make English description as follows:
Group:YOUR_GROUP_NAME 

It is done due to reason that Codeforces lacks API that works with groups.

