import requests
from bs4 import BeautifulSoup
from textblob import TextBlob
from gtts import gTTS

# Function to extract text from a URL, summarize it using noun phrases, and convert it to speech
def extract_text_summarize_and_convert_to_speech(url, output_file):
    try:
        # Send a GET request to the URL
        response = requests.get(url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the HTML content of the page
            soup = BeautifulSoup(response.text, 'html.parser')

            # Extract all the text from the page
            page_text = soup.get_text()

            # Create a TextBlob object for the extracted text
            blob = TextBlob(page_text)

            # Extract noun phrases from the text
            noun_phrases = blob.noun_phrases

            # Join the noun phrases to form the summary
            summary = ' '.join(noun_phrases)

            # Convert the summary to speech
            tts = gTTS(text=summary, lang='en')
            tts.save(output_file)

            return summary

        else:
            print("Failed to retrieve the web page. Status code:", response.status_code)
            return None

    except Exception as e:
        print("An error occurred:", str(e))
        return None

# Example usage
url = "https://www.prisma.io/dataguide/intro/what-are-databases"
output_file = "summary.mp3"

summary = extract_text_summarize_and_convert_to_speech(url, output_file)
if summary:
    print("Summary:", summary)
    print("Speech saved to:", output_file)

