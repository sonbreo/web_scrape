from WebsiteParse import WebsiteParse
import pprint

url = 'https://www.gumtree.com.au/s-video-games-consoles/melbourne/nintendo+switch+console/k0c18459l3001317r50'
temp = WebsiteParse(url)

keywords = 'nintendo switch console'
# pprint.pprint(temp.gumtree_parse(keywords))
temp.gumtree_parse(keywords)
