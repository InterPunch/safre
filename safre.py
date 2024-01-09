import random
import sys

print("safre v. 1.0.1 created by interpunch aka squiddr")

platform = input("Enter the use of the password: ")
notes = input("\nEnter any notes here(Enter to skip): ")
date = input("Enter Date(Enter to skip))")

letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p'
]
number = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
sped_char = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "+"]

combined_list = letters + number + sped_char
random.shuffle(combined_list)
password = ''.join(combined_list)
print("Your new password is, " + password)
print("https://github.com/InterPunch/safre")

with open('text.txt', 'w') as file:
  file.write(platform + "\n" + password + "\nNotes: " + notes + "\n" + date)
