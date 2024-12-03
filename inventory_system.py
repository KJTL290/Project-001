# Inventory Management System
# Created by: Kim Joshua T. Lopez, BSIT 2B

import tkinter as tk
from tkinter import messagebox
from tkinter import ttk


class InventoryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Inventory Management System")
        self.root.geometry("700x500")

        # Inventory list to store items
        self.inventory = []

        # Frames
        self.frame_top = tk.Frame(self.root)
        self.frame_top.pack(pady=10)

        self.frame_middle = tk.Frame(self.root)
        self.frame_middle.pack(pady=10)

        self.frame_bottom = tk.Frame(self.root)
        self.frame_bottom.pack(pady=10)

        # Labels and Entry Fields
        self.label_name = tk.Label(self.frame_top, text="Item Name:")
        self.label_name.grid(row=0, column=0, padx=5, pady=5)

        self.entry_name = tk.Entry(self.frame_top)
        self.entry_name.grid(row=0, column=1, padx=5, pady=5)

        self.label_quantity = tk.Label(self.frame_top, text="Quantity:")
        self.label_quantity.grid(row=1, column=0, padx=5, pady=5)

        self.entry_quantity = tk.Entry(self.frame_top)
        self.entry_quantity.grid(row=1, column=1, padx=5, pady=5)

        self.label_price = tk.Label(self.frame_top, text="Price:")
        self.label_price.grid(row=2, column=0, padx=5, pady=5)

        self.entry_price = tk.Entry(self.frame_top)
        self.entry_price.grid(row=2, column=1, padx=5, pady=5)

        # Buttons
        self.btn_add = tk.Button(self.frame_middle, text="Add Item", command=self.add_item)
        self.btn_add.grid(row=0, column=0, padx=5, pady=5)

        self.btn_update = tk.Button(self.frame_middle, text="Update Item", command=self.update_item)
        self.btn_update.grid(row=0, column=1, padx=5, pady=5)

        self.btn_delete = tk.Button(self.frame_middle, text="Delete Item", command=self.delete_item)
        self.btn_delete.grid(row=0, column=2, padx=5, pady=5)

        self.btn_clear = tk.Button(self.frame_middle, text="Clear Fields", command=self.clear_fields)
        self.btn_clear.grid(row=0, column=3, padx=5, pady=5)

        # Treeview (Table)
        self.tree = ttk.Treeview(self.frame_bottom, columns=("Name", "Quantity", "Price"), show="headings")
        self.tree.heading("Name", text="Item Name")
        self.tree.heading("Quantity", text="Quantity")
        self.tree.heading("Price", text="Price")
        self.tree.pack()

        self.tree.bind("<Double-1>", self.load_selected_item)

    def add_item(self):
        name = self.entry_name.get().strip()
        quantity = self.entry_quantity.get().strip()
        price = self.entry_price.get().strip()

        if name and quantity.isdigit() and price.replace('.', '', 1).isdigit():
            self.inventory.append((name, int(quantity), float(price)))
            self.refresh_table()
            self.clear_fields()
        else:
            messagebox.showerror("Invalid Input", "Please provide valid item details.")

    def update_item(self):
        selected = self.tree.focus()
        if selected:
            index = self.tree.index(selected)
            name = self.entry_name.get().strip()
            quantity = self.entry_quantity.get().strip()
            price = self.entry_price.get().strip()

            if name and quantity.isdigit() and price.replace('.', '', 1).isdigit():
                self.inventory[index] = (name, int(quantity), float(price))
                self.refresh_table()
                self.clear_fields()
            else:
                messagebox.showerror("Invalid Input", "Please provide valid item details.")
        else:
            messagebox.showwarning("No Selection", "Please select an item to update.")

    def delete_item(self):
        selected = self.tree.focus()
        if selected:
            index = self.tree.index(selected)
            del self.inventory[index]
            self.refresh_table()
        else:
            messagebox.showwarning("No Selection", "Please select an item to delete.")

    def load_selected_item(self, event):
        selected = self.tree.focus()
        if selected:
            index = self.tree.index(selected)
            name, quantity, price = self.inventory[index]

            self.entry_name.delete(0, tk.END)
            self.entry_name.insert(0, name)

            self.entry_quantity.delete(0, tk.END)
            self.entry_quantity.insert(0, quantity)

            self.entry_price.delete(0, tk.END)
            self.entry_price.insert(0, price)

    def clear_fields(self):
        self.entry_name.delete(0, tk.END)
        self.entry_quantity.delete(0, tk.END)
        self.entry_price.delete(0, tk.END)

    def refresh_table(self):
        for row in self.tree.get_children():
            self.tree.delete(row)

        for item in self.inventory:
            self.tree.insert("", tk.END, values=item)


# Main Program
if __name__ == "__main__":
    root = tk.Tk()
    app = InventoryApp(root)
    root.mainloop()
