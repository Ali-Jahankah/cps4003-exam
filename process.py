from collections import Counter, defaultdict
from statistics import mean

class DataProcessor:
    def __init__(self, data):
        self.data = data

    def total_videos_and_channels(self):
        total_videos = len(self.data)
        channels = {video["channel_title"] for video in self.data}
        return total_videos, len(channels)

    def videos_per_category(self):
        counter = Counter(video["category_id"] for video in self.data)
        return dict(counter)

    def video_details(self, search_term):
        search_term = search_term.lower()
        for video in self.data:
            if (
                video["video_id"].lower() == search_term
                or video["title"].lower() == search_term
            ):
                return video
        return None

    def top_10_videos(self):
        return sorted(
            self.data,
            key=lambda v: (v["views"], v["likes"], v["comment_count"]),
            reverse=True
        )[:10]

    def category_engagement(self):
        categories = defaultdict(lambda: {"likes": [], "dislikes": [], "comments": []})

        for video in self.data:
            cat = video["category_id"]
            categories[cat]["likes"].append(video["likes"])
            categories[cat]["dislikes"].append(video["dislikes"])
            categories[cat]["comments"].append(video["comment_count"])
            
        averages = {}
        
        for cat, values in categories.items():
            averages[cat] = {
                "avg_likes": mean(values["likes"]),
                "avg_dislikes": mean(values["dislikes"]),
                "avg_comments": mean(values["comments"]),
            }
        return averages

    def trending_duration(self):
        dates_by_video = defaultdict(set)

        for video in self.data:
            dates_by_video[video["video_id"]].add(video["trending_date"].date())

        durations = {}
        for video_id, dates in dates_by_video.items():
            durations[video_id] = len(dates)

        return durations

    def high_like_dislike_ratio(self, threshold=10):
        result = []

        for video in self.data:
            if video["dislikes"] == 0:
                continue

            ratio = video["likes"] / video["dislikes"]
            if ratio >= threshold:
                result.append({
                    "video_id": video["video_id"],
                    "title": video["title"],
                    "ratio": round(ratio, 2)
                })

        return result