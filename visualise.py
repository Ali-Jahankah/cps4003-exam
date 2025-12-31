import matplotlib.pyplot as plt
from collections import Counter, defaultdict
from statistics import mean


class Visualiser:
    def __init__(self, data):
        self.data = data

    def pie_videos_per_category(self):
        counts = Counter(video["category_id"] for video in self.data)

        plt.figure()
        plt.pie(counts.values(), labels=counts.keys(), autopct="%1.1f%%")
        plt.title("Distribution of Videos per Category")
        plt.show()

    def histograms_engagement(self):
        views = [video["views"] for video in self.data]
        likes = [video["likes"] for video in self.data]
        comments = [video["comment_count"] for video in self.data]

        plt.figure()
        plt.hist(views, bins=30)
        plt.title("Views Distribution")
        plt.xlabel("Views")
        plt.ylabel("Frequency")
        plt.show()

        plt.figure()
        plt.hist(likes, bins=30)
        plt.title("Likes Distribution")
        plt.xlabel("Likes")
        plt.ylabel("Frequency")
        plt.show()

        plt.figure()
        plt.hist(comments, bins=30)
        plt.title("Comments Distribution")
        plt.xlabel("Comments")
        plt.ylabel("Frequency")
        plt.show()
        
    def avg_trending_duration_per_category(self):
        category_days = defaultdict(list)

        for video in self.data:
            days = (video["trending_date"] - video["publish_time"]).days
            category_days[video["category_id"]].append(days)

        categories = []
        averages = []

        for cat, days in category_days.items():
            categories.append(cat)
            averages.append(mean(days))

        plt.figure()
        plt.plot(categories, averages, marker="o")
        plt.xlabel("Category ID")
        plt.ylabel("Average Trending Duration (days)")
        plt.title("Average Trending Duration per Category")
        plt.show()

    def bar_top_video_engagement(self):
        top_videos = sorted(
            self.data,
            key=lambda v: v["views"],
            reverse=True
        )[:10]

        titles = [video["title"][:15] for video in top_videos]
        likes = [video["likes"] for video in top_videos]
        dislikes = [video["dislikes"] for video in top_videos]
        comments = [video["comment_count"] for video in top_videos]

        x = range(len(titles))

        plt.figure()
        plt.bar(x, likes, label="Likes")
        plt.bar(x, dislikes, bottom=likes, label="Dislikes")
        plt.bar(
            x,
            comments,
            bottom=[l + d for l, d in zip(likes, dislikes)],
            label="Comments"
        )

        plt.xticks(x, titles, rotation=45)
        plt.ylabel("Count")
        plt.title("Engagement Metrics of Top Trending Videos")
        plt.legend()
        plt.show()