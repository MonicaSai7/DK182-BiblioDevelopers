import pyperclip
from datetime import datetime
pyperclip.copy('The text to be copied to the clipboard.')
res = pyperclip.paste()
print(res)
