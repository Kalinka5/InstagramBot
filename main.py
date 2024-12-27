import random
from instagrapi import Client


username = "theprogrammer228"
password = "Adsf!k@fglsmm"
comments = ["Просто неймовірно", "Яка краса!", "Що це за витвір мистецтва!"]

client = Client()
client.login(username, password)

user_id = client.user_id_from_username("lil_dar__")
client.user_follow(user_id)

medias = client.user_medias(user_id, 5)
for i, media in enumerate(medias):
    client.media_like(media.id)
    print(f"Liked post number {i+1}")
    comment = random.choice(comments)
    client.media_comment(media.id, comment)
    print(f"Commented {comment} under post number {i+1}")

# hashtag = "programming"
# comments = ["Really cool!", "It's incredible!", "Nice!"]

# medias = client.hashtag_medias_recent(hashtag, 20)

# for i, media in enumerate(medias):
#     client.media_like(media.id)
#     print(f"Liked post number {i+1} of hashtag {hashtag}")
#     if i % 5 == 0:
#         client.user_follow(media.user.pk)
#         print(f"Followed user {media.user.username}")
