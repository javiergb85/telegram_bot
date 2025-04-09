class TradingPreference:
    def __init__(self, user_id: int, preference: str = None):
        self.user_id = user_id
        self.preference = preference