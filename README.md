# Blame

Repository containing info for the blame program. Blame provides secure password phrases for any service you use. 

## Getting Started

These instructions will get you a copy of the project up and running on your local machine. See prerequisites and installing for notes on how to setup the software. 

It is worth noting that the Blame script curently only supports nix systems, although this does not mean you can not run Blame itself on Windows. The python file is availible to download and you can run the python file from there. 

```THE PROJECT HAS BEEN RENAMED TO BLAME, SOME OF THE FILES MAY STILL BE NAMED DIFFERENTLY```

### Prerequisites

First make sure that you have Python 2.7 installed. You can either head over to python.org to install it or get it through the terminal.


wget and install the file
```
wget https://www.python.org/ftp/python/2.7.13/Python-2.7.13.tgz
```

### Download and Set Up 

To Download the program go to the top of the page and click on the goo.gl link, this will bring you to a mega page with the zip file. Download it. 

After you have downloaded the zip extract it. You should now have a folder with the passgen files in it. Inside the folder are four files README.txt, passgen.py, passgenscript, and passwords.txt. First move the passgen folder to your home folder. After open the passgen folder and then open the passgenscript file. Go to the 3rd line of the script file and remove the # symbol. Then replace the text 'user' with your username, eg. cd /home/nax/passgen/. After you have edited the script file copy it by right clicking it and paste into your home folder. Next open a terminal window and allow the file to be run as excutable.

Do this by using chmod
```
chmod +x passgen
```
After you have done this you also have to allow the python file to be run as an executable file. 

First change into the passgen folder by using cd (note: replace user with your username for the cd command)
```
cd /home/user/passgen/
chmod +x passgen.py
```
After you have done this you are now ready to run the program!

```
./passgenscript
```

