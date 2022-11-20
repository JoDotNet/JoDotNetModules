import time
from jodotnetmodules import youtuberequests

CHANNEL_ID = "Enter_YouTube_Channel_ID"
API_KEY = "Enter_Your_Secret_API_Key"
LOCATION = r"C:\Users\user\Desktop\ExampleFolder"


# Only run this once, if you run it multiple times it will mess the files up.
youtuberequests.SETUP(id=CHANNEL_ID, key=API_KEY, location=LOCATION)


# This loop will print out the status, if there is any new videos it will print it out.
while True:
    request = youtuberequests.CheckVideos(location=LOCATION)
    print(request)
    time.sleep(1800)