unalphabet = "abcdefghijklmnopqrstuvwxyz"
upalphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
symbols = "!@#$%^&*()-_=+[|;:',<.>/?]"
numbers = "0123456789"

print("=========Decrypter========")

while True: 
    message = input("What is your message?: ")
    keys = input("What are the keys? (space-seperated integers): ")

    try:
        keys = list(map(int, keys.split()))

        if len(keys) != len(message):
            print(f"Error: The number of keys ({len(keys)}) must match the length of the message ({len(message)}).")
            continue
        break

    except ValueError:
        print("Error: Invalid format for keys. Please ensure keys are space-separated integers.")

def decode(shuffled_message, indices):
    unshuffled_message = [''] * len(shuffled_message)

    for i, original_index in enumerate(indices):
        unshuffled_message[original_index] = shuffled_message[i]
    
    decrypt_one = ''.join(unshuffled_message)

    decoded_message = ""
    for characters in decrypt_one: 
        if characters in unalphabet:
            letters = unalphabet.find(characters)
            decoded_message += unalphabet [(letters + 19 - 1) % len(unalphabet)]
        elif characters in upalphabet:
            letter = upalphabet.find(characters)
            decoded_message += upalphabet [((letter + 13 - 12) % len(upalphabet))]
        elif characters in symbols:
            spsymbol = symbols.find(characters)
            decoded_message += symbols [((spsymbol + 12 - 23) % len(symbols))]
        elif characters in numbers:
            number = numbers.find(characters)
            decoded_message += numbers [((number + 41 - 34) % len(numbers))]
        else:
            decoded_message += characters

    return (decoded_message)

try:
    print(decode(message, keys))
except IndexError as e:
    print(f"Error: {e}. Please check that each index in keys is within the correct range (0 to {len(message) - 1}).")
    



