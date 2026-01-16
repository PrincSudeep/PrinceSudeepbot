import pytz
import base64
from datetime import datetime

# temp
class temp(object):
    START_TIME = 0
    ME = None
    U_NAME = None
    B_NAME = None
    BOT = None


async def encode(string):
    string_bytes = string.encode("ascii")
    base64_bytes = base64.urlsafe_b64encode(string_bytes)
    base64_string = (base64_bytes.decode("ascii")).strip("=")
    return base64_string

async def decode(base64_string):
    base64_string = base64_string.strip("=") # links generated before this commit will be having = sign, hence striping them to handle padding errors.
    base64_bytes = (base64_string + "=" * (-len(base64_string) % 4)).encode("ascii")
    string_bytes = base64.urlsafe_b64decode(base64_bytes) 
    string = string_bytes.decode("ascii")
    return string

def get_size(size):
    units = ["Bytes", "KB", "MB", "GB", "TB", "PB", "EB"]
    size = float(size)
    i = 0
    while size >= 1024.0 and i < len(units):
        i += 1
        size /= 1024.0
    return "%.2f%s" % (size, units[i])

def get_wish():
    tz = pytz.timezone('Asia/Colombo')
    time = datetime.now(tz)
    hour = time.hour  # Get hour in 24-hour format
    minute = time.minute  # Get minute for precise comparisons

    # Good Morning: 5:00 AM to 11:59 AM
    if 5 <= hour < 12:
        status = "Good Morning 🌞"
    # Good Afternoon: 12:00 PM to 4:59 PM
    elif 12 <= hour < 17:
        status = "Good Afternoon 🌗"
    # Good Evening: 5:00 PM to 8:59 PM
    elif 17 <= hour < 21:
        status = "Good Evening 🌘"
    # Good Night: 9:00 PM to 4:59 AM
    else:  # Covers 9:00 PM to 4:59 AM
        status = "Good Night 🌙"

    return status


LANGUAGE_MAP = {
    "Hindi": "Hindi", "Hin": "Hindi",
    "Bengali": "Bengali", "Ben": "Bengali",
    "English": "English", "Eng": "English",
    "Marathi": "Marathi", "Mar": "Marathi",
    "Tamil": "Tamil", "Tam": "Tamil",
    "Telugu": "Telugu", "Tel": "Telugu",
    "Malayalam": "Malayalam", "Mal": "Malayalam",
    "Kannada": "Kannada", "Kan": "Kannada",
    "Punjabi": "Punjabi", "Pun": "Punjabi",
    "Gujrati": "Gujrati", "Guj": "Gujrati",
    "Korean": "Korean", "Kor": "Korean",
    "Japanese": "Japanese", "Jap": "Japanese",
    "Chinese": "Chinese", "Chi": "Chinese", "Mandarin": "Chinese", "Man": "Chinese",
    "Spanish": "Spanish", "Spa": "Spanish",
    "French": "French", "Fre": "French",
    "German": "German", "Ger": "German",
    "Russian": "Russian", "Rus": "Russian",
    "Portuguese": "Portuguese", "Por": "Portuguese",
    "Italian": "Italian", "Ita": "Italian",
    "Arabic": "Arabic", "Ara": "Arabic",
    "Turkish": "Turkish", "Tur": "Turkish",
    "Vietnamese": "Vietnamese", "Vie": "Vietnamese",
    "Urdu": "Urdu", "Urd": "Urdu",
    "Thai": "Thai", "Tha": "Thai",
    "Persian": "Persian", "Per": "Persian", "Farsi": "Persian",
    "Dutch": "Dutch", "Dut": "Dutch",
    "Greek": "Greek", "Gre": "Greek",
    "Hebrew": "Hebrew", "Heb": "Hebrew",
    "Indonesian": "Indonesian", "Indo": "Indonesian",
    "Bhojpuri": "Bhojpuri", "Bho": "Bhojpuri",
    "Dual": "Dual", "Multi": "Multi"
}
