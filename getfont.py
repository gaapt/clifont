import sys, re
"""try:
	from urllib.parse import quote as urlencode
except:
	from urllib import quote as urlencode
"""

__package__ = "google-get-font-name"
__author__ = "gaberpt@gmail.com"
__version__ = "1.0.0"
__license__ = "http://opensource.org/licenses/LGPL-3.0"

AGENT_STRS = {
	"eot":   "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; .NET CLR 1.1.4322)",
	"woff":  "Mozilla/5.0 (MSIE 9.0; Windows NT 6.1; Trident/5.0)",
	"woff2": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.111 Safari/537.36",
	"ttf":   "%s %s %s" % (__package__, " Agent ", __version__),
	"svg":	 "Mozilla/5.0 (iPad; U; CPU OS 3_2 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Version/4.0.4 Mobile/7B334b Safari/531.21.10"
}

RE_HTTP = re.compile("(http[s]?:[/][/][^\\) ]+)", re.I|re.DOTALL|re.M)

try:
	import requests
	import wget
	import shutil
except:
	print("You should install libraries. Try:\n\tpip install requests\n")
	exit(-1)

def getFontUrls(family, subset, style):
	return getFontUrlsWithUserAgent(family, subset, style, AGENT_STRS["ttf"])

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
		print("You should use:\n\tpython {} font-name [subset:latin|latin-ext|cyrillic] [styles:400|100|100italic|...] [file-type:all|{}]".format(__file__, '|'.join(AGENT_STRS.keys())))
		print("e.g.\n\tpython {0} Roboto latin 400\n\tpython {0} Roboto latin,latin-ext 100,100italic\n\n".format(__file__))
		print("Possible font names may be, \"Pt Sans\",Roboto,Ubuntu,...")
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


