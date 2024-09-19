from domain.card_transaction_request import CardTransactionRequest
from data_layer.abstract_card_dao import AbstractCardDao
import datetime


class DebitCardTransactionDao(AbstractCardDao):

    def get_filename(self, filename="./data/card_transaction.json") -> str:
        return filename

    def get_transaction_history(self, card_number: int) -> list:
        result = []
        for item in self.load_file():
            if item.get("card_number") == card_number:
                result.append(item)
        return result
