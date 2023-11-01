import subprocess

MESSAGE_COLOR = "\x1b[34m"
RESET_ALL = "\x1b[0m"

print (f"{MESSAGE_COLOR}Almost done!")
print (f"Initializanding a git repository...{RESET_ALL}")

subprocess.call(['git', 'init'])
subprocess.call(['git', 'add', '*'])
subprocess.call(['git', 'commit','-m','Initial commit'])

print(f"{MESSAGE_COLOR}The biginning of your destiny is defined now! create and have fun!{RESET_ALL}")