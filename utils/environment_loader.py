import os
from dotenv import load_dotenv

class EnvironmentLoader:

    @staticmethod
    def get_bot_token():
        load_dotenv()
        bot_token = os.getenv('BOT_TOKEN')

        if not bot_token:
            raise Exception("Please add BOT_TOKEN environment variable on .env file.")

        return bot_token

    @staticmethod
    def get_chat_id():
        load_dotenv()
        chat_id = os.getenv('CHAT_ID')

        if not chat_id:
            raise Exception("Please add CHAT_ID environment variable on .env file.")

        return chat_id

    @staticmethod
    def get_api_link():
        load_dotenv()
        api_link = os.getenv('API_LINK')

        if not api_link:
            raise Exception("Please add API_LINK environment variable on .env file.")

        return api_link