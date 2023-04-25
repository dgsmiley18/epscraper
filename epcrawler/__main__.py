from anime_finder import get_episode_name
import argparse
parser = argparse.ArgumentParser(
    prog="Episode Finder",
    description="Find the episodes names from your favorite anime!",
)

# Adds the "--name" argument with an explanation
parser.add_argument(
    "-n", 
    "--name", 
    help="specify the anime name", 
    type=str, 
    required=True,
)
parser.add_argument(
    "-o",
    "--output",
    help="specify the output file",
    default="titles.txt",
    type=str,
    required=False,
)
if __name__ == "__main__":
    args = parser.parse_args()

    # Displays the information on the console
    get_episode_name(args.name, args.output)