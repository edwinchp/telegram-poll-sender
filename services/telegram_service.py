import json
import time
import requests
from typing import List, Optional, Union

class TelegramService:
    def __init__(self, bot_token):
        self.bot_token = bot_token

    def send_poll(self, chat_id, question):
        url = f'https://api.telegram.org/bot{self.bot_token}/sendPoll'

        payload = {
            'chat_id': chat_id,
            'question': question.question,
            'options': json.dumps(question.options),
            'is_anonymous': True,
            'allows_multiple_answers': False,
            'type': 'quiz',
            'correct_option_id': question.correct_option_id,
            'explanation': question.explanation,
        }

        try:
            start_time = time.time()
            response = requests.post(url, data=payload, timeout=10)  # 10 second timeout
            elapsed = time.time() - start_time
            
            if response.status_code != 200:
                raise Exception(f'Error sending poll: {response.status_code} - {response.text}')
                
            print(f"✅ Poll sent successfully in {elapsed:.2f}s")
            return response
            
        except requests.Timeout:
            raise Exception('Request to Telegram API timed out after 10 seconds')
        except requests.RequestException as e:
            raise Exception(f'Error sending poll: {str(e)}')

    def send_message(self, chat_id, text):
        url = f"https://api.telegram.org/bot{self.bot_token}/sendMessage"

        payload = {
            "chat_id": chat_id,
            "text": text,
            "parse_mode": "Markdown"
        }
        try:
            start_time = time.time()
            response = requests.post(url, json=payload, timeout=10)  # 10 second timeout
            elapsed = time.time() - start_time
            
            if response.status_code != 200:
                raise Exception(f'Error sending message: {response.status_code} - {response.text}')
                
            print(f"✅ Message sent in {elapsed:.2f}s")
            return response
            
        except requests.Timeout:
            raise Exception('Request to Telegram API timed out after 10 seconds')
        except requests.RequestException as e:
            raise Exception(f'Error sending message: {str(e)}')

    def send_photo(self, chat_id, photo_path):
        url = f"https://api.telegram.org/bot{self.bot_token}/sendPhoto"

        try:
            start_time = time.time()
            with open(photo_path, 'rb') as photo_file:
                files = {'photo': photo_file}
                response = requests.post(url, files=files, data={'chat_id': chat_id}, timeout=30)  # 30s timeout for file uploads
                
            elapsed = time.time() - start_time
            
            if response.status_code != 200:
                raise Exception(f'Error sending photo: {response.status_code} - {response.text}')
                
            print(f"✅ Photo sent in {elapsed:.2f}s")
            return response
            
        except FileNotFoundError:
            raise Exception(f'Photo file not found: {photo_path}')
        except requests.Timeout:
            raise Exception('Request to Telegram API timed out after 30 seconds')
        except requests.RequestException as e:
            raise Exception(f'Error sending photo: {str(e)}')
