from entities.trading_preference import TradingPreference

class InMemoryPreferenceGateway:
    def __init__(self):
        self.preferences = {}

    async def save(self, preference: TradingPreference):
        self.preferences[preference.user_id] = preference.preference

    async def get(self, user_id: int) -> TradingPreference | None:
        preference = self.preferences.get(user_id)
        if preference:
            return TradingPreference(user_id=user_id, preference=preference)
        return None