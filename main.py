import os
import requests
from dotenv import load_dotenv
load_dotenv()

subscription_key = os.getenv('SPEECH_KEY')
region = os.getenv('SPEECH_REGION')
url = f'https://{region}.tts.speech.microsoft.com/cognitiveservices/v1'
headers = {
    'Ocp-Apim-Subscription-Key': subscription_key,
    'Content-Type': 'application/ssml+xml',
    'X-Microsoft-OutputFormat': 'audio-16khz-128kbitrate-mono-mp3',
    'User-Agent': 'curl'
}

def text_to_mp3(text:str, path:str):
    data = f'<speak version=\'1.0\' xml:lang=\'en-US\'>\n    <voice xml:lang=\'en-US\' xml:gender=\'Male\' name=\'en-US-ChristopherNeural\'><prosody pitch="high"></prosody>{text}</voice>\n</speak>'
    response = requests.post(url, headers=headers, data=data)
    with open(path, 'wb') as f:
        f.write(response.content)

def parse_text(text:str) -> str:
    return text.replace('’', '\'').replace('-',' ').replace('/', ' and ').replace('\n', ' ').replace('**','')
def rm_all(dir_name:str):
    for filename in os.listdir(dir_name):
        file_path = os.path.join(dir_name, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
        except Exception as e:
            print(f'Failed to delete {file_path}. Reason: {e}')

def split_slides_to_mp3(file_path:str):
    dir_name = os.path.basename(file_path).split('.')[0]
    if not os.path.isdir(dir_name):
        os.mkdir(dir_name)
    else: 
        rm_all(dir_name)
    
    with open(file_path, 'r') as f:
        content = f.read()
    slides = content.split('### Slide')[1:]
    for i, slide in enumerate(slides):
        slide_title, slide_content = slide.split('\n', 1)
        slide_title = slide_title.strip().split(' - ')[-1]
        slide_content = slide_content.strip()
        slide_content = parse_text(slide_content)
        text_to_mp3(slide_content, f'{dir_name}/slide_{i+1}_{slide_title}.mp3')

if __name__ == '__main__':
    split_slides_to_mp3('md/exploring.md')