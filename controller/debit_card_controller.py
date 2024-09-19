from bll.debit_card_bll import DebitCardBll

from domain.card_info_register_request import CardInfoRegisterRequest
from domain.card_transaction_request import CardTransactionRequest


class DebitCardController:
    def __init__(self) -> None:
        self.__debit_card_bll = DebitCardBll()

    def get_transaction_history(self, card_number: int) -> list:
        return self.__debit_card_bll.get_transaction_history(card_number)

    def register_card(self, card_info_request: CardInfoRegisterRequest) -> dict:
        return self.__debit_card_bll.register_card(card_info_request)

    def is_card_number_unique(self, card_number: int) -> bool:
        return self.__debit_card_bll.is_card_number_unique(card_number)

    def activate_card(self, card_number: int) -> dict:
        return self.__debit_card_bll.activate_card(card_number)

    def transact(
        self, card_transaction_request: CardTransactionRequest, transaction_type: str
    ) -> dict:
        return self.__debit_card_bll.transact(
            card_transaction_request, transaction_type
        )

    def is_card_number_exist(self, card_number: int) -> bool:
        return self.__debit_card_bll.is_card_number_exist(card_number)

    def is_valid_transaction(
        self, card_transaction_request: CardTransactionRequest, transaction_type: str
    ) -> bool:
        return self.__debit_card_bll.is_valid_transaction(
            card_transaction_request, transaction_type
        )

    def is_card_active(
        self,
        card_number: int,
    ) -> bool:
        return self.__debit_card_bll.is_card_active(card_number)

    def is_valid_card_number(self, card_number: any) -> bool:
        return self.__debit_card_bll.is_valid_card_number(card_number)

    def is_valid_transaction_type(self, value: str) -> bool:
        return self.__debit_card_bll.is_valid_transaction_type(value)
