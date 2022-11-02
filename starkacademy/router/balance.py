from fastapi import APIRouter, status
from starkacademy.application.service.balance import BalanceService
from starkacademy.domain.models.response import ResponseRequestModel
from starkacademy.domain.models.balance import BalanceModel

# Service Definitions
balance_service = BalanceService()

# router definitions
balance_router = APIRouter(prefix="/balance", tags=["Balance"])


@balance_router.get("/",
                    status_code=status.HTTP_200_OK,
                    response_description="Balance Account",
                    responses={
                        500: {'model': ResponseRequestModel, 'description': 'Internal server Error'}
                    },
                    response_model=BalanceModel
                    )
async def balance_getbalance():
    return balance_service.get_balance()
