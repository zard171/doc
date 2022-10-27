from typing import Union
import asyncio
from pyrogram import Client, filters
from pyrogram.errors import BadRequest
from pyrogram.types import (
    CallbackQuery,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Message,
)

from database import cur, save
from utils import create_mention, get_info_wallet, dobrosaldo, get_price
from config import BOT_LINK
from config import BOT_LINK_SUPORTE



@Client.on_message(filters.command(["start", "menu"]))
@Client.on_callback_query(filters.regex("^start$"))
async def start(c: Client, m: Union[Message, CallbackQuery]):
    user_id = m.from_user.id

    rt = cur.execute(
        "SELECT id, balance, balance_diamonds, refer FROM users WHERE id=?", [user_id]
    ).fetchone()

    if isinstance(m, Message):
        """refer = (
            int(m.command[1])
            if (len(m.command) == 2)
            and (m.command[1]).isdigit()
            and int(m.command[1]) != user_id
            else None
        )

        if rt[3] is None:
            if refer is not None:
                mention = create_mention(m.from_user, with_id=False)

                cur.execute("UPDATE users SET refer = ? WHERE id = ?", [refer, user_id])
                try:
                    await c.send_message(
                        refer,
                        text=f"<b>O usuário {mention} se tornou seu referenciado.</b>",
                    )
                except BadRequest:
                    pass"""

    kb = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton("🎟️ Comprar Docs", callback_data="comprar_doc"),
            ],
            
            [
                InlineKeyboardButton("💸 Add saldo", callback_data="add_saldo"),
                InlineKeyboardButton("👤 Suas informações", callback_data="user_info"),
                
            ],
              [
                InlineKeyboardButton(
                    "🛒 Buscar docs por Nome",
                    switch_inline_query_current_chat="buscar_doc A",
                ),],
              [
                InlineKeyboardButton(
                    "☂️ Buscar docs por Score",
                    switch_inline_query_current_chat="buscar_score 999",
                ),]
            
        ]
    )

    bot_logo, news_channel, support_user = cur.execute(
        "SELECT main_img, channel_user, support_user FROM bot_config WHERE ROWID = 0"
    ).fetchone()

    start_message = f"""<a href='{bot_logo}'>&#8204</a>Olá, Bem vindo(a) a StoreDocs. 🇧🇷🇧🇷🇧🇷

Loja virtual de documentos como:

CNH & RG


☂ REGRAS  SOBRE A COMPRA 

❇️ TODOS DOCUMENTOS VEM COM FOTO

❇️ A FOTO PODE OU NÃO ESTAR SEGURANDO O DOCUMENTO

❇️ O DOCUMENTO COMPRADO PODE SER RG OU CNH (ALEATÓRIO)

❇️ E SÃO DOCUMENTOS VIRGENS E (NUNCA VENDIDOS ANTES)

Valores dos documentos👇 
CNH: R$ {await get_price("docs", "cnh")}
RG: R$ {await get_price("docs", "rg")}
Por unidade ⚠️

━━━━━━━━━━━━━━━━━
🔰 GRUPO: @null
🔰 REFERÊNCIA: @null
🔰 SUPORTE: @null
━━━━━━━━━━━━━━━━━

{get_info_wallet(user_id)}

💬 Dúvidas?
<a href='https://t.me/{BOT_LINK_SUPORTE}'>SUPORTE</a>
"""

    if isinstance(m, CallbackQuery):
        send = m.edit_message_text
    else:
        send = m.reply_text
    save()
    await send(start_message, reply_markup=kb)
