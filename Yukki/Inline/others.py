from pyrogram.types import (CallbackQuery, InlineKeyboardButton,
                            InlineKeyboardMarkup, InputMediaPhoto, Message)

from Yukki import db_mem


def others_markup(videoid, user_id):
    if videoid not in db_mem:
        db_mem[videoid] = {}
    db_mem[videoid]["check"] = 1
    buttons = [
        [
            InlineKeyboardButton(text="▷", callback_data=f"resumecb"),
            InlineKeyboardButton(text="II", callback_data=f"pausecb"),
            InlineKeyboardButton(text="‣‣I", callback_data=f"skipcb"),
            InlineKeyboardButton(text="▢", callback_data=f"stopcb"),
        ],
        [
                InlineKeyboardButton(text="ʏᴏᴜʀ ᴘʟᴀʏʟɪsᴛ" callback_data=f"playlist {videoid}|{user_id}"),
                InlineKeyboardButton(text="ɢʀᴏᴜᴘ ᴘʟᴀʏʟɪsᴛ",callback_data=f"group_playlist {videoid}|{user_id}")
        ],
        [
            InlineKeyboardButton(
                text="ɢᴇᴛ ᴀᴜᴅɪᴏ",
                callback_data=f"gets audio|{videoid}|{user_id}",
            ),
            InlineKeyboardButton(
                text="ɢᴇᴛ ᴠɪᴅᴇᴏ",
                callback_data=f"gets video|{videoid}|{user_id}",
            ),
        ],
        [
            InlineKeyboardButton(
                text=" ʙᴀᴄᴋ",
                callback_data=f"pr_go_back_timer {videoid}|{user_id}",
            )
        ],
    ]
    return buttons


def download_markup(videoid, user_id):
    buttons = [
        [
            InlineKeyboardButton(
                text="ɢᴇᴛ ᴀᴜᴅɪᴏ",
                callback_data=f"gets audio|{videoid}|{user_id}",
            ),
            InlineKeyboardButton(
                text="ɢᴇᴛ ᴠɪᴅᴇᴏ",
                callback_data=f"gets video|{videoid}|{user_id}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="ʙᴀᴄᴋ", callback_data=f"goback {videoid}|{user_id}"
            )
        ],
    ]
    return buttons