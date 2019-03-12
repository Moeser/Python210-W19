import sqlite3

class Table:
  schema = {}
  rows = []
  map = {}

  def append_row(self):
    # call db_save_row
    # add to rows[]
    # call update_self
    pass

  def delete_row(self):
    # call db_delete_row
    # delete from rows[]
    # call update_self
    pass

  def update_row(self):
    # call db_save_row
    # update in rows[]
    # call update_self
    pass

  def db_delete_row(self):
    # delete from db
    pass

  def db_load_row(self):
    # select from db
    pass

  def db_save_row(self):
    # create if not exists, else update
    pass

  def db_prepare(self):
    # create table
    pass

  def count(self):
    return len(rows)

  update_self(self):
    # updates properties with new values using the function map
    for k,v in self.map.items():
      locals[v] = k()

class Inventory(Table):
  schema = {'columns': {'InventoryId': 'int',
                        'InventoryDate': 'char(100)'},
            'primary_keys': ['InventoryId']}
  map = {self.count: 'InventoryCount'}
  table_name = 'inventories'

class Product(Table):
  schema = {'columns': {'ProductId': 'int',
                        'ProductName': 'char(255)'},
            'primary_keys': ['ProductId']}
  table_name = 'products'

class InventoryCount(Table):
  schema = {'columns': {'ProductId': 'int',
                        'InventoryId': 'int',
                        'Count': 'int'},
            'primary_keys': ['ProductId', 'InventoryId']}
  table_name = 'inventory_counts'
