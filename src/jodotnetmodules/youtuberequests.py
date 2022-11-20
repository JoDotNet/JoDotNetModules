import os, requests, json



def SETUP(id, key, location):
    channel_id = id
    api_key = key

    API_url = f"https://www.googleapis.com/youtube/v3/search?part=snippet&channelId={channel_id}&maxResults=1&order=date&type=video&key={api_key}"

    with open(os.path.join(location, "youtube.txt"), "w") as file:
        file.write(API_url)
        file.close()



def GetLatestVideo(location):
    API_url = open(location, "r").read()
    request = json.loads(requests.get(API_url).text)
    video_id = request["items"][0]["id"]["videoId"]

    return "https://youtube.com/watch/" + video_id