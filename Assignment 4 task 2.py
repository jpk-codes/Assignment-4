with open('output.txt', 'w') as file:
    text1 = input("Enter text to write to the file :")
    file.write(text1)
    file.close()
    print("Data successfully written to output.txt.")
text2 = input("\nEnter additional text to append:")
with open('output.txt', 'a') as file:
    file.write('\n' + text2)
    file.close()
    print("Data successfully appended.")

with open("output.txt", "r") as file:
    print("\nFinal content of output.txt:")
    print(file.read())


# with open('output.txt', 'w') as file:
#     text1 = input("Enter text to write to the file :")
#     file.write(text1)
#     file.close()
#     print("Data successfully written to output.txt.")
# text2 = "a"
# while text2 != "":
#     text2 = input("\nEnter additional text to append:")
#     with open('output.txt', 'a') as file:
#         file.write('\n' + text2)
#         file.close()
#         print("Data successfully appended.")
#
# with open("output.txt", "r") as file:
#     print("\nFinal content of output.txt:")
#     print(file.read())
