from modules import get_JsonSearch

url = 'https://www.youtube.com/results?search_query=Ricardo+Salvatore'
dicti = get_JsonSearch(url)




with open('okay.json', "w", encoding="utf-8") as f:
    f.write(str(dicti))