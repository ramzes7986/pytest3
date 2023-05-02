
class Response:

    def __init__(self, response):
        self.response = response
        self.response_json = response.json()

    def validate(self, schema):
        if isinstance(self.response_json, list):
            for item in self.response_json:
                schema.parse_obj(item)
        else:
            schema.parse_obj(self.response_json)
        return self