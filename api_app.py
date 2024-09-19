from fastapi import FastAPI
from domain.card_transaction_request import CardTransactionRequest
from domain.card_info_register_request import CardInfoRegisterRequest
from controller.debit_card_controller import DebitCardController
from domain.service_response import ServiceResponse
from domain.card_transaction_request import CardTransactionRequest
from domain.get_response import GetResponse

api = FastAPI()
controller = DebitCardController()


@api.get("/transactions/{card_number}")
def transaction_history(card_number: int):
    if not controller.is_valid_card_number(card_number):
        return ServiceResponse(
            status="fail",
            code=600,
            message="Card number must be in 12-digit format",
        )

    if not controller.is_card_number_exist(int(card_number)):
        message = "Card number does not exist"
        return ServiceResponse(code=600, message=message, status="fail")

    transactions = controller.get_transaction_history(int(card_number))
    if len(transactions) == 0:
        return GetResponse(message="No transactions found", data=[])

    return GetResponse(data=transactions)


@api.post("/register")
def register_card(card_info_request: CardInfoRegisterRequest):
    if not controller.is_valid_card_number(card_info_request.card_number):
        return ServiceResponse(
            status="fail",
            code=600,
            message="Card number must be in 12-digit format",
        )

    if not controller.is_card_number_unique(card_info_request.card_number):
        return ServiceResponse(
            status="fail",
            code=600,
            message="Card number is not unique",
        )

    data = controller.register_card(card_info_request)
    if data == None:
        return ServiceResponse(
            status="fail",
            code=600,
            message="Unable to create a new card. Please try again later",
        )

    return ServiceResponse(
        status="success", code=200, message="A new card has been created", data=data
    )


@api.post("/activate/{card_number}")
def activate_card(card_number):
    if not controller.is_valid_card_number(card_number):
        return ServiceResponse(
            status="fail",
            code=600,
            message="Card number must be in 12-digit format",
        )

    if not controller.is_card_number_exist(int(card_number)):
        return ServiceResponse(
            status="fail", code=600, message="Card number does not exist"
        )
    if controller.is_card_active(int(card_number)):
        return ServiceResponse(
            code=600,
            message="Card is already active",
            status="fail",
        )

    data = controller.activate_card(int(card_number))
    if data == None:
        return ServiceResponse(
            status="fail",
            code=600,
            message="Unable to activate card. Please try again later",
        )


    return ServiceResponse(
        status="success",
        code=200,
        data={"card_number": card_number},
        message="Card has been activated",
    )


@api.post("/transact/{transaction_type}")
def transact(card_transaction_request: CardTransactionRequest, transaction_type: str):
    if not controller.is_valid_transaction_type(transaction_type):
        return ServiceResponse(
            status="fail",
            code=600,
            message="transaction type must either be debit or credit",
        )

    if not controller.is_card_number_exist(int(card_transaction_request.card_number)):
        return ServiceResponse(
            status="fail", code=600, message="Card number does not exist"
        )

    if not controller.is_card_active(card_transaction_request.card_number):

        return ServiceResponse(
            code=600,
            message="Unable to process the transaction due to inactive card",
            status="fail",
        )

    if not controller.is_valid_transaction(card_transaction_request, transaction_type):

        return ServiceResponse(
            code=600,
            message="Unable to process the transaction due to insufficient balance",
            status="fail",
        )

    data = controller.transact(card_transaction_request, transaction_type)
    if data == None:
        return ServiceResponse(
            code=600,
            message="Unable to process the transaction. Please try again later",
            status="fail",
        )
    return ServiceResponse(
        status="success", code=200, message="Transaction successful", data=data
    )
