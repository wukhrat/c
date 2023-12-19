from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="MIS KABEL"),
            KeyboardButton(text="ALUMEN KABEL"),
            KeyboardButton(text="ELEKTRIK"),
        ],
        [
            KeyboardButton(text="SUMMARY KABEL")
        ],
        [
            KeyboardButton(text="STORAGE"),
            KeyboardButton(text="QARZ"),
            KeyboardButton(text="KUSOK")
        ],
        [
            KeyboardButton(text="BOOK")
        ]
    ],
    resize_keyboard=True,
)
