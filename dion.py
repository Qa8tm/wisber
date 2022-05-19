# Copyright (C) 2022 GNU GENERAL PUBLIC LICENCE
#
# Licensed under the GNU GENERAL PUBLIC LICENCE, Version 3 (the "License");
# you may not use this file except in compliance with the License.
#
# Copyright (C) 2022 github.com/SeorangDion for WhisperBot repo
# FROM WhisperBot <https://github.com/SeorangDion/WhisperBot>
# t.me/DionProjects & t.me/DionSupport
# Don't remove this credits!

import logging

from telethon import events
from telethon import TelegramClient, Button
from telethon.tl.functions.users import GetFullUserRequest as us
from dion_config import *


logging.basicConfig(level=logging.INFO)


dion = TelegramClient(
        "whisper",
        api_id=DIONAPI_KEY,
        api_hash=DIONAPI_HASH
        ).start(
                bot_token=DION_TOKEN
                )
db = {}

@dion.on(events.NewMessage(pattern="^[!?/]start$"))
async def stsrt(event):
    await event.reply(
            START_TEXT)


@dion.on(events.NewMessage(pattern="^[!?/]help$"))
async def helep(event):
    await event.reply(
            HELP_TEXT,
            buttons=[
                [Button.switch_inline("استعملني في الكروبات", query="")]
                ]
            )


@dion.on(events.NewMessage(pattern="^[!?/]Source$"))
async def repos(event):
    await event.reply(
            REPO_TEXT,
            buttons=[
                [Button.url("اضغط هنا", "T.ME/ADWSL")]
                ]
            )


@dion.on(events.InlineQuery())
async def die(event):
    if len(event.text) != 0:
        return
    me = (await dion.get_me()).username

@dion.on(events.InlineQuery(pattern=""))
async def inline(event):
    me = (await dion.get_me()).username
    try:
        inp = event.text.split(None, 1)[1]
        msg, user = inp.split("")
    except IndexError:
        await event.answer(
                [],
                switch_pm=f"@{me} [اليوزر] [الرساله]",
                switch_pm_param="start"
                )
    except ValueError:
        await event.answer(
                [],
                switch_pm=f"ارسل همسه!",
                switch_pm_param="start"
                )
    try:
        ui = await dion(us(user))
    except BaseException:
        await event.answer(
                [],
                switch_pm="خطأ في  الايدي/اليوزر",
                switch_pm_param="start"
                )
        return
    db.update({"user_id": ui.user.id, "msg": msg, "gideon": event.sender.id})
    dion_text = f"""
تم ارسال همسه الى [{ui.user.first_name}](tg://user?id={ui.user.id})!
اضغط على الزر في الاسفل لرؤيه الهمسه!\n
**ملاحظه:** __فقط {ui.user.first_name} يمكنه فتح الهمسه!__
    """
    deon = event.builder.article(
            title="ارسل همسه!",
            description=f"تم التطوير بواسطه {DIONBOT_NAME}",
            url="https://t.me/K_8_U",
            text=dion_text,
            buttons=[
                [Button.inline(" رؤيه الهمسه 🔓 ", data="همسه")]
                ]
            )
    await event.answer(
            [deon],
            switch_pm="الهمسه.",
            switch_pm_param="start"
            )


@dion.on(events.CallbackQuery(data=""))
async def ws(event):
    user = int(db["user_id"])
    xflzu = [int(db["gideon"])]
    xflzu.append(user)
    if event.sender.id not in xflzu:
        await event.answer("🔐 هاي الهمسه مو الك ولكك!", alert=True)
        return
    msg = db["msg"]
    if msg == []:
        await event.anwswer(
                "احا!\nالرساله نمسحت من البوت!", alert=True)
        return
    await event.answer(msg, alert=True)


dion.run_until_disconnected()
