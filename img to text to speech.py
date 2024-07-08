#!/usr/bin/env python
# coding: utf-8

# In[35]:


from dotenv import find_dotenv, load_dotenv
from transformers import pipeline
import requests
from PIL import Image
import os

load_dotenv(find_dotenv())
HUGGINGFACEHUB_API_TOKEN = os.getenv('your_huggingface_api_token_here')

def img2text(image_path):
    image_to_text = pipeline("image-to-text", model="Salesforce/blip-image-captioning-base")
    with open(image_path, "rb") as image_file:
        img = Image.open(image_file)
        text = image_to_text(img)[0]['generated_text']
    print(f"Extracted text: {text}")
    return text

def generate_story(scenario):
    generator = pipeline("text-generation", model="gpt2")
    story = generator(f"Generate a short story based on the following scenario: {scenario}", max_length=50, num_return_sequences=1)[0]['generated_text']
    print(f"Generated story: {story}")
    return story

def text2speech(message, output_path):
    API_URL = "https://api-inference.huggingface.co/models/espnet/kan-bayashi_ljspeech_vits"
    headers = {"Authorization": f"Bearer {HUGGINGFACEHUB_API_TOKEN}"}

    payload = {
        "inputs": message
    }

    response = requests.post(API_URL, headers=headers, json=payload)
    audio_file_path = os.path.join(output_path, 'audio.mp3')
    with open(audio_file_path, 'wb') as file:
        file.write(response.content)
    print(f"Audio file saved as {audio_file_path}")


# Main function to execute the steps
def main():
    # Set the path of the image file
    image_path = "C:/Users/karan/OneDrive/Desktop/test/images.jpeg"  # Replace with the actual path to your image
    output_path = os.path.dirname(image_path)

    # Convert the image to text
    scenario = img2text(image_path)
    print('img to text done, step 1')

    # Generate a short story based on the extracted text
    story = generate_story(scenario)
    print('text to story done, step 2')

    # Convert the generated story text to audio
    text2speech(story, output_path)
    print('story to speech done, step 3')

    # Inform the user of completion
    print("Process completed. Check the generated audio file in the same folder as the image.")

# Execute the main function when the script is run directly
if __name__ == '__main__':
    main()

