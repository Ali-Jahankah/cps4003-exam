from load import DataLoader
from process import DataProcessor
from visualise import Visualiser
from export import DataExporter
def cli_menu():
    loader = DataLoader("./data/youtube_trending_videos.csv")
    data = loader.load_csv()
    loader.save_to_json("./data/data.json")
    processor = DataProcessor(data)
    visualiser = Visualiser(data)
    exporter = DataExporter(data)
    while True:
        print("""\n -------------------------------
| Please choose an option below |
 -------------------------------
    1.  Total videos and channels
    2.  Category summary
    3.  Video info by ID or title
    4.  Top trending videos
    5.  Average engagement by category
    6.  Trending duration per video
    7.  High like/dislike ratio videos
    8.  Pie chart: videos per category
    9.  Histograms: views, likes, comments
    10. Line chart: avg trending duration per category
    11. Bar chart: engagement of top videos
    12. Export video details (JSON)
    13. Export top 10 videos (CSV / JSON)
    14. Export category engagement metrics (JSON)
    15. Export filtered dataset
    16. Exit
        """)

        choice = int(input("\nSelect an option: "))

        if choice == 1:
            videos, channels = processor.total_videos_and_channels()
            print(f"\nTotal videos: {videos}")
            print(f"Total channels: {channels}")

        elif choice == 2:
            categories = processor.videos_per_category()
            for cat, count in categories.items():
                print(f"Category {cat}: {count} videos")

        elif choice == 3:
            term = input("Enter video ID or exact title: ")
            video = processor.video_details(term)
            if video:
                for k, v in video.items():
                    print(f"{k}: {v}")
            else:
                print("Video not found.")

        elif choice == 4:
            top_videos = processor.top_10_videos()
            for i, video in enumerate(top_videos, 1):
                print(f"{i}. {video['title']} | Views: {video['views']}")

        elif choice == 5:
            averages = processor.category_engagement()
            for cat, stats in averages.items():
                print(f"Category {cat}:")
                print(f"  Avg Likes: {stats['avg_likes']:.2f}")
                print(f"  Avg Dislikes: {stats['avg_dislikes']:.2f}")
                print(f"  Avg Comments: {stats['avg_comments']:.2f}")

        elif choice == 6:
            durations = processor.trending_duration()
            for vid, days in list(durations.items())[:10]:
                print(f"video_id: {vid} - Duration: {days} days")

        elif choice == 7:
            viral = processor.high_like_dislike_ratio()
            for v in viral[:10]:
                print(f"""{v['title']}
                      Ratio: {v['ratio']}
                      ------------------------""")

        elif choice == 8:
            visualiser.pie_videos_per_category()

        elif choice == 9:
            visualiser.histograms_engagement()

        elif choice == 10:
            visualiser.avg_trending_duration_per_category()

        elif choice == 11:
            visualiser.bar_top_video_engagement()
        
        elif choice == 12:
            term = input("Enter video ID or exact title: ")
            video = processor.video_details(term)
            if video:
                exporter.export_video_json(video, "./data/video_export.json")
            else:
                print("Video not found.")

        elif choice == 13:
            format = input("Enter format (json/csv): ").lower()
            top_videos = processor.top_10_videos()
            exporter.export_top_10(
                top_videos,
                f"./data/top_10_videos.{format}",
                format
            )

        elif choice == 14:
            metrics = processor.category_engagement()
            exporter.export_category_metrics(
                metrics,
                "./data/category_engagement.json"
            )

        elif choice == 15:
            print("Filter keys: category_id | channel_title")
            key = input("Enter filter key: ")
            value = input("Enter filter value: ")
            exporter.export_filtered(
                key,
                value,
                "./data/filtered_data.json"
            )
        
        elif choice == 16:
            print("Exiting program.")
            break

        else:
            print("Invalid option.")


if __name__ == "__main__":
    cli_menu()