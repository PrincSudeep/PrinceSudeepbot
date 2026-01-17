class script(object):

    START_TXT = """<b>👋 Hello {}, <i>{}</i>

I Am A Powerful Auto Poster Bot</b>"""

    HELP_TXT = """<b>Hey {},

Here is my basic features. 🎊

• Filter Movies and TV Series by your keyword.

Here is my basic commands. 🪅

• /start - Start The Bot!
• /status - Get Bot Status.
• /ping - Get Bot Ping.
• /id - Get chat ID.
• /info - Get bot or user info.
• /donate - Donate For Us.

How to use me? 🤔

1. Add me to your group.
2. Make me as admin with all access.
3. Type and send you want Movie or TV Series name in to group.
4. Then you can see my magic.
5. Enjoy with yours Movie and TV Series.

We hope to provide you with the best service. 🪄</b>"""

    ABOUT_TXT = """<b>🌟 Welcome to <a href="https://t.me/{1}">{2}</a>! 🎉</b>

👋 <b>Hello, {0}!</b>

<b>I’m <a href="https://t.me/{1}">{2}</a>, your smart and powerful Auto Filter Bot.</b> 
<b>I help you search and fetch movies or series from your group instantly – no hassle, just results! 🎯</b>

<b>👨‍💻 Developer :</b> <a href='https://t.me/SMDxTG'>Mɪᴄʜᴀᴇʟ 💤</a>  
<b>📚 Library :</b> <a href='https://docs.pyrogram.org/'>Pyrogram</a>  
<b>🦾 Language :</b> Python 3  
<b>🗃 Database :</b> <a href='https://www.mongodb.com/'>MongoDB</a>  
<b>📡 Hosted on :</b> <a href='https://heroku.com'>Heroku</a>  
<b>🚀 Version :</b> v2.0.1 [Beta]

<b>❓ Need help?</b> <a href='https://t.me/SMD_BOTz_Support'>Contact Support</a>  
<b>⚡ Experience lightning-fast filtering with me. Add me to your group and enjoy seamless searching!</b>
"""

    DONATE_TXT = """<b>👋 Hello {}, <i>{}</i>

💸 Donate 🙏🏻

As you know, our service is completely free. However, maintaining it comes with server costs and other expenses. To keep this bot running smoothly, I would greatly appreciate any donation you can offer.

Every bit helps — whether it’s ₹5, ₹10, ₹20, ₹30, or ₹50 — it all goes toward keeping the service alive. You can donate via UPI. 🙏🏻❤️

📲 GPay (UPI) : <code>smdowner@ybl</code>  
📸 Send Screenshot : @SMDxTG

Please share and support us! 🙏🏻❤️</b>"""
    
    STATUS_TXT = """<b>📊 Bot Status Report ❗</b>

<b>👤 Total Users :</b> <code>{}</code>  
<b>👥 Total Chats :</b> <code>{}</code>
<b>🧊 Data DB Used :</b> <code>{}</code>

<b>🗂️ Primary DB Files :</b> <code>{}</code>
<b>📦 Primary DB Storage :</b> <code>{}</code>
<b>🗂️ Secondary DB Files :</b> <code>{}</code>
<b>📦 Secondary DB Storage :</b> <code>{}</code>

<b>📟 CPU Usage :</b> <code>{}%</code>
<b>🧠 RAM Usage :</b> <code>{}%</code>

<b>🚀 Bot Uptime :</b> <code>{}</code>
<b>⚡ Response Time :</b> <code>{} ms</code>
<b>🔄 Last Restart :</b> <code>{}</code>"""
    
    NEW_GROUP_TXT = """<b>📢 New Group Added</b>

<b>🎊 Group Name :</b> <code>{}</code>
<b>🌥️ Group ID :</b> <code>{}</code>
<b>👤 User Name :</b> <code>{}</code>  
<b>🧊 Total Members :</b> <code>{}</code>"""
  
    NEW_USER_TXT = """<b>👤 New User Started</b>
    
<b>📛 Name:</b> {}
<b>🆔 ID:</b> <code>{}</code>"""


    NOT_FILE_TXT = """<b>👋 Hello {}, </b>

I can't find <b>"{}"</b> in my database! 🔍🥲

<b>💡 Possible reasons:</b>
• 🔤 Check your spelling and try again
• 🎬 The content may not be released yet
• 📝 Try using a different keyword
• 🌐 Use IMDB name for better results

<b>🔄 Try again or browse our latest additions!</b>"""
    
    RESTART_TXT = """<b>🔄 Bot Restarted!</b>

<b>📅 Date:</b> <code>{}</code>  
<b>⏰ Time:</b> <code>{}</code>  
<b>🌐 Timezone:</b> <code>Asia/Kolkata</code>  
<b>🛠️ Build Status:</b> <code>v2.7.1 [Stable]</code>"""

    FILE_CAPTION = """<b>{file_name}

📦 Size : {file_size}

📂 Full Caption : {file_caption}</b>"""
    
    SHORT_CAP_TXT = """<b>👋 Hey {0}, {1}

📁 File Name : {file_name}

📦 Size : {file_size}

📝 Full Caption : {file_caption}

👇 Tap the button below to download the file !!!</b>"""

    IMDB_TEMPLATE = """<b>✅ I Found: <code>{query}</code>

🏷 Title: <a href={url}>{title}</a>
🎭 Genres: {genres}
📆 Year: <a href={url}/releaseinfo>{year}</a>
🌟 Rating: <a href={url}/ratings>{rating} / 10</a>
☀️ Languages: {languages}
📀 RunTime: {runtime} Minutes

🗣 Requested by: {message.from_user.mention}
⚡ Powered by: {message.chat.title}</b>"""
  
    LOGO = """
░██████╗███╗░░░███╗██████╗░██████╗░░█████╗░████████╗███████╗
██╔════ ████╗░████║██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝╚════██║
╚█████╗░██╔████╔██║██║░░██║██████╦╝██║░░██║░░░██║░░░░░███╔═╝
░╚═══██╗██║╚██╔╝██║██║░░██║██╔══██╗██║░░██║░░░██║░░░██╔══╝░░
██████╔╝██║░╚═╝░██║██████╔╝██████╦╝╚█████╔╝░░░██║░░░███████╗
╚═════╝░╚═╝░░░░░╚═╝╚═════╝░╚═════╝░░╚════╝░░░░╚═╝░░░╚══════╝
"""
