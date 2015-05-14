import scraperwiki
import urllib2
import json, requests

api_url = "http://www.astro.com/wiki/astro-databank/api.php?"


apcontinue = ""
params = { 
	"format":"json", 
	"action":"query", 
	"list":"allpages", 
	"aplimit":"500" 
}
params.update({"apcontinue":apcontinue})


resp = requests.get(url=api_url, params=params)
results_json = resp.json()

apcontinue = results_json["query-continue"]["allpages"]["apcontinue"]

all_pages = results_json["query"]["allpages"]
for page in all_pages:
	page_id = page["pageid"]
	page_title = page["title"]
	