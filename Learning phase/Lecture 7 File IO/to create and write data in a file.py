"""f=open("practice.txt","w")
f.write("Hi everyone\nwe are learning FIle I/O\nusing Java.\nI like programming in Java.\n")
f.close()
"""

# alternatively

with open("practice.txt","w") as f:
    f.write("Hi everyone\nwe are learning FIle I/O\nusing Java.\nI like programming in Java.\n")
    f.close()