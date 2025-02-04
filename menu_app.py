def main_menu():
  print("==== MAIN MENU ====")
  print("1) Dice Game")
  print("2) Guess the Number")
  print("3) Quiz Game")
  print("4) Hangman")
  print("5) Exit")

def main():
  while True:
    main_menu()
    choice = input("Select an option: ")

    if choice == '1':
      pass
    elif choice == '2':
      pass
    elif choice == '3':
      pass
    elif choice == '4':
      pass
    elif choice == '5':
      print("Exiting the program...")
      break
    else:
      print("Invalid choice, please try again.")

if __name__ == "__main__":
  main()