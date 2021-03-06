from tkinter import *
from tkinter import ttk
import mysql.connector
from test.queries import queries as q

# Creating root window
root = Tk()
print(root)
# root.geometry("1000x1000")
# root.state("zoomed")

button_frame = LabelFrame(root, width=root.winfo_width(), height=root.winfo_height(), text="Database viewing functions")
# button_frame.pack(side=TOP, fill='x', pady=20)
button_frame.grid(row=0, column=0, sticky='ew')

product_button = Button(button_frame, text="See product list", command=lambda: q.print_result(q.get_products(), table_frame))
product_button.grid(row=0, column=0, columnspan=1, sticky='WE')
shipment_button = Button(button_frame, text="See shipment list", command=lambda: q.print_result(q.get_shipments(), table_frame))
shipment_button.grid(row=0, column=1, columnspan=1, sticky='WE')
product_shipment_button = Button(button_frame, text="See product shipment list", command=lambda: q.print_result(q.get_product_shipment(), table_frame))
product_shipment_button.grid(row=0, column=2, columnspan=1, sticky='WE')


table_frame = LabelFrame(root, name="table_frame")
# table_frame.pack(side=TOP, fill='x', pady=20)
table_frame.grid(row=1, column=0, sticky='e')

side_frame = LabelFrame(root)
# side_frame.pack(side=RIGHT, fill='y', padx=10, anchor='nw')
side_frame.grid(row=1, column=4, sticky='nsew')
b = Button(side_frame, text="hello")
b.grid(row=0, column=0)
b1 = Button(side_frame, text="hello")
b1.grid(row=1, column=0)
b2 = Button(side_frame, text="hello")
b2.grid(row=2, column=0)

bottom_frame = LabelFrame(root, text="Database write functions")
bottom_frame.grid(row=2, column=0, sticky='ew')
add_product_button = Button(bottom_frame, text="Add new product", command=q.add_product_window)
add_product_button.grid(row=0, column=0)
update_product_button = Button(bottom_frame, text="Update a product", command=q.update_product_window)
update_product_button.grid(row=0, column=1)
delete_product_button = Button(bottom_frame, text="Delete a product", command=q.delete_product_window)
delete_product_button.grid(row=0, column=2)
add_shipment_button = Button(bottom_frame, text="Create new shipment", command=lambda: q.shipment_window('add'))
add_shipment_button.grid(row=1, column=0)
update_shipment_button = Button(bottom_frame, text="Update shipment", command=lambda: q.shipment_window('update'))
update_shipment_button.grid(row=1, column=1)
delete_shipment_button = Button(bottom_frame, text="Delete shipment", command=q.delete_shipment_window)
delete_shipment_button.grid(row=1, column=2)

q.set_root(root)

root.mainloop()

# if __name__ == '__main__':
#     from . import queries as q
