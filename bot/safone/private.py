"""
VideoPlayerBot, Telegram Video Chat Bot
Copyright (c) 2021  Asm Safone <https://github.com/AsmSafone>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>
"""

import asyncio
from config import Config
from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from pyrogram.errors import MessageNotModified

CHAT_ID = Config.CHAT_ID
USERNAME = Config.BOT_USERNAME
HOME_TEXT = "**👋 Hai [{}](tg://user?id={})**, \n\nSaya **KGVideoStream**. \nSaya Dapat Melakukan Streaming Langsung, Radio, Video YouTube & File Video Telegram Di Obrolan Suara channel & Grup Telegram ! \n\n𝙋𝙊𝙒𝙀𝙍𝙀𝘿 𝘽𝙔 @knsgnwn"
HELP_TEXT = """
️🏷️ --**Setting Up**-- :

\u2022 Mulai obrolan suara di saluran atau grup Anda.
\u2022 Tambahkan bot dan akun pengguna dalam obrolan dengan hak admin.
\u2022 Gunakan /stream [youtube link] atau /stream [live stream link] atau /stream sebagai balasan ke file video.

🏷️️ --**Perintah Umum**-- :

\u2022 `/start` - mulai bot
\u2022 `/help` - tampilkan pesan bantuan

🏷️️ --**Perintah Khusus Admin**-- :

\u2022 `/radio` - mulai streaming radio
\u2022 `/stream` - mulai streaming video
\u2022 `/endstream` - hentikan streaming video

𝙋𝙊𝙒𝙀𝙍𝙀𝘿 𝘽𝙔 @knsgnwn
"""


@Client.on_callback_query()
async def cb_handler(client: Client, query: CallbackQuery):
    if query.data=="help":
        buttons = [
            [
                InlineKeyboardButton("ɢʀᴏᴜᴘ", url="https://t.me/KGSupportgroup"),
                InlineKeyboardButton("ᴄʜᴀɴɴᴇʟ", url="https://t.me/rakasupport"),
            ],
            [
                InlineKeyboardButton("ᴅᴇᴠᴇʟᴏᴘᴇʀ", url="https://t.me/knsgnwn"),
                InlineKeyboardButton("sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ", url="https://Xhamster.com"),
            ],
            [
                InlineKeyboardButton("ʙᴀᴄᴋ", callback_data="home"),
            ]
            ]
        reply_markup = InlineKeyboardMarkup(buttons)
        try:
            await query.edit_message_text(
                HELP_TEXT,
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass

    elif query.data=="home":
        buttons = [
            [
                InlineKeyboardButton("➕ᴀᴅᴅ ᴍᴇ ᴛᴏ ɢʀᴏᴜᴘ", url=f"https://t.me/{USERNAME}?startgroup=true"),
            ],
            [
                InlineKeyboardButton("ɢʀᴏᴜᴘ", url="https://t.me/KGSupportgroup"),
                InlineKeyboardButton("ᴄʜᴀɴɴᴇʟ", url="https://t.me/rakasupport"),
            ],
            [
                InlineKeyboardButton("ᴅᴇᴠᴇʟᴏᴘᴇʀ", url="https://t.me/knsgnwn"),
                InlineKeyboardButton("sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ", url="https://Xhamster.com"),
            ],
            [
                InlineKeyboardButton("❔ʜᴏᴡ ᴛᴏ ᴜsᴇ", callback_data="help"),
            ]
            ]
        reply_markup = InlineKeyboardMarkup(buttons)
        try:
            await query.edit_message_text(
                HOME_TEXT.format(query.from_user.first_name, query.from_user.id),
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass

    elif query.data=="close":
        try:
            await query.message.delete()
            await query.message.reply_to_message.delete()
        except:
            pass


@Client.on_message(filters.command(["start", f"start@{USERNAME}"]) & (filters.chat(CHAT_ID) | filters.private))
async def start(client, message):
    buttons = [
            [
                InlineKeyboardButton("➕ᴀᴅᴅ ᴍᴇ ᴛᴏ ɢʀᴏᴜᴘ", url=f"https://t.me/{USERNAME}?startgroup=true"),
            ],
            [
                InlineKeyboardButton("ɢʀᴏᴜᴘ", url="https://t.me/KGSupportgroup"),
                InlineKeyboardButton("ᴄʜᴀɴɴᴇʟ", url="https://t.me/rakasupport"),
            ],
            [
                InlineKeyboardButton("ᴅᴇᴠᴇʟᴏᴘᴇʀ", url="https://t.me/knsgnwn"),
                InlineKeyboardButton("sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ", url="https://Xhmaster.com"),
            ],
            [
                InlineKeyboardButton("❔ʜᴏᴡ ᴛᴏ ᴜsᴇ", callback_data="help"),
            ]
            ]
    reply_markup = InlineKeyboardMarkup(buttons)
    await message.reply_text(text=HOME_TEXT.format(message.from_user.first_name, message.from_user.id), reply_markup=reply_markup)

@Client.on_message(filters.command(["help", f"help@{USERNAME}"]) & (filters.chat(CHAT_ID) | filters.private))
async def help(client, message):
    buttons = [
            [
                InlineKeyboardButton("ɢʀᴏᴜᴘ", url="https://t.me/KGSupportgroup"),
                InlineKeyboardButton("ᴄʜᴀɴɴᴇʟ", url="https://t.me/rakasupport"),
            ],
            [
                InlineKeyboardButton("ᴅᴇᴠᴇʟᴏᴘᴇʀ", url="https://t.me/knsgnwn"),
                InlineKeyboardButton("sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ", url="https://Xhamster.com"),
            ],
            [
                InlineKeyboardButton("ʙᴀᴄᴋ", callback_data="home"),
            ]
            ]
    reply_markup = InlineKeyboardMarkup(buttons)
    await message.reply_text(text=HELP_TEXT, reply_markup=reply_markup)
