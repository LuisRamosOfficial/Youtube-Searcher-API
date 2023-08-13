import requests, json5, json
from bs4 import BeautifulSoup


def get_JsonSearch(url):
    html = requests.get(url).text
    soup = BeautifulSoup(html, "lxml")
    InitialIndex = str(soup).index("var ytInitialData")
    StartCutText = str(soup)[InitialIndex:]

    last = 0
    index = 0
    for n in range(6):
        if n == 0:
            index = StartCutText.rindex("</script>")
            last = StartCutText[:index]
        else:
            index = last.rindex("</script>")
            last = last[:index]

    py_list = json5.loads(str(last[19:-1]))["contents"][
        "twoColumnSearchResultsRenderer"
    ]["primaryContents"]["sectionListRenderer"]["contents"][0]["itemSectionRenderer"][
        "contents"
    ]

    video_list = []

    for n in py_list:
        if list(n.keys())[0] == "videoRenderer":
            
            video = n['videoRenderer']
            thumb = video["thumbnail"]["thumbnails"][0]["url"]
            title = video["title"]["runs"][0]["text"]
            channel = video["longBylineText"]["runs"][0]["text"]
            date = video["publishedTimeText"]["simpleText"]
            time_duration = video["lengthText"]["accessibility"]["accessibilityData"][
                "label"
            ]
            time_short = video["lengthText"]["simpleText"]
            views = video["viewCountText"]["simpleText"]
            url = (
                "https://youtube.com"
                + video["navigationEndpoint"]["commandMetadata"]["webCommandMetadata"][
                    "url"
                ]
            )

            video_list.append({"title": title, 
                               "thumbnail": thumb,
                               "channel": channel,
                               "date": date,
                               "length": time_duration,
                               "length_short": time_short,
                               "views": views,
                               "url": url
                               })

    video_json = json.dumps(video_list, indent=4)
    return video_list
