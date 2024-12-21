import os
CURRENT_FOLDER = os.getcwd()
UPLOAD_FOLDER = CURRENT_FOLDER + "/upload"
TEMP_FOLDER = CURRENT_FOLDER + "/templates"
LOG_FOLDER = CURRENT_FOLDER + "/log"
TESSERACT_CMD = r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

ALLOWED_COMMANDS = ['ls', 'whoami', 'id', 'group']

# Regex để kiểm tra lệnh hợp lệ và các đối số an toàn
COMMAND_PATTERN = r'^[a-zA-Z0-9\-_\/\s]+$'


def check_authenticated():
    if session['role'] == 'admin':
        return True
    else:
        return 
