
import asyncio
import os
from telethon.tl.functions.users import GetFullUserRequest
from telethon import events, Button
from telethon.tl.custom import button
from DEEPAK import BOT0, BOT1, BOT2, BOT3, BOT4, BOT5, BOT6, BOT7, BOT8, BOT9, ALIVE_PIC, OWNER_ID

DEADLY_IMG = ALIVE_PIC if ALIVE_PIC else "https://te.legra.ph/file/12aa46a2c6da5ec20f8ac.jpg"

Deadly_Button = [
        [
        Button.url("•ᴄʜᴀɴɴᴇʟ•", "https://t.me/Broken_Heart_72"),
        Button.url("•sᴜᴘᴘᴏʀᴛ•", "https://t.me/Bhutiya_Haveli")
        ],
        [
        Button.url("•ᴏᴡɴᴇʀ•", "https://t.me/OFFICIALHACKERERA")
        ]
        ]

DeadlyX_Button = [
        [
        Button.url("•ᴄʜᴀɴɴᴇʟ•", "https://t.me/Broken_Heart_72"),
        Button.url("•sᴜᴘᴘᴏʀᴛ•", "https://t.me/Bhutiya_Haveli")
        ],
        [
        Button.url("•ᴏᴡɴᴇʀ•", "https://t.me/OFFICIALHACKERERA")
        ]
        ]
        
        
#USERS 


@BOT0.on(events.NewMessage(pattern="/start"))
@BOT1.on(events.NewMessage(pattern="/start"))
@BOT2.on(events.NewMessage(pattern="/start"))
@BOT3.on(events.NewMessage(pattern="/start"))
@BOT4.on(events.NewMessage(pattern="/start"))
@BOT5.on(events.NewMessage(pattern="/start"))
@BOT6.on(events.NewMessage(pattern="/start"))
@BOT7.on(events.NewMessage(pattern="/start"))
@BOT8.on(events.NewMessage(pattern="/start"))
@BOT9.on(events.NewMessage(pattern="/start"))
async def start(event):              
    if event.is_private:
       DeadlyBot = await event.client.get_me()
       bot_id = DeadlyBot.first_name
       bot_username = DeadlyBot.username
       replied_user = await event.client(GetFullUserRequest(event.sender_id))
       TheDeadly = event.chat_id
       firstname = replied_user.user.first_name
       ownermsg = f"**Hi Master, Its me {bot_id}, 🔱 ╚» 𝐔𝐋𝐓𝐑𝐀 𝐗 «╝🔥𝐒𝐏𝐀𝐌𝐌𝐄𝐑 𝐁𝐎𝐓🔥**"
       usermsg = f"**Hello {firstname} 🔱 ╚» 𝐔𝐋𝐓𝐑𝐀 𝐗 «╝🔥𝐒𝐏𝐀𝐌𝐌𝐄𝐑 𝐁𝐎𝐓🔥**"
       if event.sender_id == OWNER_ID:
            await event.client.send_file(TheDeadly,
                  DEADLY_IMG,
                  caption=ownermsg, 
                  buttons=Deadly_Button)
       else:
            await event.client.send_file(TheDeadly,
                  DEADLY_IMG,
                  caption=usermsg, 
                  buttons=DeadlyX_Button)
                
