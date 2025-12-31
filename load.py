import csv
import os
from datetime import datetime, timezone
import json
class DataLoader:
    def __init__(self, filepath):
        self.filepath = filepath
        self.data = []

    def load_csv(self):
        if not os.path.exists(self.filepath):
            raise FileNotFoundError(f"File not found in:\n {self.filepath}")
        with open(self.filepath, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                row['category_id'] = int(row['category_id'])
                row['views'] = int(row['views'])
                row['likes'] = int(row['likes'])
                row['dislikes'] = int(row['dislikes'])
                row['comment_count'] = int(row['comment_count'])
                row['trending_date'] = datetime.strptime(row['trending_date'], "%y.%d.%m").replace(tzinfo=timezone.utc)
                row['publish_time'] = datetime.fromisoformat(row['publish_time'].replace('Z', '+00:00'))
                row["comments_disabled"] = row["comments_disabled"] == "True"
                row["ratings_disabled"] = row["ratings_disabled"] == "True"
                row["video_error_or_removed"] = row["video_error_or_removed"] == "True"
                self.data.append(row)
        return self.data
    
    def save_to_json(self, output_path):
        newData = []
        for row in self.data:
            cleaned_row = row.copy()
            cleaned_row['trending_date'] = row['trending_date'].isoformat()
            cleaned_row['publish_time'] = row['publish_time'].isoformat()
            newData.append(cleaned_row)
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(newData, f, indent=4)
        print(f"New data saved to {output_path}")