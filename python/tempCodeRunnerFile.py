import logging
import os
import tempfile
from datetime import datetime

import google.generativeai as genai
from telegram import BotCommand, KeyboardButton, ReplyKeyboardMarkup, Update
from telegram.constants import ChatAction
from telegram.ext import (
    Application,
    CallbackContext,
    CommandHandler,
    ContextTypes,
    ConversationHandler,
    MessageHandler,
    filters,
)

from prompt import get_prompt

gemini_api_key = "AIzaSyDzxWf5S1eAvzmg4Y8QEOeedNNL0QO0s7A"
BOT_TOKEN = "7624145954:AAEqP9wLVHxxSQEGcnKmA5zw7aqIe1RKaXo"

genai.configure(api_key=gemini_api_key)

generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 40,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(model_name="gemini-1.5-flash", generation_config=generation_config)

chat_session = model.start_chat(history=[])

logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)
logger = logging.getLogger(__name__)

WAITING_FOR_JSON, WAITING_FOR_MODEL_NAME = range(2)


# Helper function to convert JSON to Dart
def json_to_dart(json_string: str, class_name: str = "MyModel") -> str:
    try:
        response = chat_session.send_message(get_prompt(json=json_string, model_name=class_name))
        return response.text
    except Exception as e:
        logger.error(f"Error in json_to_dart: {e}")
        return "Invalid JSON! Please ensure the JSON is well-formed."


def get_main_keyboard():
    """Create the main keyboard."""
    keyboard = [[KeyboardButton("Convert JSON to Dart 🎯")]]
    return ReplyKeyboardMarkup(keyboard, resize_keyboard=True)


# Start command handler
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    greeting = f"Hi {user.first_name}! " if user else "Hi! "
    await update.message.reply_text(
        greeting + "This bot converts JSON data into Dart \U0001F3AF code.\n\nPress 'Convert JSON to Dart' to start!",
        reply_markup=get_main_keyboard(),
    )


async def handle_main_menu(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Handle the main menu button press."""
    if update.message.text == "Convert JSON to Dart 🎯":
        keyboard = [[KeyboardButton("Done")]]
        reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True, one_time_keyboard=True)
        await update.message.reply_text(
            "Send me your JSON data. When finished, press 'Done'.",
            reply_markup=reply_markup,
        )
        context.user_data["json_parts"] = []
        return WAITING_FOR_JSON
    return ConversationHandler.END


# Handle JSON input
async def handle_json(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Handle the JSON input from the user."""
    user_message = update.message.text
    logger.info(f"Received JSON part: {user_message}")

    if user_message.lower() == "done":
        if not context.user_data["json_parts"]:
            await update.message.reply_text("You haven't sent any JSON data yet. Please send your JSON data.")
            return WAITING_FOR_JSON

        await update.message.reply_text("Great! Now, send me the model name for the Dart class.", reply_markup=None)
        return WAITING_FOR_MODEL_NAME

    # Add part to the accumulated JSON
    context.user_data["json_parts"].append(user_message)
    return WAITING_FOR_JSON


# Updated handle_model_name function
async def handle_model_name(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    model_name = update.message.text.strip()
    full_json = "".join(context.user_data["json_parts"])
    await context.bot.send_chat_action(chat_id=update.effective_chat.id, action=ChatAction.TYPING)

    try:
        # Convert JSON to Dart
        dart_code = json_to_dart(full_json, class_name=model_name)

        # Check the length of the response
        if len(dart_code) > 4096:
            await update.message.reply_text("The Dart code is too long, so I'll send it as a file.")

            # Create a temporary file to store the Dart code
            with tempfile.NamedTemporaryFile(delete=False, suffix=".dart", mode="w") as temp_file:
                dart_code = dart_code.replace("```dart", "").replace("```", "")
                temp_file.write(dart_code)
                temp_file_path = temp_file.name

            # Send the file to the user
            await context.bot.send_document(
                chat_id=update.effective_chat.id,
                document=open(temp_file_path, "rb"),
                reply_markup=get_main_keyboard(),
            )

            # Delete the file after sending
            os.remove(temp_file_path)
        else:
            await update.message.reply_text(
                f"Here is your Dart code:\n\n{dart_code}",
                parse_mode="Markdown",
                reply_markup=get_main_keyboard(),
            )

    except Exception as e:
        logger.error(f"Error during conversion: {e}")
        await update.message.reply_text(
            "An error occurred while processing your request. Please try again.",
            reply_markup=get_main_keyboard(),
        )

    # Clean up user data
    context.user_data.clear()
    return ConversationHandler.END


# Cancel command handler
async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Cancel the conversation."""
    await update.message.reply_text("Operation cancelled.", reply_markup=get_main_keyboard())
    context.user_data.clear()  # Clear any accumulated data
    return ConversationHandler.END


# Help command handler
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "Help: Use /start to start the bot, and press 'Convert JSON to Dart' button to convert! Use /cancel to stop at any time.",
        reply_markup=get_main_keyboard(),
    )


# To echo and log messages
async def echo_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_message = update.message.text
    user_name = update.effective_user.first_name if update.effective_user else "Unknown"
    log_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Format the date and time

    # Log the message with the date
    logger.info(f"[{log_date}] User {user_name} said: {user_message}")

    # Echo the message back to the user
    await update.message.reply_text(user_message)


def help_command(update: Update, context: CallbackContext):
    commands = [
        "/start - Start the bot",
        "/cancel - Cancel the current operation",
        "/help - Show this help message",
    ]
    update.message.reply_text("\n".join(commands))


# Main function
def main() -> None:
    """Start the bot."""
    # Initialize application
    application = Application.builder().token(BOT_TOKEN).build()

    # Define the conversation handler with states
    conv_handler = ConversationHandler(
        entry_points=[
            MessageHandler(filters.Regex("^Convert JSON to Dart 🎯$"), handle_main_menu),
            CommandHandler("convert", handle_main_menu),
        ],
        states={
            WAITING_FOR_JSON: [MessageHandler(filters.TEXT & ~filters.COMMAND, handle_json)],
            WAITING_FOR_MODEL_NAME: [MessageHandler(filters.TEXT & ~filters.COMMAND, handle_model_name)],
        },
        fallbacks=[CommandHandler("cancel", cancel)],
    )

    # Add handlers to the application
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("start", start))
    application.add_handler(conv_handler)

    # Set bot commands for the Telegram menu
    application.bot.set_my_commands(
        [
            BotCommand("start", "Start the bot"),
            BotCommand("help", "Show this help message"),
            BotCommand("convert", "Convert JSON to Dart 🎯"),
            BotCommand("cancel", "Cancel the current operation"),
        ]
    )

    # Add the echo handler for non-command messages
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo_message))

    # Run the bot with polling
    application.run_polling()


if __name__ == "__main__":
    main()


# gemini_api_key = "AIzaSyDzxWf5S1eAvzmg4Y8QEOeedNNL0QO0s7A"
# BOT_TOKEN = "7624145954:AAEqP9wLVHxxSQEGcnKmA5zw7aqIe1RKaXo"
