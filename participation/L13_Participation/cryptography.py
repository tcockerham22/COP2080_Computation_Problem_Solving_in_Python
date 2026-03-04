import hashlib
import string

# Store the original hash
original_hash = "d077f244def8a70e5ea758bd8352fcd8"

letters = string.ascii_lowercase  # 'abcdefghijklmnopqrstuvwxyz'

for letter1 in letters:
    for letter2 in letters:
        for letter3 in letters:
            guess = letter1 + letter2 + letter3
            new_hash = hashlib.md5(guess.encode("utf-8")).hexdigest()
            
            if new_hash == original_hash:
                print(f"Match found! The word is: {guess}")
                exit()