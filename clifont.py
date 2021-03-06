import sys, re
"""try:
	from urllib.parse import quote as urlencode
except:
	from urllib import quote as urlencode
"""


RE_HTTP = re.compile("(http[s]?:[/][/][^\\) ]+)", re.I|re.DOTALL|re.M)

try:
	import requests
	import wget
	import shutil
except:
	print("You should install libraries. Try:\n\tpip install  -r requirements.txt\n")
	exit(-1)

def getFontUrls(family, subset, style):
	return getFontUrlsWithUserAgent(family, subset, style, "ttf")

def getFontUrlsWithUserAgent(family, subset, style, agent):
	family = family.replace(' ', '+')
	subset = subset.replace(' ', '+')
	style = style.replace(' ', '+')
	headers = {"User-Agent": agent}
	r = requests.get("http://fonts.googleapis.com/css?family={0}:{2}&subset={1}".format(family, subset, style), headers=headers)
	urls = re.findall(RE_HTTP, r.text)

	return urls

if __name__ == "__main__":
	if len(sys.argv) < 2 or len(sys.argv) > 5:
		print("You should use:\n\tsudo python {} font-name [subset:latin|latin-ext|cyrillic] [styles:400|100|100italic|...] ".format(__file__))
		print("e.g.\n\tsudo python {0} Roboto latin 400\n\tpython {0} Roboto latin,latin-ext 100,100italic\n\n".format(__file__))
		print("Possible font names may be, \"Pt Sans\",Roboto,Ubuntu,...")
		print("On font name with spaces replace it with a +")
		print("e.g. \n\tsudo python clifont.py Noto+Sans")
		print("You can check further names at: https://www.google.com/fonts/")
		exit(-2)
	else:
		family = sys.argv[1]
		subset = "latin"
		style  = "400"
		if len(sys.argv) == 3:
			subset = sys.argv[2]
		elif len(sys.argv) == 4:
			style = sys.argv[3]
		elif len(sys.argv) == 5:
			format = sys.argv[4]

		if (format == "all"):
			exit(0)
		else:	
			font_url = "".join(getFontUrls(family, subset, style))
			print(font_url)
			font = wget.download(font_url)
			font = "".join(font)
			shutil.move(font, "/usr/share/fonts")			 
			exit(0)


