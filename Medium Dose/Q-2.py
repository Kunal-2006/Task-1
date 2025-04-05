morse = {
    '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F',
    '--.': 'G', '....': 'H', '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L',
    '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P', '--.-': 'Q', '.-.': 'R',
    '...': 'S', '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X',
    '-.--': 'Y', '--..': 'Z', '-----': '0', '.----': '1', '..---': '2',
    '...--': '3', '....-': '4', '.....': '5', '-....': '6', '--...': '7',
    '---..': '8', '----.': '9', '/': ' '  # "/" represents spaces
}

# Read Morse Code from file
file = open("Morse.txt", "r")
morse_code = file.read().strip()
file.close()

# Decode Morse Code
decoded_msg = []
words = morse_code.split(" / ")  # Properly split words

for word in words:
    letters = word.split()  # Split each word into Morse letters
    for letter in letters:
        if letter in morse:  # Check if letter exists in dictionary
            decoded_msg.append(morse[letter])  # Append decoded letter
    decoded_msg.append(" ")  # Append space after each word

# Remove extra trailing space
if decoded_msg and decoded_msg[-1] == " ":
    decoded_msg.pop()

# **Write to the file using a loop**
file = open("Morse.txt", "w")  # Overwrite file
for char in decoded_msg:  # Write character by character
    file.write(char)
file.close()
