from abc import ABC
import json
from util.util import read_file, convert_to_string


class AbstractCardDao(ABC):
    def load_file(self) -> dict:
        content = json.loads(read_file(self.get_filename()))
        return content

    def append_content(self, new_info: dict) -> bool:
        content = []
        prev_content = self.load_file()

        for item in prev_content:
            content.append(item)

        content.append(new_info)
        if self.write_file(content):
            return True
        return False

    def write_file(self, content: str) -> bool:
        try:
            file = open(self.get_filename(), "w")
            file.write(convert_to_string(content))
            file.close()

            return True
        except:
            return False

    def get_filename(self) -> any:
        pass

    def get_infos(self) -> dict:
        return self.load_file()

    def get_info(self, card_number: int) -> dict:
        for item in self.get_infos():
            if item.get("card_number") == card_number:
                return item
        return None
