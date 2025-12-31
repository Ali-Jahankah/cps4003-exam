import json
import csv

class DataExporter:
    def __init__(self, data):
        self.data = data

    def export_video_json(self, video, output_path):
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(video, f, indent=4, default=str)
        print(f"Video exported to {output_path}")

    def export_top_10(self, videos, output_path, format="json"):
        if format == "json":
            with open(output_path, "w", encoding="utf-8") as f:
                json.dump(videos, f, indent=4, default=str)

        elif format == "csv":
            with open(output_path, "w", newline="", encoding="utf-8") as f:
                writer = csv.DictWriter(
                    f,
                    fieldnames=["video_id", "title", "views", "likes", "comment_count"]
                )
                writer.writeheader()
                for v in videos:
                    writer.writerow({
                        "video_id": v["video_id"],
                        "title": v["title"],
                        "views": v["views"],
                        "likes": v["likes"],
                        "comment_count": v["comment_count"]
                    })

        print(f"Top 10 videos exported to {output_path}")

    def export_category_metrics(self, metrics, output_path):
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(metrics, f, indent=4)
        print(f"Category metrics exported to {output_path}")

    def export_filtered(self, key, value, output_path):
        filtered = [
            video for video in self.data
            if str(video.get(key)) == value
        ]

        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(filtered, f, indent=4, default=str)

        print(f"Filtered dataset exported to {output_path}")