import tweepy
from instagrapi import Client
import requests
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class SocialMediaAutoPoster:
    def __init__(self):
        self.message = "I love dentistry"
        
    def post_to_twitter(self):
        """Post to Twitter/X"""
        try:
            client = tweepy.Client(
                consumer_key=os.getenv('TWITTER_API_KEY'),
                consumer_secret=os.getenv('TWITTER_API_SECRET'),
                access_token=os.getenv('TWITTER_ACCESS_TOKEN'),
                access_token_secret=os.getenv('TWITTER_ACCESS_SECRET')
            )
            
            response = client.create_tweet(
                text=f"🐦 {self.message}! #Dentistry #OralHealth"
            )
            print("Posted to Twitter successfully!")
            return response
        except Exception as e:
            print(f"Twitter error: {e}")
    
    def post_to_instagram(self):
        """Post to Instagram"""
        try:
            cl = Client()
            cl.login(os.getenv('INSTAGRAM_USERNAME'), os.getenv('INSTAGRAM_PASSWORD'))
            
            # For Instagram, you'd typically post an image
            # This is simplified - you'd need an actual image file
            media = cl.photo_upload(
                path="dentistry_image.jpg",  # You need to have this file
                caption=f"📸 {self.message}! ✨\n\n#Dentistry #DentalCare #Smile"
            )
            print("Posted to Instagram successfully!")
            return media
        except Exception as e:
            print(f"Instagram error: {e}")
    
    def post_to_all(self):
        """Post to all platforms"""
        print("Starting social media posting...")
        self.post_to_twitter()
        self.post_to_instagram()
        print("Posting completed!")

if __name__ == "__main__":
    poster = SocialMediaAutoPoster()
    poster.post_to_all()