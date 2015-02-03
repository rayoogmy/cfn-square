__author__ = 'mhoyer'

import yaml
import logging


class YamlReader(object):
    def __init__(self):
        logging.basicConfig(format='%(asctime)s %(levelname)s %(module)s: %(message)s',
                            datefmt='%d.%m.%Y %H:%M:%S',
                            level=logging.INFO)
        self.logger = logging.getLogger(__name__)

    def read_file(self, file):
        with open(file, 'r') as f:
            return yaml.load(f)


if __name__ == "__main__":
    reader = YamlReader()
    print reader.read_file("stacks.yml")