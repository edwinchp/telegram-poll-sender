import random
import time
import requests
from utils.environment_loader import EnvironmentLoader
from utils.json_reader import JsonReader


class DataFactory:

    API_LINK = EnvironmentLoader.get_api_link()

    @staticmethod
    def get_random_data():

        params = {
            'difficulty': random.choice(['easy']),
            'category': 'SELENIUM-101'
        }

        response = requests.get(DataFactory.API_LINK + '/questions/api/random-question/', params=params)
        if response.status_code != 200:
            raise Exception(f'Error fetching random data: {response.status_code} - {response.text}')
        return response.json()

    @staticmethod
    def get_data_by_position(position):
        data = JsonReader.get_results('data/data.json')
        return data[position]

    @staticmethod
    def get_all_data():
        data = JsonReader.get_results('data/data.json')
        return data

    @staticmethod
    def get_data_by_id(data_id):
        data = JsonReader.get_results('data/data.json')
        for single_data in data:
            if single_data['id'] == data_id:
                return single_data
        raise Exception(f'Data with id {data_id} does not exist')