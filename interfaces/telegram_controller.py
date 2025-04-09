from telegram import Update
from telegram.ext import ContextTypes

from use_cases.trading_preference import SetTradingPreferenceInteractor
from use_cases.trading_preference import GetTradingPreferenceInteractor
from interfaces.telegram_presenter import TelegramPresenter

class TelegramController:
    def __init__(self, set_preference_interactor: SetTradingPreferenceInteractor,
                 get_preference_interactor: GetTradingPreferenceInteractor,
                 presenter: TelegramPresenter):
        self.set_preference_interactor = set_preference_interactor
        self.get_preference_interactor = get_preference_interactor
        self.presenter = presenter

    async def handle_hello(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        await self.presenter.present_hello(update)

    async def handle_buscar(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        if context.args:
            await self.presenter.present_buscar_result(update, context.args[0])
        else:
            await self.presenter.present_buscar_prompt(update)

    async def handle_menu(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        await self.presenter.present_menu(update)

    async def handle_button_click(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        query = update.callback_query
        user_id = query.from_user.id
        preference = query.data.split(" ")[-1].lower() # Extract "compras" or "ventas"
        result_message = await self.set_preference_interactor.execute(user_id, preference)
        await self.presenter.present_preference_set(query, result_message)