import os


class Enviroment:
    @staticmethod
    def get_variable(variable_name):
        try:
            result = os.getenv(variable_name)
            return result
        except Exception:
            return None
