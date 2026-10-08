'''
Question: Why does it matter whether you're running Python 2 or Python 3? Find one real difference between them beyond print syntax.
Answer:Python 2's str type is actually a byte string... In Python 3, the str type contains Unicode characters, and a new bytes type is introduced to hold raw 8-bit bytes. Python 3 will no longer automatically convert between text and bytes.
Source:https://peps.python.org/pep-3112/


Question: What is a text editor vs. an IDE, and which are you using? Name one feature of your editor that will help you as you write more Python.
Answer: A text editor is a lightweight tool designed primarily for writing and editing raw code or plain text, whereas an Integrated Development Environment (IDE) is a heavy-duty
 software suite that combines an editor with built-in developer tools like a compiler/interpreter, debugger, terminal, and project manager in a single interface.

-Visual Studio Code (VS Code)
-Built-in Terminal with Auto-Activated Virtual Environments allowing me to run scripts (python main.py) or install packages without manually switching windows or sourcing paths..
Source: Gemini
Question:Look up “the Zen of Python” (hint: type import this into a Python shell). Pick one line from it and explain, in your own words, what it means for how you should write code.
Answer:Beautiful is better than ugly. This means it is better to organize your code to make it readable than to make it disorganized and not readable.
Source: https://www.python.org/dev/peps/pep-0020/
'''
# A python program that prints "Hi!" to the console
print("Hi!")

