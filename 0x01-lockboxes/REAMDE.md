📖 0x01. Lockboxes
Topics Covered
Python.
Lockboxes.
💻 Tasks.
0. Lockboxes
Task requirements.
You have n number of locked boxes in front of you. Each box is numbered sequentially from 0 to n - 1 and each box may contain keys to the other boxes.

Write a method that determines if all the boxes can be opened.

Prototype: def canUnlockAll(boxes)
boxes is a list of lists
You can assume all keys will be positive integers
There can be keys that do not have boxes
The first box boxes[0] is unlocked
Return True if all boxes can be opened, else return False
carrie@ubuntu:~/0x01-lockboxes$ cat main_0.py
#!/usr/bin/python3

canUnlockAll = __import__('0-lockboxes').canUnlockAll

boxes = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes))

boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
print(canUnlockAll(boxes))

boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes))

carrie@ubuntu:~/0x01-lockboxes$
carrie@ubuntu:~/0x01-lockboxes$ ./main_0.py
True
True
False
carrie@ubuntu:~/0x01-lockboxes$
🔧 Task setup.
# Create task file and set write permission.
touch ./0-lockboxes.py
chmod +x ./0-lockboxes.py
./0-lockboxes.py

# Lint the code.
pycodestyle ./0-lockboxes.py
pep8 ./0-lockboxes.py

# Create test file
touch ./0-main.py
chmod +x ./0-main.py
./0-main.py
✔️ Solution.
👉 Open 0-lockboxes.py

📚 References
Python Lists
Python sum() Function
👨 Author and Credits.
This project was done by SE. Moses Mwangi. Feel free to get intouch with me;

📱 WhatsApp +254115227963

📧 Email moses.soft.eng@gmail.com

👍 A lot of thanks to ALX-Africa Software Engineering program for the project requirements.
