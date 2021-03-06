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
HOME_TEXT = "**š Hai [{}](tg://user?id={})**, \n\nSaya **KGVideoStream**. \nSaya Dapat Melakukan Streaming Langsung, Radio, Video YouTube & File Video Telegram Di Obrolan Suara channel & Grup Telegram ! \n\nšššššššæ š½š @knsgnwn"
HELP_TEXT = """
ļøš·ļø --**Setting Up**-- :

\u2022 Mulai obrolan suara di saluran atau grup Anda.
\u2022 Tambahkan bot dan akun pengguna dalam obrolan dengan hak admin.
\u2022 Gunakan /stream [youtube link] atau /stream [live stream link] atau /stream sebagai balasan ke file video.

š·ļøļø --**Perintah Umum**-- :

\u2022 `/start` - mulai bot
\u2022 `/help` - tampilkan pesan bantuan

š·ļøļø --**Perintah Khusus Admin**-- :

\u2022 `/radio` - mulai streaming radio
\u2022 `/stream` - mulai streaming video
\u2022 `/endstream` - hentikan streaming video

šššššššæ š½š @knsgnwn
"""


@Client.on_callback_query()
async def cb_handler(client: Client, query: CallbackQuery):
    if query.data=="help":
        buttons = [
            [
                InlineKeyboardButton("É¢Źį“į“į“", url="https://t.me/KGSupportgroup"),
                InlineKeyboardButton("į“Źį“É“É“į“Ź", url="https://t.me/rakasupport"),
            ],
            [
                InlineKeyboardButton("į“į“į“ į“Źį“į“į“Ź", url="https://t.me/knsgnwn"),
                InlineKeyboardButton("sį“į“Źį“į“ į“į“į“į“", url="https://Xhamster.com"),
            ],
            [
                InlineKeyboardButton("Źį“į“į“", callback_data="home"),
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
                InlineKeyboardButton("āį“į“į“ į“į“ į“į“ É¢Źį“į“į“", url=f"https://t.me/{USERNAME}?startgroup=true"),
            ],
            [
                InlineKeyboardButton("É¢Źį“į“į“", url="https://t.me/KGSupportgroup"),
                InlineKeyboardButton("į“Źį“É“É“į“Ź", url="https://t.me/rakasupport"),
            ],
            [
                InlineKeyboardButton("į“į“į“ į“Źį“į“į“Ź", url="https://t.me/knsgnwn"),
                InlineKeyboardButton("sį“į“Źį“į“ į“į“į“į“", url="https://Xhamster.com"),
            ],
            [
                InlineKeyboardButton("āŹį“į“” į“į“ į“sį“", callback_data="help"),
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
                InlineKeyboardButton("āį“į“į“ į“į“ į“į“ É¢Źį“į“į“", url=f"https://t.me/{USERNAME}?startgroup=true"),
            ],
            [
                InlineKeyboardButton("É¢Źį“į“į“", url="https://t.me/KGSupportgroup"),
                InlineKeyboardButton("į“Źį“É“É“į“Ź", url="https://t.me/rakasupport"),
            ],
            [
                InlineKeyboardButton("į“į“į“ į“Źį“į“į“Ź", url="https://t.me/knsgnwn"),
                InlineKeyboardButton("sį“į“Źį“į“ į“į“į“į“", url="https://Xhmaster.com"),
            ],
            [
                InlineKeyboardButton("āŹį“į“” į“į“ į“sį“", callback_data="help"),
            ]
            ]
    reply_markup = InlineKeyboardMarkup(buttons)
    await message.reply_text(text=HOME_TEXT.format(message.from_user.first_name, message.from_user.id), reply_markup=reply_markup)

@Client.on_message(filters.command(["help", f"help@{USERNAME}"]) & (filters.chat(CHAT_ID) | filters.private))
async def help(client, message):
    buttons = [
            [
                InlineKeyboardButton("É¢Źį“į“į“", url="https://t.me/KGSupportgroup"),
                InlineKeyboardButton("į“Źį“É“É“į“Ź", url="https://t.me/rakasupport"),
            ],
            [
                InlineKeyboardButton("į“į“į“ į“Źį“į“į“Ź", url="https://t.me/knsgnwn"),
                InlineKeyboardButton("sį“į“Źį“į“ į“į“į“į“", url="https://Xhamster.com"),
            ],
            [
                InlineKeyboardButton("Źį“į“į“", callback_data="home"),
            ]
            ]
    reply_markup = InlineKeyboardMarkup(buttons)
    await message.reply_text(text=HELP_TEXT, reply_markup=reply_markup)
