import socket
import time

import koyeb3
from pyrogram import filters

import config
from VIPMUSIC.core.mongo import mongodb

from .logging import LOGGER

SUDOERS = filters.user()

HAPP = None
clonedb = None
_boot_ = time.time()


def is_heroku():
    return "koyeb" in socket.getfqdn()


XCB = [
    "/",
    "@",
    ".",
    "com",
    ":",
    "git",
    "koyeb",
    "push",
    str(config.KOYEB_API_KEY),
    "https",
    str(config.KOYEB_APP_NAME),
    "HEAD",
    "master",
]


def dbb():
    global db
    global clonedb
    clonedb = {}
    db = {}


async def sudo():
    global SUDOERS
    SUDOERS.add(config.OWNER_ID)
    sudoersdb = mongodb.sudoers
    sudoers = await sudoersdb.find_one({"sudo": "sudo"})
    sudoers = [] if not sudoers else sudoers["sudoers"]
    if config.OWNER_ID not in sudoers:
        sudoers.append(config.OWNER_ID)
        await sudoersdb.update_one(
            {"sudo": "sudo"},
            {"$set": {"sudoers": sudoers}},
            upsert=True,
        )
    if sudoers:
        for user_id in sudoers:
            SUDOERS.add(user_id)
    LOGGER(__name__).info(f"🍂နို့ကြိုက်ကောင်လေး................")


def heroku():
    global HAPP
    if is_koyeb:
        if config.KOYEB_API_KEY and config.KOYEB_APP_NAME:
            try:
                KOYEB = koyeb3.from_key(config.KOYEB_API_KEY)
                HAPP = Koyeb.app(config.KOYEB_APP_NAME)
                LOGGER(__name__).info(f"🌈𝐇𝐞𝐫𝐨𝐤𝐮 𝐀𝐩𝐩 𝐍𝐚𝐦𝐞 𝐋𝐨𝐚𝐝𝐞𝐝...")
            except BaseException:
                LOGGER(__name__).warning(
                    f"🏓𝐘𝐨𝐮 𝐇𝐚𝐯𝐞 𝐍𝐨𝐭 𝐅𝐢𝐥𝐥𝐞𝐝 𝐇𝐞𝐫𝐨𝐤𝐮 𝐀𝐩𝐢 𝐊𝐞𝐲 𝐀𝐧𝐝 𝐇𝐞𝐫𝐨𝐤𝐮 𝐀𝐩𝐩 𝐍𝐚𝐦𝐞 𝐂𝐨𝐫𝐫𝐞𝐜𝐭...🙃 "
                )
