from playwright.sync_api import sync_playwright
from parser import parse_html, create_videos_dict ,convert_to_dataframe , save_to_csv
# import datahorse as dh

def run(playwright):
    browser = playwright.chromium.launch(headless=True) # ouverture du navigateur sans interface graphique
    page = browser.new_page()
    page.goto('https://www.youtube.com/@JustinSung/videos') # Aller sur la page de la chaine youtube
    contents = page.locator("#contents")
    contents.wait_for()
    inner_html = contents.inner_html()
    browser.close()
    return inner_html

def read_csv_file():
    with open("youtube_videos.csv", "r") as file:
        content = file.read()
    return content

if __name__ == '__main__':
    with sync_playwright() as playwright:
        page_content = run(playwright)

    parsed_content  = parse_html(page_content)
    videos_dict = create_videos_dict(parsed_content)
    df_videos = convert_to_dataframe(videos_dict)
    save_to_csv(df_videos)
    # file_content = read_csv_file()
    # datahorse_df = dh.read(file_content)
    # datahorse_df.chat("Visualise the number of views for each video")



################ to do ###########
# fix datahorse error 
# add scroll to the page to get more videos





