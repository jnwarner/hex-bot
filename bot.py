import tweepy
import os
import time
import random
from secrets import *
from PIL import Image

#log into Twitter
auth = tweepy.OAuthHandler(C_KEY, C_SECRET)
auth.set_access_token(A_TOKEN, A_TOKEN_SECRET)
api = tweepy.API(auth)

#generate random hex and store in variable
r = lambda: random.randint(0,255)
hex = '#%02X%02X%02X' % (r(),r(),r())

#generate 128px x 128px image with hex fill
webhexcolor = hex
im = Image.new("RGB", (128,128), webhexcolor)
im.save("color.png")

#set im equal to the path of the image
im = os.path.abspath('color.png')

#greeting array
foo = ['Hey, try this hex code: ', 'Hi, looking for a new color? Try this one: ', 'What are you up to? Want to try a new color? Try this one: ', 'Heya, try this hex code: ', 'Howdy, take this hex code for a spin: ', 'Well hello! Get some inspiration with this hex code: ', 'Yo, here\'s a color for you to try: ']

#store random greeting in a variable
greeting = random.choice(foo)

#update Twitter status with im, random greeting, and hex
api.update_with_media(im, status=greeting + hex + " #ColorInspiration")

#delete color.png 5 seconds after tweeting
time.sleep(5)
os.remove('color.png')
