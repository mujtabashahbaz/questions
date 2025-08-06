import instaloader
import time

L = instaloader.Instaloader()

# Load session (or log in interactively)
try:
    L.load_session_from_file("dentazon360")  
except FileNotFoundError:
    L.interactive_login("dentazon360")
    L.save_session_to_file()

# Target profile
target_profile = "dice_institute"  # Replace with the account you want to scrape
profile = instaloader.Profile.from_username(L.context, target_profile)

# Scrape posts
for post in profile.get_posts():
    print(f"\nPost URL: https://www.instagram.com/p/{post.shortcode}")
    print(f"Caption: {post.caption}")
    
    # Scrape comments (optional)
    for comment in post.get_comments():
        print(f"Comment by {comment.owner.username}: {comment.text}")
    
    time.sleep(3)  # Avoid rate limits