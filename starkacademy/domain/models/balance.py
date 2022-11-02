from pydantic import BaseModel, StrictInt


class BalanceModel(BaseModel):
    amount: StrictInt
    currency: str
    id: str
    updated: str
