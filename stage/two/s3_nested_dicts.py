from utils.form import blank_form
from utils import fields_generate


route = {
    'type': blank_form,
    'url': '/stage/two/s3_nested_dicts',
    'methods': ['GET', 'POST']
}

data = {
    'title': 'Spotify Playlist: Iterating through a Nested Dictionary',
    'author': 'Nemesis Contreras (@nemessisc) on Twitter!',
    'description': [
        'Let\'s learn about iterating through nested dictionaries!',
        'Our goal is to check if our Spotify playlist is at least 15 minutes so we can go on a run!' 
        'We will use a for loop to iterate over the nested dictionary and'+
        'check if once we add up the duration of all the songs it will be at least 15 minutes!' 
        '\n',
        'Our starter code is as follows ' 
        '' 
        'We want to take the Duration for all the songs and add them up!' 
        'Using a for loop can help us ,
        'Given the following for loop write the if statement logic to '+ 
        'check if we can use the playlist only if it is 15 minutes or longer!'
    ],
    'code': [
         'playlist = {
           "Title": "Kpop Music",
           "Author": "Nemesis",
           "Songs": [
                     {"Title": "Peek-A-Boo", "Artist": ["Red Velvet"], "Duration": 3.49},
                     {"Title": "Idol", "Artist": ["BTS"], "Duration": 3.51},
                     {"Title": "DDU-DU DDU-DU", "Artist": ["Blackpink"], "Duration": 3.35},
                     {"Title": "Really Really", "Artist": ["Winner"], "Duration": 3.40},
                     {"Title": "MIC Drop (Steve Aoki Remix)", "Artist": ["BTS"], "Duration": 4.34},

                     ]}'  


        'total_duration = 0',

        'for song in playlist["Songs"]:
            total_duration += song["Duration"]',


    ],
    'fields': []
}

data['fields'] = fields_generate(data)


async def sanic_request(request):
    try:
        return override(request)
    except NameError:
        global data, route
        return route['type'](data, request, answer)


def answer(stdout, stderr):
    try:
        if stderr != []:
            return False
        else:
            ans = "Yes! You can use this playlist it is 18.09 min\n"
            if stdout[0].decode() != ans:
                return False
            return True
    except Exception:
return False