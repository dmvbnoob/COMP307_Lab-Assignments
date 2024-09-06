alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890 .,?!"
partialOne=""
partialTwo=""
newAlphabet=""
message = input("Please enter the message you want to translate: ").upper()
key = int(input("Please enter the number you want to shift by: "))

if key == 0:
    newAlphabet = alphabet
elif key > 0:
    partialOne = alphabet[:key]
    partialTwo = alphabet[key:]
    newAlphabet = partialTwo + partialOne
else:
    partialOne = alphabet[:(26 + key)]
    partialTwo = alphabet[(26 + key):]
    newAlphabet = partialTwo + partialOne


encrypted=""
for message_index in range(0,len(message)):
    if message[message_index] == " ":
        encrypted+= " "
    for alphabet_index in range(0,len(newAlphabet)):
        if message[message_index] == alphabet[alphabet_index]:
            encrypted+= newAlphabet[alphabet_index]

print(encrypted)

decrypt = input("Do you want to decrypt this message? Y/N ")

if decrypt == "Y":
    for dkey in range(len(alphabet)):
        translated = ''
        for alp in message:
            if alp in alphabet:
                alpIndex = alphabet.find(alp)
                translatedIndex = alpIndex - dkey
                if translatedIndex < 0:
                    translatedIndex = translatedIndex + len(alphabet)
                translated = translated + alphabet[translatedIndex]
            else:
                translated = translated + alp
        print('Key #%s: %s' % (dkey, translated))
else:
    print("Goodbye!")