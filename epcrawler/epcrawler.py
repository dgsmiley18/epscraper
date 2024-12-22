import requests
from bs4 import BeautifulSoup
import re


def get_episode_name(anime_name, output_file="titles.txt"):
    # Remove the spaces and replace them with a plus sign
    anime_name = anime_name.replace(" ", "+")
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0"
    }
    url = f"https://anidb.net/anime/?adb.search={anime_name}&do.search=1&entity.animetb=1&field.titles=1"
    html = requests.get(url=url, headers=headers).content
    soup = BeautifulSoup(html, "html.parser")

    # Find the first result with the link
    result = soup.find_all("tr", class_="g_odd")[0].find("a").get("href")

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
                    # Remove the new line and spaces
                    ep_name = (
                        ep_name.replace("\n", "")
                        .replace(" ", ".")
                        .replace("\t", "")
                        .replace("-", ".")
                    )
                    name_result = re.sub(r'[\\/:\,`"*?<>|]+', "", ep_name)
                    # Type the name of the episodes on the file
                    writer.write(name_result + "\n")
            return print("The file was created successfully!")
    except writer.errors as error:
        return print("Error: ", error)
