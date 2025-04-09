from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes, CallbackContext

async def say_hello(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello World!")

async def buscar(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if context.args:
        await update.message.reply_text(context.args[0])
    else:
        await update.message.reply_text("Por favor, especifica el término de búsqueda.")

async def menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton(text="Solo Compras", callback_data="solo Compras"),
         InlineKeyboardButton(text="Solo Ventas", callback_data="solo Ventas")],
        [InlineKeyboardButton(text="Buscar compras y ventas", callback_data="compras y ventas")]
    ])
    await update.message.reply_text("¿Qué tipo de operaciones de trading te gustaría que se realicen?", reply_markup=keyboard)

async def button_controller(update: Update, context: CallbackContext):
    query = update.callback_query
    await query.answer(text=f"ha seleccionado la opción {query.data}", show_alert=True)
    await query.message.reply_text(f"ha seleccionado la opción {query.data}")