def cli_menu():

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
        print("12. Exit")
        choice = input("\nSelect an option: ")
        print(choice)


if __name__ == "__main__":
    cli_menu()