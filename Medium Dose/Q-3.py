data = "ABCDE"
new = []

for i in range(len(data)):  
    shifted_value = ord(data[i]) - i - 1  # Shift character

    if shifted_value < 65:  # If below 'A', wrap around to 'Z'
        k = 90 - (65 - shifted_value) + 1  # Wrap calculation
        new.append(chr(k))  
    else:
        new.append(chr(shifted_value))  // append directly

# Print each character separately using append
for ch in new:
    print(ch, end="")  # Output characters one by one

print("Decoded message saved in 'Morse.txt'")
