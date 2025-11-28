import pandas as pd
import random
from datetime import datetime, timedelta

# Configuration
num_records = 100
start_date = datetime(2023, 1, 1, 10, 0, 0)

# Options
platforms = ['Twitter', 'Instagram', 'Facebook', 'LinkedIn', 'TikTok']
post_types = ['Text', 'Image', 'Video', 'Article', 'Reel']
regions = ['US', 'UK', 'IN', 'CA', 'AU']
languages = ['English', 'Spanish', 'French', 'German']
binary = ['Yes', 'No']

data = []

for i in range(num_records):
    # Generate random features
    date_time = start_date + timedelta(hours=i + random.randint(0, 2))
    platform = random.choice(platforms)
    post_type = random.choice(post_types)
    region = random.choice(regions)
    language = random.choice(languages)
    has_hashtags = random.choice(binary)
    has_media = random.choice(binary)
    is_ad = random.choice(binary)
    
    followers = random.randint(100, 100000)
    
    # Correlate metrics roughly with followers and random factors
    base_engagement = followers * random.uniform(0.01, 0.1)
    if is_ad == 'Yes':
        base_engagement *= 1.5
    if has_media == 'Yes':
        base_engagement *= 1.2
        
    likes = int(base_engagement * random.uniform(0.5, 0.8))
    shares = int(base_engagement * random.uniform(0.1, 0.3))
    comments = int(base_engagement * random.uniform(0.05, 0.2))
    
    # Calculate Engagement Score (simple formula)
    engagement_score = likes + (shares * 2) + (comments * 3)
    
    data.append([
        date_time.strftime("%Y-%m-%d %H:%M:%S"),
        engagement_score,
        platform,
        post_type,
        region,
        language,
        has_hashtags,
        has_media,
        is_ad,
        followers,
        likes,
        shares,
        comments
    ])

# Create DataFrame
columns = [
    "Date_Time", "Engagement_Score", "Platform", "Post_Type", "Region", 
    "Language", "Has_Hashtags", "Has_Media", "Is_Ad", 
    "Followers", "Likes", "Shares", "Comments"
]
df = pd.DataFrame(data, columns=columns)

# Save to CSV
output_path = "dataset/social_media_data.csv"
df.to_csv(output_path, index=False)

print(f"Successfully generated {len(df)} records to {output_path}")
