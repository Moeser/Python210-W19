#!/usr/bin/env python3

import final as db

p = db.Product()
i = db.Inventory()
ic = db.InventoryCount()

p.append_row(ProductId=1, ProductName='Staples')
p.append_row(ProductId=2, ProductName='Erasers')
p.update_row({'ProductId': 1}, ProductName='Deluxe Staples')
p.update_row({'ProductId': 2}, ProductName='Deluxe Erasers')
print(p.read_rows({'ProductId': 1}, ['ProductName']))
print(p.read_rows({'ProductId': 2}, ['ProductName']))
p.delete_row({'ProductId': 1})
p.delete_row({'ProductId': 2})

