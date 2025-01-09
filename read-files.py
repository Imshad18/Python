from pathlib import Path

path = Path("C:\\Users\\imsha\\Desktop\\pi_digit.txt.txt")  #path to the file you want to read
cont = path.read_text()
cont = cont.rstrip()
print(cont)
