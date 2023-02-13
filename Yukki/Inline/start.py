from pyrogram.types import (CallbackQuery, InlineKeyboardButton,
                            InlineKeyboardMarkup, InputMediaPhoto, Message)

from config import MUSIC_BOT_NAME, SUPPORT_CHANNEL, SUPPORT__GROUP
from Yukki import BOT_USERNAME


def setting_markup():
    buttons = [
        [
            InlineKeyboardButton(text="ᴀᴜᴅɪᴏ ǫᴜᴀʟɪᴛʏ", callback_data="AQ"),
            InlineKeyboardButton(text="ᴀᴜᴅɪᴏ ᴠᴏʟᴜᴍᴇ", callback_data="AV"),
        ],
        [
            InlineKeyboardButton(
                text="ᴀᴜᴛʜᴏʀɪᴢᴇᴅ ᴜsᴇʀs", callback_data="AU"
            ),
            InlineKeyboardButton(
                text="ᴅᴀsʜʙᴏᴀʀᴅ", callback_data="Dashboard"
            ),
        ],
        [
            InlineKeyboardButton(text="ᴄʟᴏsᴇ", callback_data="close"),
        ],
    ]
    return f"**{BOT_NAME} Settings**", buttons


def start_pannel():
    if not SUPPORT_CHANNEL and not SUPPORT_GROUP:
        buttons = [
            [
                InlineKeyboardButton(
                    text="sᴇᴛᴛɪɴɢs", callback_data="settingm"
                )
            ],
        ]
        return f"**This is {BOT_NAME}**", buttons
    if not SUPPORT_CHANNEL and SUPPORT_GROUP:
        buttons = [
            [
                InlineKeyboardButton(
                    text="sᴇᴛᴛɪɴɢs", callback_data="settingm"
                )
            ],
            [
                InlineKeyboardButton(
                    text="sᴜᴘᴘᴏʀᴛ", url=f"https://t.me/{SUPPORT_SUPPORT_GROUP}"
                ),
            ],
        ]
        return f"**This is {BOT_NAME}*", buttons
    if SUPPORT_CHANNEL and not SUPPORT_GROUP:
        buttons = [
            [
                InlineKeyboardButton(
                    text="sᴇᴛᴛɪɴɢs", callback_data="settingm"
                )
            ],
            [
                InlineKeyboardButton(
                    text=" ᴅᴏɴᴀsɪ ❤️", url=f"https://t.me/Riizzvbss"
                ),
            ],
        ]
        return f"**This is {BOT_NAME}**", buttons
    if SUPPORT_CHANNEL and SUPPORT_GROUP:
        buttons = [
            [
                InlineKeyboardButton(
                    text="sᴇᴛᴛɪɴɢs", callback_data="settingm"
                )
            ],
            [
                InlineKeyboardButton(
                    text="ᴅᴏɴᴀsɪ ❤️", url=f"https://t.me/Riizzvbss"
                ),
                InlineKeyboardButton(
                    text="sᴜᴘᴘᴏʀᴛ", url=f"https://t.me/{SUPPORT_GROUP}"
                ),
            ],
        ]
        return f"**This is {BOT_NAME}**", buttons


def private_panel():
    if not SUPPORT_CHANNEL and not SUPPORT_GROUP:
        buttons = [
            [
                InlineKeyboardButton(
                    "➕ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘs",
                    url=f"https://t.me/{BOT_USERNAME}?startSUPPORT_GROUP=true",
                )
            ],
        ]
        return f"**This is {BOT_NAME}**", buttons
    if not SUPPORT_CHANNEL and SUPPORT_GROUP:
        buttons = [
            [
                InlineKeyboardButton(
                    "➕ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴏs",
                    url=f"https://t.me/{BOT_USERNAME}?startSUPPORT_GROUP=true",
                )
            ],
            [
                InlineKeyboardButton(
                    text="sᴜᴘᴘᴏʀᴛ", url=f"https://t.me/{SUPPORT_GROUP}"
                ),
            ],
        ]
        return f"**This is {BOT_NAME}*", buttons
    if SUPPORT_CHANNEL and not SUPPORT_GROUP:
        buttons = [
            [
                InlineKeyboardButton(
                    "➕ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘs",
                    url=f"https://t.me/{BOT_USERNAME}?startSUPPORT_GROUP=true",
                )
            ],
            [
                InlineKeyboardButton(
                    text="ᴅᴏɴᴀsɪ ❤️", url=f"https://t.me/Riizzvbss"
                ),
            ],
        ]
        return f"**This is {BOT_NAME}**", buttons
    if SUPPORT_CHANNEL and SUPPORT_GROUP:
        buttons = [
            [
                InlineKeyboardButton(
                    "➕ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘs",
                    url=f"https://t.me/{BOT_USERNAME}?startSUPPORT_GROUP=true",
                )
            ],
            [
                InlineKeyboardButton(
                    text="ᴅᴏɴᴀsɪ ❤️", url=f"https://t.me/Riizzvbss"
                ),
                InlineKeyboardButton(
                    text="sᴜᴘᴘᴏʀᴛ", url=f"https://t.me/{SUPPORT_GROUP}"
                ),
            ],
        ]
        return f"**This is {BOT_NAME}**", buttons


def setting_markup():
    buttons = [
        [
            InlineKeyboardButton(text="ᴀᴜᴅɪᴏ ǫᴜᴀʟɪᴛʏ", callback_data="AQ"),
            InlineKeyboardButton(text="ᴀᴜᴅɪᴏ ᴠᴏʟᴜᴍᴇ", callback_data="AV"),
        ],
        [
            InlineKeyboardButton(
                text="ᴀᴜᴛʜᴏʀɪᴢᴇᴅ ᴜsᴇʀs", callback_data="AU"
            ),
            InlineKeyboardButton(
                text="ᴅᴀsʜʙᴏᴀʀᴅ", callback_data="Dashboard"
            ),
        ],
        [
            InlineKeyboardButton(text="ᴄʟᴏsᴇ", callback_data="close"),
        ],
    ]
    return f"**{BOT_NAME} Settings**", buttons


def volmarkup():
    buttons = [
        [
            InlineKeyboardButton(
                text="ʀᴇsᴇᴛ ᴀᴜᴅɪᴏ ᴠᴏʟᴜᴍᴇ", callback_data="HV"
            )
        ],
        [
            InlineKeyboardButton(text="ʟᴏᴡ ᴠᴏʟ", callback_data="LV"),
            InlineKeyboardButton(text="ᴍᴇᴅɪᴜᴍ ᴠᴏʟ", callback_data="MV"),
        ],
        [
            InlineKeyboardButton(text="ʜɪɢʜ ᴠᴏʟ", callback_data="HV"),
            InlineKeyboardButton(text="ᴀᴍᴘʟɪғɪᴇᴅ ᴠᴏʟ", callback_data="VAM"),
        ],
        [
            InlineKeyboardButton(
                text="ᴄᴜsᴛᴏᴍ ᴠᴏʟᴜᴍᴇ", callback_data="Custommarkup"
            )
        ],
        [InlineKeyboardButton(text="ʙᴀᴄᴋ", callback_data="settingm")],
    ]
    return f"**{BOT_NAME} Settings**", buttons


def custommarkup():
    buttons = [
        [
            InlineKeyboardButton(text="+10", callback_data="PTEN"),
            InlineKeyboardButton(text="-10", callback_data="MTEN"),
        ],
        [
            InlineKeyboardButton(text="+25", callback_data="PTF"),
            InlineKeyboardButton(text="-25", callback_data="MTF"),
        ],
        [
            InlineKeyboardButton(text="+50", callback_data="PFZ"),
            InlineKeyboardButton(text="-50", callback_data="MFZ"),
        ],
        [InlineKeyboardButton(text="ᴄᴜsᴛᴏᴍ ᴠᴏʟᴜᴍᴇ", callback_data="AV")],
    ]
    return f"**{BOT_NAME} Settings**", buttons


def usermarkup():
    buttons = [
        [
            InlineKeyboardButton(text="ᴇᴠʀʏᴏɴᴇ", callback_data="EVE"),
            InlineKeyboardButton(text="ᴀᴅᴍɪɴs", callback_data="AMS"),
        ],
        [
            InlineKeyboardButton(
                text="ᴀᴜᴛʜᴏʀɪᴢᴇᴅ ᴜsᴇʀ ʟɪsᴛ", callback_data="USERLIST"
            )
        ],
        [InlineKeyboardButton(text="ʙᴀᴄᴋ", callback_data="settingm")],
    ]
    return f"**{BOT_NAME} Settings**", buttons


def dashmarkup():
    buttons = [
        [
            InlineKeyboardButton(text="ᴜᴘᴛɪᴍᴇ", callback_data="UPT"),
            InlineKeyboardButton(text="ʀᴀᴍ", callback_data="RAT"),
        ],
        [
            InlineKeyboardButton(text="ᴄᴘᴜ", callback_data="CPT"),
            InlineKeyboardButton(text="ᴅɪsᴋ", callback_data="DIT"),
        ],
        [InlineKeyboardButton(text="ʙᴀᴄᴋ", callback_data="settingm")],
    ]
    return f"**{BOT_NAME} Settings**", buttons