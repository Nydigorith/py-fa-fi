from pydantic import BaseModel, Field

class GetResponse(BaseModel):
    status:str = Field(description="Status Message", default="success")
    code:int= Field(description="Status code", default=200)
    data:list= Field(description="Response data" ,default=None)
   