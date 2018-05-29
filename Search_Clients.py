import urllib.request
import json
import pprint

class GoogleClient():
    def search(self,search):
        google_api = "https://www.googleapis.com/customsearch/v1?key=AIzaSyA2r3oK7Fxr8GiKKsE9D7hGxoJRtdQCnKo&cx=014170932909531414778:kcyx0xaz-60&q="+search+""
        request = urllib.request.urlopen(google_api)
        data = json.loads(request.read().decode('utf-8'))
        #pp = pprint.PrettyPrinter(indent=4)
        #pp.pprint(data)
        items = data.get('items')
        #pp.pprint(items)
        try:
            item = items[0]
        except (IndexError, ValueError, TypeError):
            item = "null"
        if item!="null":
            google_url = item.get('formattedUrl')
            google_details = item.get('snippet')
        else:
            google_url = "No Response From Search Engine"
            google_details = "No Response from Search Engine"
        return [google_url,google_details]

class DdgoClient():
    def search(self,search):
        ddg = "https://api.duckduckgo.com/?q="+search+"&format=json"
        request = urllib.request.urlopen(ddg)
        data = json.loads(request.read().decode('utf-8'))
        items = data.get('RelatedTopics')
        try:
            item = items[0]
        except (IndexError, ValueError, TypeError):
            item = "null"
        if item != "null":
            ddg_url = item.get('FirstURL')
            ddg_details = item.get('Text')
        else:
            ddg_url = "No Response From Search Engine"
            ddg_details = "No Response from Search Engine"
        return [ddg_url, ddg_details]


