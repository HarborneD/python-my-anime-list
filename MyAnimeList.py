import requests

class MyAnimeListAPI(object):
    """docstring for MyAnimeListAPI"""
    def __init__(self, username, password):
        super(MyAnimeListAPI, self).__init__()
        self.username = username
        self.password = password
        self.credentials = (username,password)

        self.my_al_endpoint = "https://myanimelist.net/api/"
        self.my_al_search_endpoint = self.my_al_endpoint + "%s/search.xml"

        self.mal_add_anime_endpoint = self.my_al_endpoint + "animelist/add/%s.xml"
        self.mal_update_anime_endpoint = self.my_al_endpoint + "animelist/update/%s.xml"
        self.mal_delete_anime_endpoint = self.my_al_endpoint + "animelist/delete/%s.xml"

        self.mal_add_manga_endpoint = self.my_al_endpoint + "mangalist/add/%s.xml"
        self.mal_update_manga_endpoint = self.my_al_endpoint + "mangalist/update/%s.xml"
        self.mal_delete_manga_endpoint = self.my_al_endpoint + "mangalist/delete/%s.xml"

        self.anime_status_dict = {"watching":1, "completed":2, "onhold":3, "dropped":4, "plantowatch":6 }
        self.manga_status_dict = {"reading":1, "completed":2, "onhold":3, "dropped":4, "plantoread":6 }


    def PerformSearch(self,query_string,anime_search=True):
        if(anime_search):
            search_type = "anime"
        else:
            search_type = "manga"

        query = {"q":query_string}

        request_string = self.my_al_search_endpoint % search_type

        response = requests.get(request_string, params=query , auth=self.credentials)

        return response.content



    def AddUpdateAnime(self,anime_id,add=True,status=6,episode="",score=""):
        xml = {"data":self.ProduceAnimeDataXML(status,episode,score)}

        if(add):
            request_string = self.mal_add_anime_endpoint % str(anime_id)
        else:
            request_string = self.mal_update_anime_endpoint % str(anime_id)

        response = requests.post(request_string, data=xml , auth=self.credentials)
        print(response.status_code)
        return response.content


    def DeleteAnime(self,anime_id):
        request_string = self.mal_delete_anime_endpoint % str(anime_id)

        response = requests.post(request_string , auth=self.credentials)

        return response.content



    def AddUpdateManga(self,manga_id,add=True,status=6,chapter="",volume="",score=""):
        xml = {"data":self.ProduceMangaDataXML(status,chapter,volume,score)}

        if(add):
            request_string = self.mal_add_manga_endpoint % str(manga_id)
        else:
            request_string = self.mal_update_manga_endpoint % str(manga_id)

        response = requests.post(request_string, data=xml , auth=self.credentials)
        print(response.status_code)
        
        return response.content


    def DeleteManga(self,manga_id):
        request_string = self.mal_delete_manga_endpoint % str(manga_id)

        response = requests.post(request_string , auth=self.credentials)

        return response.content



    def ProduceAnimeDataXML(self,status=6,episode="",score=""):
        template = """<?xml version="1.0" encoding="UTF-8"?><entry>"""
    
        if(episode != ""):
            template += "<episode>"+str(episode)+"</episode>"
        
        if(status != ""):
            template += "<status>"+str(status)+"</status>"
        
        if(score != ""):
            template += "<score>"+str(score)+"</score>"
        
    #     template += """<storage_type></storage_type>
    # <storage_value></storage_value>
    # <times_rewatched></times_rewatched>
    # <rewatch_value></rewatch_value>
    # <date_start></date_start>
    # <date_finish></date_finish>
    # <priority></priority>
    # <enable_discussion></enable_discussion>
    # <enable_rewatching></enable_rewatching>
    # <comments></comments>
    # <tags></tags>"""
        template += "</entry>"

        return template


    def ProduceMangaDataXML(self,status=6,chapter="",volume="",score=""):
        template = """<?xml version="1.0" encoding="UTF-8"?><entry>"""
    
        if(chapter != ""):
            template += "<chapter>"+str(chapter)+"</chapter>"

        if(volume != ""):
            template += "<volume>"+str(volume)+"</volume>"
        
        if(status != ""):
            template += "<status>"+str(status)+"</status>"
        
        if(score != ""):
            template += "<score>"+str(score)+"</score>"
        
    #     template += """<storage_type></storage_type>
    # <storage_value></storage_value>
    # <times_rewatched></times_rewatched>
    # <rewatch_value></rewatch_value>
    # <date_start></date_start>
    # <date_finish></date_finish>
    # <priority></priority>
    # <enable_discussion></enable_discussion>
    # <enable_rewatching></enable_rewatching>
    # <comments></comments>
    # <tags></tags>"""
        template += "</entry>"

        return template



if __name__ == '__main__':
    username = "Beelzedan"
    password = "ANIMEokm09)("

    mal_api = MyAnimeListAPI(username,password)

    #print(mal_api.PerformSearch("full metal"))

    #print(mal_api.AddUpdateAnime(71))

    #print(mal_api.AddUpdateAnime(71, add=False,status=2,episode="",score=10))

    #print(mal_api.AddUpdateAnime(71, add=False,status=1))
    
    #print(mal_api.DeleteAnime(71))
