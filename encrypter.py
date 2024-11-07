import random

unalphabet = "abcdefghijklmnopqrstuvwxyz"
upalphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
symbols = "!@#$%^&*()-_=+[|;:',<.>~'/?]"
numbers = "0123456789"
total_symbols = unalphabet + upalphabet + symbols + numbers

print("========Encrypter========")
message = input ("What is your message?: ")

def encode(message):
    encrypted_message = ""
    for characters in message:
        if characters in unalphabet:
            letters = unalphabet.find(characters)
            encrypted_message += unalphabet [(letters - 19 + 1) % len(unalphabet)]
        elif characters in upalphabet:
            letter = upalphabet.find(characters)
            encrypted_message += upalphabet [(letter - 13 + 12) % len(upalphabet)]
        elif characters in symbols:
            spsymbol = symbols.find(characters)
            encrypted_message += symbols [(spsymbol - 12 + 23) % len(symbols)]
        elif characters in numbers:
            number = numbers.find(characters)
            encrypted_message += numbers [(number - 41 + 34) % len(numbers)]
        else:
            encrypted_message += characters
    
    indices = list(range(len(encrypted_message)))
    random.shuffle(indices)

    shuffled_message = ''.join(encrypted_message[i] for i in indices)
    
    return shuffled_message, indices

encoded_message, shuffle_key = encode(message)
print(encoded_message)
print(shuffle_key)

