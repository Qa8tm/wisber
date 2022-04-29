# Copyright (C) 2022 @SeorangDion for WhisperBot repo
# FROM WhisperBot <https://github.com/SeorangDion/WhisperBot>
# t.me/DionProjects & t.me/DionSupport
# Don't remove this credits!

import os

# Config Vars
DIONAPI_HASH = "23c93aa64d16911f521bd0b16291af57"
DIONAPI_KEY = 14624642
DIONBOT_NAME = os.environ.get("BOT_NAME", None) # Your bot name, example: Dion Bot
BOT_USERNAME = os.environ.get("BOT_USERNAME", None) # Your bot username with (@), example: @WhisperXRobot
DION_TOKEN = os.environ.get("TOKEN", None) # Your token bot, get one from t.me/botfather

# Config Text
START_TEXT = f"**مرحبا, انا اسمي {DIONBOT_NAME}!**\n\nاكتب /help لرؤية طريقة استخدامي!\nاكتب /repo لطريقة عمل بوت مشابه لـ {DIONBOT_NAME}."

HELP_TEXT = f"**• طريقة استعمال بوت {DIONBOT_NAME}:**\n\nاضغط الزر في الاسفل أو\n\nاكتب __{BOT_USERNAME} همسه <يوزر المرسل له> | <النص>__\nمثال: `{BOT_USERNAME} همسه @Xflzu | مرحبا!`"

REPO_TEXT = f"اضغط في الاسفل لصنع بوت مشابه لبوت {DIONBOT_NAME}"
