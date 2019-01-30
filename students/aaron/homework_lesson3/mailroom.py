#!/usr/bin/env python3

donors = {'Bob Barker': {'donations': 2, 'total': 24456.24},
          'Roger Rabbit': {'donations': 1, 'total': 4930.26},
          'Bruce Lee': {'donations': 3, 'total': 52246.75},
          'Frodo Baggins': {'donations': 1, 'total': 1249.44},
          'Kermit the Frog': {'donations': 2, 'total': 23475.20}}

# prints a main menu
def show_main_menu():
  print("-------------------")
  print("1. Send a Thank You")
  print("2. Create a Report")
  print("3. Quit")

# gets a menu selection
def get_main_selection():
  user_in = ""
  while user_in == "":
    show_main_menu()
    user_in = input("Enter a menu number: ")
    if user_in != "1" and user_in != "2" and user_in != "3":
      print("Invalid selection.  Enter a menu selection.  1, 2, or 3.")
      user_in = ""
  return user_in

# logic for inputting a new donation
def send_thankyou():
  user_in = ""
  names = list(donors.keys())
  while user_in == "":
    print("----------------------------------------------------------------")
    user_in = input("Enter a full name or type 'list' for a list of names: ")
    if user_in == 'list':
      print("Donors: ")
      for name in names:
         print(" " + name)
      user_in = ""
    elif user_in not in names:
      donors[user_in] = {'donations': 0, 'total': 0}
  amount = float(input("Enter a donation amount: "))
  donors[user_in]['donations'] += 1
  donors[user_in]['total'] += amount
  output_thankyou(user_in, amount)

# print a report
def output_report():
  table_headerfmt = "{:<19s}|{:>15s} |{:>14s} |{:>15s}"
  table_formatter = "{:<19s}  ${:13.2f}  {:14d}   ${:13.2f}"
  table_seperator = "-" * 68
  print(table_headerfmt.format("Donor Name", "Total Given", "Num Gifts", "Average Gift"))
  print(table_seperator)

  # unpack to a list of lists
  donor_list = []
  for donor in donors:
    donor_list.insert(0, [donor, donors[donor]['donations'], donors[donor]['total']])

  # sort the list
  donor_list = sorted(donor_list, key = lambda x: x[2] * -1)

  # print the list
  for donor in donor_list:
    print(table_formatter.format(donor[0], donor[2], donor[1], donor[2] / donor[1]))

# print a thank you note for a new donation
def output_thankyou(donor_name, latest_amount):
  print("-" * 70)
  print("From: Me <me@example.org>")
  print(f'To: {donor_name} <generous_donor@example.org>')
  print("Subject: Thank you.")
  print("")
  print(f'Dear {donor_name},')
  print(f'  Thank you for your generous donation of {latest_amount:.2f}!')
  print(f'That brings your total of {donors[donor_name]["donations"]} donation(s) to ${donors[donor_name]["total"]:.2f}')
  print("Sincerely,")
  print(" -Me")

# the main loop
def main():
  selection = ""
  while selection != "3":
    selection = get_main_selection()
    if selection == "1":
      send_thankyou()
    elif selection == "2":
      output_report()

if __name__ == '__main__':
  main()
