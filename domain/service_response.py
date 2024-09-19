from pydantic import BaseModel, Field


class ServiceResponse(BaseModel):
    status: str = Field(description="Status Message", default="success")
    code: int = Field(description="Status code", default=200)
    data: dict = Field(description="Response data", default=None)
    message: str = Field(description="Additional information", default="")
