import tweepy
import os
import random
from secrets import *
from PIL import Image

auth = tweepy.OAuthHandler(C_KEY, C_SECRET)
auth.set_access_token(A_TOKEN, A_TOKEN_SECRET)
api = tweepy.API(auth)

r = lambda: random.randint(0,255)
hex = '#%02X%02X%02X' % (r(),r(),r())

webhexcolor = hex
im = Image.new("RGB", (128,128), webhexcolor)
im.save("color.png")

im = os.path.abspath('color.png')

foo = ['Hey, try this hex code: ', 'Hi, looking for a new color? Try this one: ', 'What are you up to? Want to try a new color? Try this one: ', 'Heya, try this hex code: ', 'Howdy, take this hex code for a spin: ', 'Well hello! Get some inspiration with this hex code: ', 'Yo, here\'s a color for you to try: ']
api.update_with_media(im, status=random.choice(foo) + hex + "#ColorInspiration")

os.remove('color.png')
