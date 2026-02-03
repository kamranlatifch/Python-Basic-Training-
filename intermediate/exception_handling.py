# run it as python3 exception_handling.py
try:
    open("file.txt", "r")  # this will raise a FileNotFoundError
except FileNotFoundError:
    print("File not found")
finally:
    print("This will always run")

print("This will always run")
