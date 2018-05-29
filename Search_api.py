from flask_restful import Resource,reqparse
from Search_Clients import GoogleClient,DdgoClient


class SearchAPI(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('q',type=str,location = 'args')
        query = parser.parse_args()
        req = query.q
        print (query)
        print(req)
        search_str = req.replace(" ","+")
        print(search_str)
        g = GoogleClient().search(search_str)
        d = DdgoClient().search(search_str)
        return {
            "Query" : search_str,
            "Results" : {
                "Google": {
                "Url" : g[0],
                "Text" : g[1]
                },
                "DuckDuckGO" : {
                    "Url" : d[0],
                    "Text" : d[1]
                }
            }
        }
