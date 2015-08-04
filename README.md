# clifont
###Install Google Fonts in one command


## Usage
 `sudo pip install -r requirements.txt`
 
 `sudo python clifont.py [font-name] [subset:latin|latin-ext|cyrillic] [styles:400|100|100italic|...]`
 
 With font names with space replace it with a +'
 
 e.g. PT+Sans
 
 *Used and tested in Ubuntu and Linux systems with /usr/share/fonts/ installation path*
   
 *For more names check https://www.google.com/fonts/*
 
### Examples:

 `sudo python clifont.py Roboto latin 400`

 `sudo python clifont.py Roboto latin,latin-ext 100,100italic`
 
 `sudo python clifont.py PT+Sans`
 

