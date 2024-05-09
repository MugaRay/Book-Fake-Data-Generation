from faker import Faker
import random
import csv
import emoji



# Initialize Faker instance
fake = Faker()

# Define a list of emojis
emojis = [':)', ':(', ':D', ':p', ':heart:', ':fire:', ':thumbsup:', ':rocket:', ':sunglasses:']

# Keywords related to climate change
climate_keywords = [
    'climatechange', 'climatechange', 'climatechange',  # Weight: 3
    'globalwarming', 'globalwarming',  # Weight: 2
    'carbonemissions',  # Weight: 1
    'renewableenergy', 'renewableenergy',  # Weight: 2
    'sustainability', 'sustainability',  # Weight: 2
    'greenhousegases',  # Weight: 1
    'climatecrisis',  # Weight: 1
    'carbonfootprint',  # Weight: 1
    'cleanenergy',  # Weight: 1
    'sustainabledevelopment',  # Weight: 1
    'environmentaljustice'  # Weight: 1
]


# Supported languages and their corresponding Faker providers
languages = {
    'en': fake.text,
    'es': fake.text,
    'fr': fake.text,
    'de': fake.text,
}

def generate_fake_tweet(users):
    # Generate random username
    username = fake.user_name()

    # Generate tweet content with climate change keywords
    language = random.choices(['en', 'es', 'fr', 'de'], weights=[0.7, 0.1, 0.1, 0.1], k=1)[0]  # 70% chance of English
    tweet_content = languages[language](max_nb_chars=140)  # Generate tweet content in the selected language





    # Add climate change hashtags
    tweet_content += ' #' + random.choices(climate_keywords)[0]
    tweet_content += ' #' + random.choices(climate_keywords)[0]


    
    # adding emojis to the text

    if random.random() < 0.4:
        num_emojis = random.randint(1, 3)  # Random number of emojis between 1 and 3
        emojis = [fake.emoji() for _ in range(num_emojis)]
        tweet_content += ' ' + ' '.join(emojis)


    # Add fake user mentions
    if random.random() < 0.5:  # 50% chance of including a mention
        mentioned_user = random.choice(users)
        tweet_content += ' @' + mentioned_user

    # Generate random timestamp (within the past year)
    timestamp = fake.date_time_between(start_date='-1y', end_date='now')

    # Generate random number of likes and retweets
    likes = random.randint(0, 1000)
    retweets = random.randint(0, 500)

    # Generate random location
    location = fake.city()

    # Generate reply_to field (usually null)
    reply_to = "NA"
    if random.random() < 0.3:  # 30% chance of replying to another user
        reply_to = random.choice(users)

    # Construct tweet dictionary
    tweet = {
        "username": username,
        "content": tweet_content,
        "timestamp": timestamp,
        "likes": likes,
        "retweets": retweets,
        "location": location,
        "language": language,
        "reply_to": reply_to
    }

    return tweet

# Generate 10,000 fake tweets about climate change
with open('climate_tweets.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['username', 'content', 'timestamp', 'likes', 'retweets', 'location', 'language', 'reply_to']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    users = [fake.user_name() for _ in range(100)]  # Generate 100 users

    for _ in range(10000):
        tweet = generate_fake_tweet(users)
        writer.writerow(tweet)
