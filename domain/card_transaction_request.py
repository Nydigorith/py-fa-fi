from pydantic import BaseModel, Field

class CardTransactionRequest(BaseModel):
    card_number:int  = Field(description="Card Number", default=123456789012)
    description:str = Field(description="Transaction Description", default="Check Deposit")
    amount: float = Field(amount="Amount", gt=0)