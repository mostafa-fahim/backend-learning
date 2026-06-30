message = input("> ").lower()
words = message.split(" ")
emojis = {
    ":)": "😄",
    ":(": "😟",
    ":D": "😁",
    ":p": "😛"
}
output = ""
for word in words:
    output += emojis.get(word, word) + " "
print(output)