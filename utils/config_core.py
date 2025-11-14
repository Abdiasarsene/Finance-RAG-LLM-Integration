# utils/config_loader.py
import os
import yaml

# ====== LOAD SETTINGS FROM ENVIRONMENT VARIABLES ======
class ConfigLoader:
    @staticmethod
    def load_yaml(path: str) -> dict:
        with open(path, "r") as f:
            return yaml.safe_load(f)

    @staticmethod
    def get_env(var: str, default=None):
        return os.environ.get(var, default)
