import bs4
from rich import print
import arrow
import re
import pandas as pd

def parse_html(html: str):
    soup = bs4.BeautifulSoup(html, 'html.parser')
    # Récupérer la balise avec l'ID "contents"
    contents = soup.select(".style-scope.ytd-rich-grid-renderer")
    if contents:
        print("Nombre de videos charge : ", len(contents))  # Afficher le HTML de la balise "contents"
    else:
        print("Balise avec l'ID 'contents' non trouvée")
    
    return list(contents)


def create_videos_dict(contents: list[bs4.Tag]):
    videos = []
    for video_tag in contents:
        # print("Tag : ", video_tag)
        video_dict = {
            "video title": get_video_title(video_tag),
            "release date": get_video_release_date(video_tag),
            "views numbers": get_video_views(video_tag)
        }
        videos.append(video_dict)
    for vid in videos:
        print(vid)
    return videos


def get_video_title(contents: bs4.Tag):
    title = contents.select_one(".yt-simple-endpoint.focus-on-expand.style-scope.ytd-rich-grid-media")
    if title:
        return title.text
    else:
        print("Titre de la video non trouvé")

def get_video_release_date(contents: bs4.Tag):
    duration = contents.select(".inline-metadata-item.style-scope.ytd-video-meta-block")
    if duration:
        sanitized_date = date_sanitizer(duration[1].text)
        return sanitized_date
    else:
        print("Durée de la video non trouvée")

def get_video_views(contents: bs4.Tag):
    views = contents.select_one(".inline-metadata-item.style-scope.ytd-video-meta-block")
    if views:
        sanitized_views = views_sanitizer(views.text)
        return sanitized_views
    else:
        print("Nombre de vues non trouvé")


def date_sanitizer(date: str):
    now = arrow.utcnow()
    match = re.search(r'(\d+)\s*(day|days|week|weeks|month|months|year|years|hour|hours)\s*ago', date)
    if match:
        value, unit = int(match.group(1)), match.group(2)
        if 'day' in unit:
            return now.shift(days=-value).datetime
        elif 'week' in unit:
            return now.shift(weeks=-value).datetime
        elif 'month' in unit:
            return now.shift(months=-value).datetime
        elif 'year' in unit:
            return now.shift(years=-value).datetime
        elif 'hour' in unit:
            return now.shift(hours=-value).datetime
    else:
        print("Format de date non reconnu")
        return None

def views_sanitizer(views: str):
    number = views.split(" ")[0]
    if "K" in number:
        number = number.replace("K", "")
        if "," in number:
            number = number.replace(",", ".")
            return float(number) * 1000
        else:
            return float(number) * 1000
    elif "M" in number:
        number = number.replace("M", "")
        if "," in number:
            number = number.replace(",", ".")
            if len(number) == 2:
                return float(number) * 1000000
        else:
            return float(number) * 1000000
    else:
        return float(number)


def convert_to_dataframe(data: list):
    df = pd.DataFrame(data)
    print(df)
    return df

def save_to_csv(data: pd.DataFrame):
    data.to_csv("youtube_videos.csv", index=False)
    print("Data saved to videos.csv")