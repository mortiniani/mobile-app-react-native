import os
import logging
from typing import Dict

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class Utils:
    def __init__(self):
        self.config = {}

    def load_config(self, filename: str) -> Dict:
        try:
            with open(filename, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            logger.error(f"File '{filename}' not found.")
            return {}

    def save_config(self, filename: str, data: Dict) -> None:
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)

    def get_config(self, key: str) -> Dict:
        return self.config.get(key, {})

    def set_config(self, key: str, value: any) -> None:
        self.config[key] = value
```

```python
def main():
    utils = Utils()
    utils.load_config('config.json')
    print(utils.get_config('debug'))
    utils.set_config('debug', True)
    utils.save_config('config.json', utils.get_config('debug'))
    print(utils.get_config('debug'))

if __name__ == '__main__':
    main()