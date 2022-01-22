from typing import OrderedDict
import requests
from requests.models import codes
import pprint
from bs4 import BeautifulSoup

class Kobis:

    def __init__(self,key) -> None:
        self.api_key = key

    def get_url(self):
        base_url = f'http://kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json'
        request_url = base_url + f'?key={self.api_key}'

        return request_url

    ## 영화 이름을 입력하면 정보를 주는 함수
    def name_movie(self,name):
        base_url = f'http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieList.json'
        request_url = base_url + f'?key={self.api_key}'
        move_name = requests.get(request_url + f'&movieNm={name}').json()
        request_name = []
        for i in range(len(move_name["movieListResult"]["movieList"])):
            request_name.append(move_name["movieListResult"]["movieList"][i])
        return request_name

    ## 입력한 날짜의 영화 상영관에 있는 영화를 알려주는 함수
    def day_movie(self,time,local=None):
        base_url = 'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json'
        base_url += f'?key={self.api_key}'
        base_url += f'&targetDt={time}'
        self.local = local
        # 지역 코드가 받아져 왔다면
        if local != None:
            codes_url = requests.get(f'http://kobis.or.kr/kobisopenapi/webservice/rest/code/searchCodeList.json?key={self.api_key}&comCode=0105000000').json()
            local_code = ''
            for i in range(len(codes_url['codes'])):
                if codes_url['codes'][i]['korNm'] == self.local:
                    local_code = codes_url['codes'][i]["fullCd"]
                    base_url += f'&wideAreaCd={local_code}'
            # 만약 그런 지역이 없으면?
            if local_code == '':
                print('그런지역 없습니다')
            
        # 이름을 가져와서 출력
        list_daymov = requests.get(base_url).json()
        list_name = []
        for i in range(len(list_daymov['boxOfficeResult']['dailyBoxOfficeList'])):
            list_name.append(list_daymov['boxOfficeResult']['dailyBoxOfficeList'][i]['movieNm'])
        return list_name
    
    ## 이름을 입력하면 reprole 과 filmolist 를 말해주는 함수
    def actor_movie(self,name):
        pass
        base_url = 'http://www.kobis.or.kr/kobisopenapi/webservice/rest/people/searchPeopleList.json'
        base_url += f'?key={self.api_key}'
        base_url += f'&peopleNm={name}'
        actor_url = requests.get(base_url).json()
        list_actor = []
        role_actor = []
        name_actor = []
        url_set = actor_url["peopleListResult"]["peopleList"]
        for i in range(len(actor_url["peopleListResult"]["peopleList"])):
            name_actor.append(url_set[i]["peopleNm"])
            list_actor.append(url_set[i]["repRoleNm"])
            role_actor.append(url_set[i]["filmoNames"])
            actor_url = {}
            list_all = [0]*len(name_actor)
        list_all = OrderedDict()
        for j in range(len(name_actor)):
            list_all[f'{(j+1)}번째 결과'] = [name_actor[j],list_actor[j],role_actor[j]]
        return list_all

#---- test case ----#
i = Kobis('0cf1798046414be815dbfe42a61c9d49')
# print(i.day_movie(20210729,"부산시"))
# pprint.pprint(i.name_movie('개와 결혼'))
pprint.pprint(i.actor_movie('원빈'))