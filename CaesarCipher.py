message = input("Print message: ")
shift = int(input("Enter offset: "))

result = ""

for ch in message:
    if 'A' <= ch <= 'Z':
        result += chr((ord(ch) - ord('A') + shift) % 26 + ord('A'))
    elif 'a' <= ch <= 'z':
        result += chr((ord(ch) - ord('a') + shift) % 26 + ord('a'))
    else:
        result += ch

print("Message:", result)
