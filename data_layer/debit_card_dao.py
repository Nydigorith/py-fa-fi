from data_layer.abstract_card_dao import AbstractCardDao
from domain.card_info_register_request import CardInfoRegisterRequest


class DebitCardDao(AbstractCardDao):
    def get_filename(self, filename="./data/card_info.json"):
        return filename
