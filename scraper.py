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

for x in range(0, 100):
	params.update({"apcontinue":apcontinue})
	resp = requests.get(url=api_url, params=params)
	results_json = resp.json()
	apcontinue = results_json["query-continue"]["allpages"]["apcontinue"]
	all_pages = results_json["query"]["allpages"]
	for page in all_pages:
		data = {}
		data = {"id": page["pageid"], "page_id": page["pageid"], "page_title": page["title"]}
		data["id"] = page["pageid"]
		data["page_id"] = page["pageid"]
		data["page_title"] = page["title"]
		scraperwiki.sqlite.save(unique_keys=['id'], data=data, table_name="data")
		pass
	if not apcontinue:
		break
	pass


