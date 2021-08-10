from PIL import Image
from PIL.ExifTags import TAGS
from termcolor import colored

print(colored("""

 _         _____  ___    ___           ___    _____  _____  ___    _____  _____  _____ 
(_)/'\_/`\(  _  )(  _`\ (  _`\ /'\_/`\(  _`\ (_   _)(  _  )(  _`\ (  _  )(_   _)(  _  )
| ||     || (_) || ( (_)| (_(_)|     || (_(_)  | |  | (_) || | ) || (_) |  | |  | (_) |
| || (_) ||  _  || |___ |  _)_ | (_) ||  _)_   | |  |  _  || | | )|  _  |  | |  |  _  |
| || | | || | | || (_, )| (_( )| | | || (_( )  | |  | | | || |_) || | | |  | |  | | | |
(_)(_) (_)(_) (_)(____/'(____/'(_) (_)(____/'  (_)  (_) (_)(____/'(_) (_)  (_)  (_) (_)
                                                                                                                                                                                                                                                                                                                                                                                                                                                                 
\n""","green"))
print(colored("ÇðÐêÐ ß¥ Måårï-Krï§h \n","magenta"))

print(colored("[+] Exif Image Metadata...","red"))
print(colored("[+] Enter the path of the image....","red"))
print('\n')
imagename = input(colored("Enter the image path: ","blue"))
print("Image Metadata results for",imagename)
print('\n')
image = Image.open(imagename)
exifdata = image.getexif()
for tag_id in exifdata:
    tag = TAGS.get(tag_id, tag_id)
    data = exifdata.get(tag_id)
    if isinstance(data, bytes):
        data = data.decode()
    print(colored(f"{tag:25}: {data}","green"))