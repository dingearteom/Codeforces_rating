from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from meta import FILE_NAME_DISK

def load_google_drive():
    FILE_NAME_LOCAL = f"data/{FILE_NAME_DISK}.xlsx"

    gauth = GoogleAuth()
    gauth.LocalWebserverAuth()

    drive = GoogleDrive(gauth)

    file_list = drive.ListFile({'q': "'root' in parents and trashed=false"}).GetList()
    m = {}
    for file1 in file_list:
        m[file1['title']] = file1
        #print('title: %s, id: %s' % (file1['title'], file1['id']))

    if (FILE_NAME_DISK in m):
        file = m[FILE_NAME_DISK]
    else:
        file = drive.CreateFile()
    file.SetContentFile(FILE_NAME_LOCAL)
    file['title'] = FILE_NAME_DISK
    file.Upload()