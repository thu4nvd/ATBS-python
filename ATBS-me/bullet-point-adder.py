# bullet-point-adder.py add bullet to list
# author alibaba

import pyperclip


text = pyperclip.paste()
# print(text)
lines = text.split('\n')
for i in range(len(lines)):
    lines[i] = '* ' + lines[i]
text = '\n'.join(lines)
pyperclip.copy('Hello Thuan')
print(text)
# unable to flush on clipboard
