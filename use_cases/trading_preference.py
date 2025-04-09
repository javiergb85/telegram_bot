from entities.trading_preference import TradingPreference

class SetTradingPreferenceInteractor:
    def __init__(self, preference_gateway):
        self.preference_gateway = preference_gateway

    async def execute(self, user_id: int, preference: str):
        trading_preference = TradingPreference(user_id=user_id, preference=preference)
        await self.preference_gateway.save(trading_preference)
        return f"Ha seleccionado la opción: {preference}"

# use_cases/get_trading_preference.py
from entities.trading_preference import TradingPreference

class GetTradingPreferenceInteractor:
    def __init__(self, preference_gateway):
        self.preference_gateway = preference_gateway

    async def execute(self, user_id: int) -> TradingPreference | None:
        return await self.preference_gateway.get(user_id)