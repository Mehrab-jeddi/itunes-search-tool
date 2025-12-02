import requests as req 
question = input("Please enter a search term :")
url =f"https://itunes.apple.com/search?term={question}&entity=album"
response = req.get(url)

data = response.json()
result_count = data.get("resultCount")
print(f"The search returned {result_count} results.")

for result in data.get("results"):
        artist = result.get("artistName")
        album = result.get("collectionName")
        track_count = result.get("trackCount")
        print(f"Artist: {artist} - Album: {album} - Track Count: {track_count}")