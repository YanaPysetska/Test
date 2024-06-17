from art import logo

print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f',
            'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't',
            'u', 'v', 'w', 'x', 'y', 'z']

# TODO-1: Create a function called 'encrypt'
# that takes the 'text' and 'shift' as inputs.

def caesar(plain_text, shift_amount, cypher_direction):
    global new_position
    cipher_text = ""
    for i in plain_text:
        if i in alphabet:
            position = alphabet.index(i)
            if cypher_direction=='encode':
                new_position = (position + shift_amount) % len(alphabet)
            elif cypher_direction=='decode':
                new_position = (position - shift_amount) % len(alphabet)
            new_letter = alphabet[new_position]
            cipher_text += new_letter
        else:
            cipher_text +=i

    print(f"The {cypher_direction} text is {cipher_text}")

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


while True:
    caesar(plain_text=text, shift_amount=shift,cypher_direction=direction)
    user_input = input("Do you want to continue (yes/no): ").strip().lower()
    if user_input == 'no':
        print("Bye.")
        break
    elif user_input == 'yes':
        print("OK")
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
    else:
        print("Error.")

