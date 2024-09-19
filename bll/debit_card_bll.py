import datetime
from data_layer.debit_card_dao import DebitCardDao

from domain.card_info_register_request import CardInfoRegisterRequest
from data_layer.debit_card_transaction_dao import DebitCardTransactionDao
from data_layer.debit_card_dao import DebitCardDao
from domain.card_transaction_request import CardTransactionRequest
from util.util import is_int


class DebitCardBll:
    def __init__(self) -> None:
        self.__debit_card_transaction_dao = DebitCardTransactionDao()
        self.__debit_card_dao = DebitCardDao()

    def get_transaction_history(self, card_number: int) -> list:
        return self.__debit_card_transaction_dao.get_transaction_history(card_number)

    def register_card(self, card_info_request: CardInfoRegisterRequest) -> dict:
        new_info = {
            "card_number": card_info_request.card_number,
            "account_name": card_info_request.account_name,
            "card_status": "Inactive",
            "balance": 0.0,
        }

        result = self.__debit_card_dao.append_content(new_info)
        if result:
            return new_info
        return None

    def is_card_number_unique(self, card_number: int) -> bool:
        cards = self.__debit_card_dao.get_infos()
        if len(cards) == 0:
            return True

        if not self.is_card_number_exist(card_number):
            return True
        return False

    def is_card_number_exist(self, card_number: int) -> bool:
        if self.__debit_card_dao.get_info(card_number) != None:
            return True
        return False

    def activate_card(self, card_number) -> dict:
        card_info = self.__debit_card_dao.get_info(card_number)
        if card_info != None:
            if self.update_card_info(card_number, "card_status", "Active"):
                return card_info
        return None

    def update_card_info(
        self, card_number: int, dict_value: str, new_value: str
    ) -> bool:
        prev_content = self.__debit_card_dao.get_infos()
        index = 0
        if not (len(prev_content) == 0):
            for item in prev_content:
                if item.get("card_number") == card_number:
                    prev_content[index][dict_value] = new_value
                    self.__debit_card_dao.write_file(prev_content)
                    return True
                index += 1
        return False

    def is_valid_transaction(
        self, card_transaction_request: CardTransactionRequest, transaction_type: str
    ) -> bool:
        if (
            card_transaction_request.amount
            > self.__debit_card_dao.get_info(card_transaction_request.card_number).get(
                "balance"
            )
            and transaction_type == "debit"
        ):
            return False
        return True

    def is_card_active(
        self,
        card_number: int,
    ) -> bool:

        card_info = self.__debit_card_dao.get_info(card_number)
        if card_info != None:
            print(card_info)
            if card_info.get("card_status") == "Active":
                return True
        return False

    def is_valid_card_number(self, card_number: any) -> bool:
        if is_int(card_number) and len(str(card_number)) == 12:
            return True
        return False

    def is_valid_transaction_type(self, value: str) -> bool:
        if value == "credit" or value == "debit":
            return True
        return False

    def transact(
        self, card_transaction_request: CardTransactionRequest, transaction_type: str
    ) -> dict:
        balance = 0
        card_info = self.__debit_card_dao.get_info(card_transaction_request.card_number)
        balance = card_info.get("balance")

        if transaction_type == "debit":
            balance -= card_transaction_request.amount
        elif transaction_type == "credit":
            balance += card_transaction_request.amount

        new_info = {
            "transaction_date": str(datetime.datetime.now()),
            "card_number": card_transaction_request.card_number,
            "description": card_transaction_request.description,
            "transaction_type": transaction_type,
            "amount": card_transaction_request.amount,
            "balance": balance,
        }

        if self.__debit_card_transaction_dao.append_content(
            new_info
        ) and self.update_card_info(
            card_transaction_request.card_number, "balance", balance
        ):
            return new_info
        return None
