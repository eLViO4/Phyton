import urllib.request

url = "https://www.gutenberg.org/files/1184/1184-0.txt"

with urllib.request.urlopen(url) as response:
    text = response.read().decode('utf-8')

total_letters = 0
lowercase_count = 0
uppercase_count = 0

for char in text:
    if char.isalpha():
        total_letters += 1
        if char.islower():
            lowercase_count += 1
        elif char.isupper():
            uppercase_count += 1

lowercase_percent = (lowercase_count / total_letters) * 100
uppercase_percent = (uppercase_count / total_letters) * 100

print(f"Amount of letters: {total_letters}")
print(f"Small letters: {lowercase_count} ({lowercase_percent:.2f}%)")
print(f"Big letters: {uppercase_count} ({uppercase_percent:.2f}%)")
