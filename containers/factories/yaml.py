import os
from containers.models.config import ApplicationConfig
from helpers.containers.databaseHelper import yaml, load_dotenv


class FactoryYaml:
    @staticmethod
    def config() -> ApplicationConfig:
        load_dotenv()  # Load environment variables from .env file
        with open('./configurations/config.yaml', 'r') as stream:
            config_data = yaml.safe_load(stream)

        def replace_placeholders(data):
            if isinstance(data, dict):
                return {k: replace_placeholders(v) for k, v in data.items()}
            elif isinstance(data, list):
                return [replace_placeholders(item) for item in data]
            elif isinstance(data, str) and data.startswith("${") and data.endswith("}"):
                env_var = data[2:-1]
                return os.getenv(env_var, data)
            return data

        config_data = replace_placeholders(config_data)
        return ApplicationConfig(**config_data)
