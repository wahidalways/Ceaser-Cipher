import art

alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd',
    'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
    't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
    'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w',
    'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
    'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a',
    'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
    'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e',
    'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
    'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
    'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
    'y', 'z'
]
print(art.logo)
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def ceaser(start_text, shift_ammount, cipher_direction):
    end_text = ""
    if shift_ammount > 26:
        shift_ammount = round(shift_ammount % 26)
        print(shift_ammount)
    for position in range(0, len(start_text)):
        letter = start_text[position]
        if cipher_direction == "encode":
            if letter in alphabet:
                index = alphabet.index(letter)
                newposition = index + shift_ammount
                new = alphabet[newposition]
                end_text += new
            elif letter not in alphabet:
                end_text += letter

        elif cipher_direction == "decode":
            if letter in alphabet:
                index = alphabet.index(letter)
                newposition = 26 + (index - shift_ammount)
                new = alphabet[newposition]
                end_text += new
            elif letter not in alphabet:
                end_text += letter

    print(f"Your {cipher_direction}d is ", end_text)


ceaser(start_text=text, shift_ammount=shift, cipher_direction=direction)

end_of_loop = False
while not end_of_loop == True:
    wantMore = input("Do you want to continue? yes/no \n")
    if wantMore == "yes":
        direction = input(
            "Type 'encode' to encrypt, type 'decode' to decrypt:\n")
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        ceaser(start_text=text,
               shift_ammount=shift,
               cipher_direction=direction)
    elif wantMore == "no":
        end_of_loop = True
