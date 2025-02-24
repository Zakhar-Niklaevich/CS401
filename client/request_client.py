import requests
import json

API_URL = "http://127.0.0.1:52002/api/recommend"

def get_recommendations():
    print("Enter song names (comma-separated), or type 'exit' to quit.")
    while True:
        user_input = input("Songs: ")
        if user_input.lower() == "exit":
            break

        song_list = [song.strip() for song in user_input.split(",")]
        payload = json.dumps({"songs": song_list})
        headers = {"Content-Type": "application/json"}

        try:
            response = requests.post(API_URL, data=payload, headers=headers)
            if response.status_code == 200:
                print("Recommended Songs:", response.json()["songs"])
            else:
                print("Error:", response.text)
        except requests.exceptions.RequestException as e:
            print("Request failed:", e)

if __name__ == "__main__":
    get_recommendations()
