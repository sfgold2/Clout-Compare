import instaloader

def get_follower_count(username):
    L = instaloader.Instaloader()
    user = "cloutcomparegame"
    password = "petertheanteater2021"
    L.login(user, password)
    profile = instaloader.Profile.from_username(L.context, username)
    return profile.followers

print(get_follower_count('therock'))