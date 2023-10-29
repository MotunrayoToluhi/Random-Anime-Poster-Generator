#This piece of code is a random poster generator.
# In the results_file.txt the name of the random anime and it's poster are written down

# Importing modules
import requests
import json
import random

# Using the function to get the anime data from the API
def get_anime_info(anime_id):
    url = f'https://api.jikan.moe/v4/anime/{anime_id}'
    response = requests.get(url)

    # Checking if the request for the data from the API was successful
    if response.status_code == 200:
        anime_data = response.json()
        # If successful, data is returned in dictionary format
        return anime_data

    # If not successful, this error message is printed
    else:
        print("Couldn't get data")
        return None

# Function used to generate a random anime name and its poster
def main():
    # Generates an anime id between 1 and 1000
    anime_id = random.randint(1, 1000)
    anime_data = get_anime_info(anime_id)

    # If an anime id is found, the large image URL is extracted to generate the poster link
    if anime_data:
        title = anime_data.get("data", {}).get("title", "Unknown Title")
        large_image_url = anime_data.get("data", {}).get("images", {}).get("jpg", {}).get("large_image_url", "")
        shortened_url = large_image_url[:100]  # Shorten the URL to the first 50 characters

        if large_image_url:
            # Open a file in write mode so that the URL is written down
            with open("results_file.txt", "w") as file:
                file.write(f"Title: {title}\n")
                file.write(f"Shortened Image URL: {shortened_url}\n")
        else:
            print("Large image URL not found for this anime.")

if __name__ == "__main__":
    # Use main to execute the function and run the program
    main()
