from bs4 import BeautifulSoup
import urllib
import sys, getopt

def main(argv):
	url = ''
	save = ''
	try:
		opts, args = getopt.getopt(argv,"hi:s:",["url=","save="])
	except getopt.GetoptError:
		print 'scraper.py -i <imageurl> -s <savefilename>'
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-h':
			print 'scraper.py -i <imageurl> -s <savefilename>'
			sys.exit()
		elif opt in ("-i", "--url"):
			url = arg
		elif opt in ("-s", "--save"):
			save = arg
	print 'URL : "', url
	print 'Save File Name : ', save
	r=urllib.urlopen(url).read()
	soup=BeautifulSoup(r)
	img=soup.find_all("meta",property="og:image")
	imgurl=img[0]["content"]
	urllib.urlretrieve(imgurl, save)

if __name__ == "__main__":
	main(sys.argv[1:])