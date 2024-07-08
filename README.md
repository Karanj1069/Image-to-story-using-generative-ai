# Image to Audio Story Converter

This Python script demonstrates how to convert an image into an audio story using Hugging Face's transformers library and API. It integrates image captioning, text generation, and text-to-speech functionalities to create an audio narration based on the content of an uploaded image.

## Features

- **Image to Text Conversion**: Uses a pre-trained image captioning model (`Salesforce/blip-image-captioning-base`) to extract text from an uploaded image.
- **Text Generation**: Generates a short story based on the extracted text using the GPT-2 language model.
- **Text to Speech**: Converts the generated story into audio using the ESPnet model for text-to-speech.

## Requirements

- Python 3.x
- Install required packages using `pip install -r requirements.txt`
- Hugging Face API token (obtainable from Hugging Face's website)

## Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/image-to-audio-story.git
   cd image-to-audio-story
   ```

2. Set up your environment:
   - Create a virtual environment (optional but recommended).
   - Install dependencies:
     ```bash
     pip install -r requirements.txt
     ```

3. Configure API token:
   - Create a `.env` file in the root directory and add your Hugging Face API token:
     ```
     'your_huggingface_api_token_here'=your_huggingface_api_token_here
     ```

4. Run the script:
   ```bash
   python image_to_audio_story.py
   ```

5. Follow the prompts:
   - Choose an image file when prompted.
   - Wait for the script to process the image, generate a story, and convert it to audio.
   - The resulting audio file (`audio.mp3`) will be saved in the same folder as the image.

## Example

- Input: An image depicting a serene landscape.
- Output: An audio file narrating a short story inspired by the image's content.

## Notes

- Ensure the image file format is supported by the image captioning model.
- Adjust parameters (e.g., story length) in the script as needed for different use cases.
