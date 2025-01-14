from playwright.sync_api import sync_playwright
from playwright.sync_api import Browser
from parser import parse_html, create_videos_dict ,convert_to_dataframe, remove_empty_values , save_to_csv
import datahorse as dh

def run(playwright, channel_name: str):
    browser : Browser = playwright.chromium.launch(headless=True)  # ouverture du navigateur sans interface graphique
    page = browser.new_page()
    page.goto(f'https://www.youtube.com/{channel_name}/videos')  # Aller sur la page de la chaine youtube
    page.mouse.down()
    page.locator("#contents").scroll_into_view_if_needed()
    contents = page.locator("#contents")
    contents.wait_for(state="visible", timeout=50000)
    inner_html = contents.inner_html()
    browser.close()
    return inner_html

# def read_csv_file():
#     with open("youtube_videos.csv", "r") as file:
#         content = file.read()
#     return content

if __name__ == '__main__':
    at_channel_name =input("Enter the name of the channel you want to scrape(it should start with a `@` sign ): ")
    with sync_playwright() as playwright:
        if not at_channel_name.startswith("@"):
            print("The channel name is invalid add the `@` sign before the channel name")
        if at_channel_name == "":
            exit()
        page_content = run(playwright, at_channel_name)

    parsed_content  = parse_html(page_content)
    videos_dict = create_videos_dict(parsed_content)
    videos_dict_cleaned = remove_empty_values(videos_dict)
    df_videos = convert_to_dataframe(videos_dict_cleaned)
    save_to_csv(df_videos)
    datahorse_df = dh.read("youtube_videos.csv")
    datahorse_df.chat("draw a column chart to diplsay the number of views for each video")








