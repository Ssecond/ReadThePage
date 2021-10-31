# Constants
import requests as requests

# Делаем запрос и получаем html.
response = requests.get('https://dvgups.ru/')
textOfSite = response.text.split('\n')
if response.status_code == 200:
    final = ''
    news = []
    for string in textOfSite:
        if string.find('<span><p') != -1:
            final = string
            i = 0
            while i < len(string):
                if string[i] == '<':
                    while string[i] != '>':
                        final = final.replace(string[i], '', 1)
                        i += 1
                    final = final.replace(string[i], '', 1)
                i += 1
            final = final.replace('\t', '').replace('\n', '').replace('-', '—', 1)
            final = final.replace('&b;', '').replace('&nbs;', '').replace('&nbsp;pspn', '')
            news.append(final)
    for o in news:
        print(o)
else:
    print('Something wrong happened: ' + str(response.status_code))
print()
