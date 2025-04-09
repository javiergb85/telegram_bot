from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler
import os
from dotenv import load_dotenv
from interfaces.telegram_controller import TelegramController
from interfaces.in_memory_preference_gateway import InMemoryPreferenceGateway
from interfaces.telegram_presenter import TelegramPresenter
from use_cases.trading_preference import SetTradingPreferenceInteractor
from use_cases.trading_preference import GetTradingPreferenceInteractor

load_dotenv() 

TOKEN_TELEGRAM =  os.environ.get('TOKEN_TELEGRAM')

# Initialize Gateways
preference_gateway = InMemoryPreferenceGateway()

        # Initialize Use Case Interactors
set_preference_interactor = SetTradingPreferenceInteractor(preference_gateway)
get_preference_interactor = GetTradingPreferenceInteractor(preference_gateway)

        # Initialize Presenter
presenter = TelegramPresenter()

        # Initialize Controller
telegram_controller = TelegramController(set_preference_interactor, get_preference_interactor, presenter)

application = ApplicationBuilder().token(TOKEN_TELEGRAM).build()

        # Command Handlers (map routes to controller actions)
application.add_handler(CommandHandler("start", telegram_controller.handle_hello))
application.add_handler(CommandHandler("buscar", telegram_controller.handle_buscar))
application.add_handler(CommandHandler("menu", telegram_controller.handle_menu))

        # Callback Query Handler (map button clicks to controller actions)
application.add_handler(CallbackQueryHandler(telegram_controller.handle_button_click))

application.run_polling(allowed_updates=Update.ALL_TYPES)