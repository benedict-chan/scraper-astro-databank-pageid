import scraperwiki
import urllib2
import json, requests
import pprint


def request_page_using_id ( page_id ):
	p_params = { 
	    "format":"json", 
	    "action":"query", 
	    "prop":"revisions", 
	    "rvprop":"content" 
	}
	p_params.update({"pageids":page_id})
	p_api_url = "http://www.astro.com/wiki/astro-databank/api.php?"
	resp = requests.get(url=p_api_url, params=p_params)
	single_data = resp.json()
	json_str = json.dumps(single_data)
	return json_str


api_url = "http://www.astro.com/wiki/astro-databank/api.php?"
#http://www.astro.com/wiki/astro-databank/api.php?format=json&action=query&list=allpages&aplimit=500&apcontinue=Woodbridge%2C%20Todd

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
	try:
		results_json = resp.json()
		all_pages = results_json["query"]["allpages"]
		apcontinue = results_json["query-continue"]["allpages"]["apcontinue"]
	except Exception, e:
		apcontinue = "" # break the loop later
	for page in all_pages:
		data = {}
		data = {"id": page["pageid"], "page_id": page["pageid"], "page_title": page["title"]}
		data["id"] = page["pageid"]
		data["page_id"] = page["pageid"]
		data["page_title"] = page["title"]
		data["json_str"] = request_page_using_id(page["pageid"])
		scraperwiki.sqlite.save(unique_keys=['id'], data=data, table_name="data")
		pass
	if not apcontinue:
		break
	pass


