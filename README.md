

Question : What's the difference between git commit and git push — why are they two separate steps?**

Answer: git commit saves your staged changes locally on your computer. It creates a snapshot of your project in your local repository's history, requiring a commit message to record what changed. No network or internet connection is involved. Whereas git push uploads your local commits to a remote repository (like GitHub or GitLab) so others can see your work or so it is safely backed up off your local machine.**

Why the two?

The single reason for separating the two is local independence: git commit lets you save and organize your work locally without network dependencies, while git push lets you choose when to publish that history to others.

Source: Gemini


Question: What does the -u in git push -u origin main actually do?

Answer : The -u flag is short for --set-upstream.

When you run git push -u origin main, Git links your local main branch directly to the main branch on the origin remote.

Source: official Git documentation for git-push


-Running hello_world.py and variables_and_data_types.py from the terminal
godfred@godfred-HP-EliteBook-840-G3:~/Documents/Github/python-practice$ python3 hello_world.py 
Hi!
godfred@godfred-HP-EliteBook-840-G3:~/Documents/Github/python-practice$ python3 variables_and_data_types.py 
My name is BOATENG GODFRED AGYEMANG and I was born around 2008, so I'm 18 years old.
www.google.com
google.com
Sum: 15
a^5: 243
b^5: 3125
c^5: 16807
29

- Looking up the version of python3 i am using
godfred@godfred-HP-EliteBook-840-G3:~/Documents/Github/python-practice$ python3 --version
Python 3.14

