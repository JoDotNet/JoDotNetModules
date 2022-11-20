import os, requests, json



def SETUP(id, key, location):
    channel_id = id
    api_key = key

    API_url = f"https://www.googleapis.com/youtube/v3/search?part=snippet&channelId={channel_id}&maxResults=1&order=date&type=video&key={api_key}"

    with open(os.path.join(location, "youtube.txt"), "a") as file:
        file.write(API_url)
        file.close()

    with open(os.path.join(location, "latestvideo.txt"), "a") as file:
        file.close()


def GetLatestVideo(location):
    API_url = None
    with open(os.path.join(location, "youtube.txt"), "r") as file:
        API_url = file.read()
        file.close()

    request = json.loads(requests.get(API_url).text)
    video_id = request["items"][0]["id"]["videoId"]

    return "https://youtube.com/watch/" + video_id

def CheckVideos(location):
    GET_Video = GetLatestVideo(location)
    LATEST_Video = None
    with open(os.path.join(location, "latestvideo.txt"), "r") as file:
        LATEST_Video = file.read()
        file.close()

    if GET_Video == LATEST_Video:
        print("Video is up to date.")
        return "nil"
    else:
        print("Video is not up to date. Updating now!")
        
        with open(os.path.join(location, "latestvideo.txt"), "w") as file:
            file.write(str(GET_Video))
            file.close()
            
        return str(GET_Video)