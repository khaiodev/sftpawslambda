import pysftp as sftp

FTP_HOST = "valueFTP_HOST"
FTP_USER = "valueFTP_USER"
FTP_PASS = "valueFTP_PASS"
FTP_PORT = 222

cnopts = sftp.CnOpts()
cnopts.hostkeys = None

with sftp.Connection(host=FTP_HOST, port=FTP_PORT, username=FTP_USER, password=FTP_PASS, cnopts=cnopts) as sftp:
   print("Connection succesfully stablished ... ")
   sftp.cwd('/export/home/38225-teste/htdocs/')  # Switch to a remote directory
   directory_structure = sftp.listdir_attr() # Obtain structure of the remote directory

for attr in directory_structure:
   print(attr.filename, attr)
