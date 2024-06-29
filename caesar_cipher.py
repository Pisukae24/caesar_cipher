alphabets=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
             'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encryption(plain_text, shift_key):
    cipher_text=""
    for char in plain_text:
        if char in alphabets:
            position = alphabets.index(char)
            new_position = (position+shift_key)%26
            cipher_text += alphabets[new_position]
        else:
            cipher_text += char
    print(f"here is the text after encryption: {cipher_text}")
def decryption(cipher_text, shift_key):
    plain_text=""
    for char in cipher_text:
        if char in alphabets:
            position = alphabets.index(char)
            new_position = (position-shift_key)%26
            plain_text += alphabets[new_position]
        else:
            cipher_text += char
    print(f"here is the text after encryption: {plain_text}")
wanna_end = False
while not wanna_end:
    what_to_do = input("type 'encrypt' for encryption and 'decrypt' for description\n")
    text = input("enter the message : \n").lower()
    shift = int(input("Enter shift key: \n"))
    if what_to_do=="encrypt":
        encryption(plain_text=text,shift_key=shift)
    elif what_to_do=="decrypt":
        decryption(text,shift)
    play_again=input("do you want to play again or not:")
    if play_again=="no":
       wanna_end=True
       print("have a nice day!!\n bye")