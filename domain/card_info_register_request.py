from pydantic import BaseModel, Field

class CardInfoRegisterRequest(BaseModel):
    card_number:int = Field(description="Card Number", default="123456789012", gt=0)
    account_name:str  = Field(description="Account Name", default="Juan Dela Cruz")
