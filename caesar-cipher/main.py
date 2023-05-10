# _________________________________CAESAR CIPHER______________________________ #
# User chooses whether to encode or decode -

# Encode: User gives a message and a shift key
# computer encodes it by shifting each letter by the shift key amount

# Decode: User gives the coded message and the shift key
# computer decodes it by shifting the letter back to what they're supposed to be

# Import art
import art

# Set main variables
run_program = True

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


# _________________________________CAESAR CODING FUNCTION______________________________ #
def caesar(start_text, shift_amount, cipher_direction):
    """Shifts the given text by the shift amount either forward or backward depending on command."""
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount
            end_text += alphabet[new_position]
        else:
            end_text += char

    print(f"Here's the {cipher_direction}d result: {end_text}")


# _________________________________MAIN CODE______________________________ #
while run_program:
    print(art.logo)

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    if shift > 26:
        shift %= 26

    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
    choose = input("Would you like to run the program again? Type 'Yes' or 'No'\n").lower()
    if choose == "no":
        run_program = False
        print("Et Tu Brute?")