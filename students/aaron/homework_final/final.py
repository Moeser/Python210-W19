#=========================================
# Title: Final exercise for Python210-W19
# Changelog:
# Aaron Devey,2019-03-17,Created
#=========================================

import sqlite3

class Table:
  schema = {}
  rows = []

  # append a row with values in kwargs
  def append_row(self, **kwargs):
    columns_text = ", ".join(kwargs.keys())
    values = []
    for v in kwargs.values():
      if type(v) == str:
        values.append("'{}'".format(v))
      else:
        values.append("{}".format(str(v)))
    values_text = ", ".join(values)
    sql = "INSERT INTO {} ({}) VALUES ({})".format(self.table_name, columns_text, values_text)
    self._db_write(sql)

  # delete row matching all key=value pairs
  def delete_row(self, kv):
    where_text = self._build_clause(kv)
    sql = "DELETE FROM {} WHERE {}".format(self.table_name, where_text)
    self._db_write(sql)

  # update a row matching all key=value pairs to kwargs
  def update_row(self, kv, **kwargs):
    set_text = ""
    where_text = self._build_clause(kv)
    set_text = self._build_clause(kwargs, ", ")
    sql = "UPDATE {} SET {} WHERE {}".format(self.table_name, set_text, where_text)
    self._db_write(sql)

  # create table
  def db_prepare(self):
    column_text = ','.join([ ' '.join([k,v]) for k,v in self.schema['columns'].items()])
    pkey_text = ", ".join(self.schema['primary_keys'])
    if len(pkey_text) > 0:
      table_format = "CREATE TABLE IF NOT EXISTS {} ( {}, {} )"
      pkey_text = "PRIMARY KEY ( {} )".format(pkey_text)
    else:
      table_format = "CREATE TABLE IF NOT EXISTS {} ( {} )"
    sql = table_format.format(self.table_name, column_text, pkey_text)
    self._db_write(sql)

  # Read all rows and all columns in the table
  def db_read_all(self):
    sql = "SELECT * FROM {}".format(self.table_name)
    self.rows = self._db_read(sql)
    return self.rows

  # Read all rows matching the key=value pairs
  # columns defaults to all columns.
  def read_rows(self, kv, columns = None):
    column_text = ""
    if columns == None:
      column_text = "*"
    else:
      column_text = ",".join(columns)
    where_text = self._build_clause(kv)
    sql = "SELECT {} FROM {} WHERE {}".format(column_text, self.table_name, where_text)
    rows = self._db_read(sql)
    return rows

  # build a clause from k=v pairs
  def _build_clause(self, kv, clause_seperator = ' AND '):
    clauses = []
    for k,v in kv.items():
      if type(v) == str:
        clauses.append("{}='{}'".format(k,v))
      else:
        clauses.append("{}={}".format(k,str(v)))
    return clause_seperator.join(clauses)

  def _db_connect(self):
    try:
      conn = sqlite3.connect('final.db')
    except Exception as e:
      raise(Exception("Could not connect to database: {}".format(e)))
    return conn

  def _db_read(self, query):
    conn = self._db_connect()
    rows = []
    print("DEBUG: executing", query)
    try:
      cursor = conn.cursor()
      cursor.execute(query)
      rows = cursor.fetchall()
      conn.close()
    except Exception as e:
      raise(Exception("Could not read from database: {}".format(e)))
    return rows

  def _db_write(self, query):
    conn = self._db_connect()
    print("DEBUG: executing", query)
    try:
      cursor = conn.cursor()
      cursor.execute(query)
      conn.commit()
      conn.close()
    except Exception as e:
      raise(Exception("Could not make mutating call to database: {}".format(e)))

  def count(self):
    return len(rows)

  def update_self(self):
    # updates properties with new values using the function map
    for k,v in self.map.items():
      locals[v] = k()

  def __init__(self):
    self.db_prepare()
    

class Inventory(Table):
  schema = {'columns': {'InventoryId': 'int',
                        'InventoryDate': 'char(100)'},
            'primary_keys': ['InventoryId']}
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
