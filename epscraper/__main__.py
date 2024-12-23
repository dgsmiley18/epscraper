from epscraper import get_episode_name
import argparse


def main():
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

    # Displays the information on the console
    args = parser.parse_args()
    get_episode_name(args.name, args.output)


if __name__ == "__main__":
    main()
