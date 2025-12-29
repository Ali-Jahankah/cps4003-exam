from load import DataLoader

def cli_menu():
    loader = DataLoader("./data/youtube_trending_videos.csv")
    loader.load_csv()
    loader.save_to_json("./data/data.json")
    while True:
        print("""\n -------------------------------
| Please choose an option below |
 -------------------------------""")
        print("1.  Total videos and channels")
        print("2.  Category summary")
        print("3.  Video info by ID or title")
        print("4.  Top trending videos")
        print("5.  Average engagement by category")
        print("6.  Trending duration per video")
        print("7.  High like/dislike ratio videos")
        print("8.  Exit")
        choice = input("\nSelect an option: ")
        print(choice)


if __name__ == "__main__":
    cli_menu()