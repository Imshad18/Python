from pathlib import Path

path=Path("C:\\Users\\imsha\\Desktop\\py_chaps\\chapter_10\\exceptions\\alice.txt")
try:
    content = path.read_text(encoding='utf-8')
except FileNotFoundError:
    print(f"File does not exists.")
else:
    #counting the words in the file
    words = content.split() #split() splits a string whenever it finds a whitespace
    print(f"There are {len(words)} words in Alice in Wonderland")
