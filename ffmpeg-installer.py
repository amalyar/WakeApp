from zipfile import ZipFile
import os
import ctypes

admin_check = ctypes.windll.shell32.IsUserAnAdmin()

win_user = os.getlogin()  # Checking the windows username that running logged in right now.
zipfile_path = 'C:/Users/' + win_user + '/Downloads/ffmpeg-N-100772-ga6d741920f-win64-gpl.zip'  # The default path to the zip file
while True:
    if admin_check == 0:
        print("I see you dont have enough permission i am quiting.")
        print("Please run this with admin privilege")
        break

    if os.path.exists(zipfile_path) is True:  # Checking if the zip exists.
        break

    if os.path.exists(
            zipfile_path) is False and admin_check == 1:  # checking if the file exists and if the user that run is an admin
        print(
            "I saw that you don't have the ffmpeg zip file downloaded, and it may make some problems with the audio.\n")
        ffmpeg_install = input("Do you want me to download it for you[y/n]: ")
        if ffmpeg_install == 'y' or ffmpeg_install == 'Y':
            print("Great!, starting the download")
            import wget

            wget.download(
                'https://github.com/BtbN/FFmpeg-Builds/releases/download/autobuild-2021-02-09-12-38/ffmpeg-N-101017-gcfcc36240f-win64-gpl.zip',
                zipfile_path)  # The github link for the zip file to download it.

        if ffmpeg_install == 'n' or ffmpeg_install == 'N':
            print('Ok but it may make some problems, you can also download it manual if you want :)')
            break

        with ZipFile(zipfile_path) as unzip:
            unzip.printdir()  # Prints what inside the zipfile.
            try:
                unzip.extractall(path='C:/')  # extract all the files from the zip
                os.renames('C:/ffmpeg-N-101017-gcfcc36240f-win64-gpl', 'C:/ffmpeg')


            except FileExistsError:
                counter = 0
                checking = os.listdir('C:/ffmpeg')
                real = ['bin', 'doc']
                for i in range(0, 2):
                    for checking in real:
                        if checking == real[i]:
                            counter = counter + 1
                if counter == 2:
                    break

        try:
            counter = 0
            checking = os.listdir('C:/ffmpeg')
            real = ['bin', 'doc']
            for i in range(0, 2):
                for checking in real:
                    if checking == real[i]:
                        counter = counter + 1
            if counter == 2:
                print('Download successfully ')
                break
            else:
                print('Something went wrong.')
                break

        except FileNotFoundError:
            print('Download Failed')
            break

        except PermissionError:  # windows may give permission error but it's probably already downloaded
            print('You got permission error, its most likely downloaded but make sure')
            break
