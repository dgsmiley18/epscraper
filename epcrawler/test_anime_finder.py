import subprocess
from anime_finder import get_episode_name


def test_episode_name():
    anime_name = "Boku no Hero Academia"
    output_file = "bokunohero.txt"
    get_episode_name(anime_name, output_file)
    with open(output_file, "r") as f:
        content = f.read()
        assert "Izuku.Midoriya:.Origin" in content
        assert "What.It.Takes.to.Be.a.Hero" in content


def test_help():
    output = subprocess.check_output(["python", "anime_finder.py", "--help"])
    assert b"specify the anime name" in output
