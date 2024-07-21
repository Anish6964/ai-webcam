# Image Analyzer

This project captures an image from a webcam stream, analyzes it using OpenAI GPT-4, and reads out a description of the image. The description is limited to 25 words or 150 characters.

## Requirements

- Python 3.7+
- OpenAI API Key
- The following Python packages:
  - `opencv-python`
  - `requests`
  - `openai`
  - `pyttsx3`
  - `numpy`

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/your-username/image-analyzer.git
    cd image-analyzer
    ```

2. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

3. Replace `YOUR_OPENAI_API_KEY` in `main.py` with your actual OpenAI API key.

## Usage

1. Start the IP Webcam app on your Android phone.
2. Run the script:
    ```sh
    python main.py
    ```

The script will capture an image from the webcam stream every 20 seconds, analyze it using OpenAI, and read out the description.

## License

This project is licensed under the MIT License.
