import requests, json5, json
from bs4 import BeautifulSoup


html = requests.get('https://www.youtube.com/results?search_query=the+world+is+yours').text
soup = BeautifulSoup(html, 'lxml')
varDataIndex = str(soup).index('var ytInitialData')
# varFinalIndex = str(soup).index(";</script><script nonce=\"nh2TZ6y_j22p7BqlB_fKaA\"")
ytInitialData = str(soup)[varDataIndex:]

last = 0
index = 0
for n in range(6):
    if n == 0:
        index = ytInitialData.rindex('</script>')
        last = ytInitialData[:index]
    else:
        index = last.rindex('</script>')
        last = last[:index]

py_obj = json5.loads(str(last[19:-1]))
json_object = json.dumps(py_obj, indent = 4)

with open('okay.json', "w", encoding="utf-8") as f:
    f.write(json_object)