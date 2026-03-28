import instaloader

# Create object
L = instaloader.Instaloader()

# Username of profile
username = input("Enter Instagram username: ")

# Download profile (posts, images, videos)
L.download_profile(username, profile_pic_only=False)