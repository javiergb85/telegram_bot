from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup


class TelegramPresenter:
    async def present_hello(self, update: Update):
        await update.message.reply_text("Hello World!")

    async def present_buscar_prompt(self, update: Update):
        await update.message.reply_text("Por favor, especifica el término de búsqueda.")

    async def present_buscar_result(self, update: Update, result: str):
        await update.message.reply_text(result)

    async def present_menu(self, update: Update):
        keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton(text="Solo Compras", callback_data="has seleccionado Compras"),
             InlineKeyboardButton(text="Solo Ventas", callback_data="has seleccionado Ventas")],
            [InlineKeyboardButton(text="Buscar compras y ventas", callback_data="has seleccionado compras y ventas")]
        ])
        await update.message.reply_text("¿Qué tipo de operaciones de trading te gustaría que se realicen?", reply_markup=keyboard)

    async def present_preference_set(self, query, message: str):
        await query.answer(text=message, show_alert=True)
        await query.message.reply_text(message)
