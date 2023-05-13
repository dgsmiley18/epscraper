import requests
from bs4 import BeautifulSoup


def get_episode_name(anime_name, output_file):
    # Remove the spaces and replace them with a plus sign
    anime_name = anime_name.replace(" ", "+")
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0"
    }
    url = f"https://anidb.net/anime/?adb.search={anime_name}&do.search=1"
    html = requests.get(url=url, headers=headers).content
    soup = BeautifulSoup(html, "html.parser")

    # Find the first result

    result = soup.find("td", class_="name main anime").find("a").get("href")
    url = f"https://anidb.net{result}"

    html = requests.get(url=url, headers=headers).content
    soup = BeautifulSoup(html, "html.parser")

    # Find the table with the episodes
    trs = soup.find("table", class_="eplist").find("tbody").find_all("tr")
    try:
        if ".txt" in output_file:
            with open(output_file, "a") as writer:
                # Find the episode name
                for tr in trs:
                    ep_name = tr.find("td", class_="title name episode").get_text()
                    # Remove the new line
                    ep_name = ep_name.replace("\n", "")
                    # Remove the spaces
                    ep_name = ep_name.replace(" ", ".")
                    # Type the name of the episodes on the file
                    writer.write(ep_name + "\n")
            return print("The file was created successfully!")
        else:
            return print("The output file must be a .txt file")
    except Exception as e:
        print("Error: ", e)
        return None
