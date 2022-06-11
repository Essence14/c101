import dropbox
class Transferdata:
    def __init__(self,accessToken):
        self.accessToken=accessToken
    def uploadFile(self,filefrom,fileto):
        dbx=dropbox.Dropbox(self.accessToken)
        with open(filefrom,"rb")as f:
            dbx.files_upload(f.read(),fileto)

def main():
    accessToken="sl.BJUQdp4EcZT1MXRAAvA19PTjJX5jh95UjszpjHuHOW62YOb_4vpQ_5Z-zVgBDuaSJZw9aiUhWIc0Y2LqaHQhl0dycGhXbhm6Qr-9uXQiOKAVj7nmgfxl-zb-iBxaPU5ie4LNpHPEVfAh"
    transferdata=Transferdata(accessToken)
    filefrom=input("enter the file path you want to tranfer")
    fileto=input("enter the full file path to upload items to dropbox")
    transferdata.uploadFile(filefrom,fileto)
    print("FILE HAS BEEN MOVED")


if __name__=="__main__":
    main()