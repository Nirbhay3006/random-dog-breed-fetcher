import requests
import webbrowser

def get_random_dog_image():
    response = requests.get("https://dog.ceo/api/breeds/image/random")
    if response.status_code == 200:
        return response.json()['message']
    return None

def extract_breed(url):
    return url.split('/')[4].replace('-', ' ').title()

def main():
    print("Fetching a random dog image...")
    img_url = get_random_dog_image()

    if img_url:
        webbrowser.open(img_url)
        breed = extract_breed(img_url)
        print(f"The breed is: {breed}")
    else:
        print("Could not fetch image.")

main()