import csv
import random
from faker import Faker

# Initialize Faker instance
fake = Faker()

# Predefined set of hashtags
predefined_hashtags = ['#funny', '#dance', '#travel', '#food', '#music', 
                       "#tiktok", "#fyp", "#FYI", "#fypシ゚", "viral", "#foryou",
                       "#love",'#LoveYouTikTok', '#love', 
                       '#instalove', '#couplegoals', '#relationshipgoals', '#loveyou', 
                       '#happiness', '#romance', '#heart', "#kiss", "#forever",
                       '#dance', '#dancer', '#dancers', '#dancemoms', '#poledance', '#dancehall', '#dancelife', "#bellydance"
                       ]


# Function to generate fake TikTok-like data
def generate_fake_tiktok():
    # Generate author details
    author = fake.user_name()
    author_followers = random.randint(100, 1000000)
    author_likes = random.randint(100, 1000000)
    author_videos = random.randint(1, 1000)

    # Generate TikTok content
    body = fake.sentence(nb_words=10)
    is_duet = random.choices([True, False], weights=[40, 60], k=1)[0]  # 60% chance of being False
    tiktok_url = "https://www.tiktok.com/" + fake.lexify(text='??????????')  # Random string after base URL
    likes = random.randint(0, 100000)
    comments = random.randint(0, 10000)
    shares = random.randint(0, 10000)
    plays = random.randint(1000, 1000000)

        # Add emojis to the body text with a probability of 20%
    if random.random() < 0.4:
        num_emojis = random.randint(1, 3)  # Random number of emojis between 1 and 3
        emojis = [fake.emoji() for _ in range(num_emojis)]
        body += ' ' + ' '.join(emojis)

    # Generate hashtags
    if random.random() < 0.2:  # 20% chance of using predefined hashtags
        hashtags = random.sample(predefined_hashtags, k=random.randint(1, min(len(predefined_hashtags), 3)))
    else:
        hashtags = [fake.word() for _ in range(random.randint(1, 5))]
    
    hashtags = [hashtag for hashtag in hashtags]

    # Combine body and hashtags
    body_with_hashtags = body + ' ' + ' '.join(hashtags)

    # Generate random timestamp
    timestamp = fake.date_time_between(start_date='-30d', end_date='now')

    # Construct TikTok dictionary
    tiktok_data = {
        "author": author,
        "author_followers": author_followers,
        "author_likes": author_likes,
        "author_videos": author_videos,
        "body": body_with_hashtags,
        "timestamp": timestamp,
        "is_duet": is_duet,
        "tiktok_url": tiktok_url,
        "likes": likes,
        "comments": comments,
        "shares": shares,
        "plays": plays
    }

    return tiktok_data

# Generate fake TikTok-like data and write to CSV file
with open('tiktok_data.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['author', 'author_followers', 'author_likes', 'author_videos', 'body', 'timestamp', 'is_duet',
                  'tiktok_url', 'likes', 'comments', 'shares', 'plays']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    # Generate 10,000 fake TikTok-like records
    for _ in range(10000):
        tiktok_data = generate_fake_tiktok()
        writer.writerow(tiktok_data)

print("Fake TikTok-like data has been written to tiktok_data.csv.")


