import json
from datetime import datetime

class JsonClient:

    def __init__(self, json_file_path):
        self.JSONF_FILE_PATH = json_file_path
        # self.JSON_DATA = self.load(json_file_path)
        
    def load(self):
        with open(self.JSONF_FILE_PATH) as json_file:
            json_data = json.load(json_file)
            return json_data

    def get(self, key, json_object=None, default=None):
        if json_object == None:
            json_object = self.load() #return self.JSON_DATA[key]
        
        if default is None:
            return json_object[key]

        try:
            value = json_object[key]
            return value
        except Exception as exception:
            print('use default (', str(exception), ')')
            return default

    def getDatetime(self, key, json_object=None):
        value = self.get(key, json_object)
        return JsonClient.datetimeFrom(value)

    def decodeToJson(self, content):
        m_decode = str(content.decode("utf-8","ignore"))
        return json.loads(m_decode) # decode to json data

    @staticmethod
    def datetimeFrom(datetime_str, should_print=False):
        # datetime_str = '09/19/18 13:55:26'
        datetime_object = datetime.strptime(datetime_str, '%m/%d/%y %H:%M:%S')
        if should_print:
            print(datetime_object)
