import cv2
import time
import requests
import base64
import pyttsx3

# OpenAI API key
api_key = ""

# Initialize text-to-speech engine
engine = pyttsx3.init()

# Function to capture an image from the webcam stream
def capture_image_from_stream(url):
    cap = cv2.VideoCapture(url)
    ret, frame = cap.read()
    cap.release()
    if ret:
        filename = 'frame.jpg'
        cv2.imwrite(filename, frame)
        return filename
    else:
        print("Failed to capture image")
        return None

# Function to encode the image to base64
def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

# Function to analyze the image using OpenAI GPT-4
def analyze_image(image_path):
    base64_image = encode_image(image_path)

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }

    payload = {
        "model": "gpt-4-turbo",  
        "messages": [
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "What’s in this image?"
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{base64_image}"
                        }
                    }
                ]
            }
        ],
        "max_tokens": 300
    }

    response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)
    return response.json()

# Function to convert analysis result to speech and play it
def play_analysis_result(result_text):
    engine.say(result_text)
    engine.runAndWait()

# Main loop to capture image, analyze it, and play the result every 20 seconds
def main():
    stream_url = 'http://192.168.0.104:8080/shot.jpg'  
    while True:
        image_path = capture_image_from_stream(stream_url)
        if image_path:
            analysis_result = analyze_image(image_path)
            result_text = analysis_result['choices'][0]['message']['content']
            play_analysis_result(result_text)
        time.sleep(20)

if __name__ == '__main__':
    main()
