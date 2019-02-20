#!/usr/bin/env python3
#
#-------------------------------------
# Assignment: mailroom tests (mailroom version 4, from lesson 6)
# Description: This file contains tests for mailroom_v4.py
# Changelog:
# 2019-02-19,Aaron Devey,Created
#-------------------------------------
#
#

import pytest
import glob
from mailroom_v4 import generate_main_menu, generate_report, generate_thankyou, write_letter_files, new_donor, add_donation, get_donors


def test_generate_main_menu_text():
  test_text = '''----------------------------------------------------------------------
1. Send a Thank You to a single donor.
2. Create a report.
3. Send letters to all donors.
4. Quit.
'''
  assert(generate_main_menu() == test_text)

def test_generate_report_text():
  test_text = '''Donor Name         |    Total Given |     Num Gifts |   Average Gift
--------------------------------------------------------------------
Bruce Lee            $     52246.75               3   $     17415.58
Bob Barker           $     24456.24               2   $     12228.12
Kermit the Frogg     $     23475.20               2   $     11737.60
Roger Rabbit         $      4930.26               1   $      4930.26
Frodo Baggins        $      1249.44               1   $      1249.44
'''
  assert(generate_report() == test_text)

def test_generate_thankyou_report_text():
  test_text = '''----------------------------------------------------------------------
Dear Bruce Lee,
  Thank you for all 3 of your generous donations for a total of 52246.75!
We will put the money to good use.
Sincerely,
 -Me
'''
  assert(generate_thankyou("Bruce Lee") == test_text)

def test_generate_thankyou_new_donation():
  test_text = '''----------------------------------------------------------------------
Dear Bruce Lee,
  Thank you for your generous donation of 232.12!
That brings your total of 3 donation(s) to $52246.75
Sincerely,
 -Me
'''
  assert(generate_thankyou("Bruce Lee", 232.12, True) == test_text)

def test_generate_thankyou_unknown_donor():
  with pytest.raises(KeyError):
    generate_thankyou("Adam West")
  with pytest.raises(KeyError):
    generate_thankyou("Adam West", 1232.12, True)

def test_write_letter_files():
  test_written = {'bob barker': 'bob_barker.txt',
    'bruce lee': 'bruce_lee.txt',
    'frodo baggins': 'frodo_baggins.txt',
    'kermit the frog': 'kermit_the_frog.txt',
    'roger rabbit': 'roger_rabbit.txt'}
  assert(write_letter_files() == test_written)

def test_new_donor():
  test_donor = {'name': 'Adam West', 'total': 0, 'donations': 0}
  test_all_donors = {'adam west': {'donations': 0, 'name': 'Adam West', 'total': 0},
    'bob barker': {'donations': 2, 'name': 'Bob Barker', 'total': 24456.24},
    'bruce lee': {'donations': 3, 'name': 'Bruce Lee', 'total': 52246.75},
    'frodo baggins': {'donations': 1, 'name': 'Frodo Baggins', 'total': 1249.44},
    'kermit the frog': {'donations': 2, 'name': 'Kermit the Frogg', 'total': 23475.2},
    'roger rabbit': {'donations': 1, 'name': 'Roger Rabbit', 'total': 4930.26}}
  assert(new_donor('Adam West') == test_donor)
  assert(get_donors() == test_all_donors)

def test_add_donation():
  test_donor = {'donations': 1, 'name': 'Adam West', 'total': 1122.33}
  test_all_donors = {'adam west': {'donations': 1, 'name': 'Adam West', 'total': 1122.33},
    'bob barker': {'donations': 2, 'name': 'Bob Barker', 'total': 24456.24},
    'bruce lee': {'donations': 3, 'name': 'Bruce Lee', 'total': 52246.75},
    'frodo baggins': {'donations': 1, 'name': 'Frodo Baggins', 'total': 1249.44},
    'kermit the frog': {'donations': 2, 'name': 'Kermit the Frogg', 'total': 23475.2},
    'roger rabbit': {'donations': 1, 'name': 'Roger Rabbit', 'total': 4930.26}}
  assert(add_donation('Adam West', 1122.33) == test_donor)
  assert(get_donors() == test_all_donors)

def test_add_donation_new_donor():
  test_donor = {'donations': 1, 'name': 'Han Solo', 'total': 3322.11}
  test_all_donors = {'adam west': {'donations': 1, 'name': 'Adam West', 'total': 1122.33},
    'bob barker': {'donations': 2, 'name': 'Bob Barker', 'total': 24456.24},
    'bruce lee': {'donations': 3, 'name': 'Bruce Lee', 'total': 52246.75},
    'frodo baggins': {'donations': 1, 'name': 'Frodo Baggins', 'total': 1249.44},
    'kermit the frog': {'donations': 2, 'name': 'Kermit the Frogg', 'total': 23475.2},
    'roger rabbit': {'donations': 1, 'name': 'Roger Rabbit', 'total': 4930.26},
    'han solo': test_donor}

  assert(add_donation('Han Solo', 3322.11) == test_donor)
  assert(get_donors() == test_all_donors)

def test_written_file_outputs():
  test_written = {'adam west': 'adam_west.txt',
    'bob barker': 'bob_barker.txt',
    'bruce lee': 'bruce_lee.txt',
    'frodo baggins': 'frodo_baggins.txt',
    'han solo': 'han_solo.txt',
    'kermit the frog': 'kermit_the_frog.txt',
    'roger rabbit': 'roger_rabbit.txt'}
  assert(write_letter_files() == test_written)

def test_written_file_contents():
  test_first_line = "-" * 70 + "\n"
  test_second_line = "Dear Adam West,\n"
  f = open("adam_west.txt", "r")
  actual_first_line = f.readline()
  actual_second_line = f.readline()
  assert(actual_first_line == test_first_line)
  assert(actual_second_line == test_second_line)
