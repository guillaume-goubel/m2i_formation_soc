from datetime import datetime

def get_date_time_format():
    now = datetime.now()
    timecode_format = now.strftime("%Y-%m-%d %H:%M:%S")
    return timecode_format