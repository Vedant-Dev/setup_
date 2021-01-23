
import secrets
letter_list =  "abcdefghijklmnopqrstuvwxyz".upper()
length = input("Enter number of letter")
final_name = ''
for _ in range(length):
  final_name = final_name + secrets.choice(letter_list)
 print(final_name)
