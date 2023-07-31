from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(logo)

def ceaser_cipher(start_text , shift_value, cipher_direction):
  end_text = ""
  # If the direction is to decode, then we are going backward, thus multiply shift value by -1
  if cipher_direction == "decode":
    shift_value *= -1

  # Start to decode/encode each letter as follows:
  for char in start_text:
    #1.check if the char is a letter, if not then just print it as it is
    if char in alphabet:
      #2.encode/decode the char since it's a letter

      #find the position of the letter
      position = alphabet.index(char)
      #calculate the new position by adding the shifting value to it (if shifting value is negative it will decode)
      new_position = position + shift_value
      #use the module (%) on the shift value to ensure that the numbers are within the range of the list (26 letters) 
      new_position %= 26
      #add the new letter into the full string at the end
      end_text += alphabet[new_position]
    else:
      # It's not a letter, thus print thae character (e.g. numbers, symbols, etc.) as it is
      end_text += char

  print(f"Here's the {cipher_direction}d result: {end_text}")


user_input = "yes"
while user_input == "yes":
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  ceaser_cipher(text , shift, direction)
  user_input = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")

  
  