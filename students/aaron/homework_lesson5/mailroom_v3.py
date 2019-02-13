#!/usr/bin/env python3

import re

donors = {'bob barker': {'donations': 2, 'total': 24456.24, 'name': 'Bob Barker'},
          'roger rabbit': {'donations': 1, 'total': 4930.26, 'name': 'Roger Rabbit'},
          'bruce lee': {'donations': 3, 'total': 52246.75, 'name': 'Bruce Lee'},
          'frodo baggins': {'donations': 1, 'total': 1249.44, 'name': 'Frodo Baggins'},
          'kermit the frog': {'donations': 2, 'total': 23475.20, 'name': 'Kermit the Frogg'}}

# prints a main menu
def show_main_menu():
  print("-" * 70)
  for number, func in sorted(menu_opts.items()):
    print('{}. {}'.format(number, menu_opts_text[func]))

# gets a menu selection
def get_main_selection():
  user_in = ""
  while user_in == "":
    show_main_menu()
    user_in = input("Enter a menu number: ")
    if user_in not in menu_opts.keys():
      print("Invalid selection.  Enter a menu selection:", list(menu_opts.keys()))
      user_in = ""
  return user_in

# logic for inputting a new donation
def send_thankyou():
  user_in = ""
  names = [n.lower() for n in list(donors.keys())]
  while user_in == "":
    print("----------------------------------------------------------------")
    user_in = input("Enter a full name or type 'list' for a list of names: ")
    user_lower = user_in.lower()
    if user_lower == 'list':
      print("Donors: ")
      for name in names:
         print(" " + name)
      user_in = ""
    elif user_lower not in names:
      donors[user_lower] = {'donations': 0, 'total': 0, 'name': user_in}
  amount = 0
  while amount == 0:
    try:
      amount = float(input("Enter a donation amount: "))
    except:
      amount = 0
      print("-> ERROR: Please enter a valid floating point number.")
  donors[user_lower]['donations'] += 1
  donors[user_lower]['total'] += amount
  output_thankyou(user_in, amount)

# print a report
def output_report():
  table_headerfmt = "{:<19s}|{:>15s} |{:>14s} |{:>15s}"
  table_formatter = "{:<19s}  ${:13.2f}  {:14d}   ${:13.2f}"
  table_seperator = "-" * 68
  print(table_headerfmt.format("Donor Name", "Total Given", "Num Gifts", "Average Gift"))
  print(table_seperator)

  # unpack to a list of lists
  donor_list = [[donors[donor]['name'], donors[donor]['donations'], donors[donor]['total']] for donor in donors]

  # sort the list
  donor_list = sorted(donor_list, key = lambda x: x[2] * -1)

  # print the list
  for donor in donor_list:
    print(table_formatter.format(donor[0], donor[2], donor[1], donor[2] / donor[1]))

# print a thank you for a recent donation
def output_thankyou(donor_name, latest_amount):
  print(generate_thankyou(donor_name, latest_amount, True))

# write a thank you note to disk for a donor
def write_letters():
  for donor_name in donors.keys():
    # convert any non-alphanumeric characters to _ for the filename
    donor_file = re.sub(r"[^a-zA-Z0-9_-]+", "_", donor_name) + ".txt"

    note = generate_thankyou(donor_name)
    f = open(donor_file, 'w')
    f.write(note)
    f.close()
    print('>>> Wrote thank you note for {} to {}'.format(donor_name, donor_file))

# generate a thank you note for a donor
def generate_thankyou(donor_name, latest_amount=0, recent=False):
  donations_total = donors[donor_name]["total"]
  donations_count = donors[donor_name]["donations"]
  format_values = {'donations_total': donations_total,
                   'donations_count': donations_count,
                   'donor_name': donor_name,
                   'latest_amount': latest_amount}
  if recent:
    template = '''----------------------------------------------------------------------
Dear {donor_name},
  Thank you for your generous donation of {latest_amount:.2f}!
That brings your total of {donations_count} donation(s) to ${donations_total:.2f}
Sincerely,
 -Me
'''
  else:
    template = '''----------------------------------------------------------------------
Dear {donor_name},
  Thank you for all {donations_count} of your generous donations for a total of {donations_total:.2f}!
We will put the money to good use.
Sincerely,
 -Me
'''
  letter = template.format(**format_values)
  return(letter)

# the main loop
def main():
  selection = "2"
  while menu_opts[selection] != quit:
    selection = get_main_selection()
    menu_opts[selection]()

# a dict for mapping user selection to functions
menu_opts = {'1': send_thankyou,
             '2': output_report,
             '3': write_letters,
             '4': quit}
menu_opts_text = {send_thankyou: "Send a Thank You to a single donor.",
                  output_report: "Create a report.",
                  write_letters: "Send letters to all donors.",
                  quit: "Quit."}

if __name__ == '__main__':
  main()
