import instaloader

ig = instaloader.Instaloader()
profile = input("Introduce el usuario de instagram: ")

ig.download_profile(profile, profile_pic_only=True)