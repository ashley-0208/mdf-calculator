import tkinter as tk
from tkinter import ttk

from data_manager import add_material
from data_manager import load_materials
from data_manager import delete_material
from data_manager import update_material

from calculator import calculate_piece_price


# -------------------------
# FUNCTIONS
# -------------------------
selected_material_name = None


def refresh_materials():

    # پاک کردن جدول
    for row in materials_table.get_children():
        materials_table.delete(row)

    # گرفتن اطلاعات
    materials = load_materials()

    # اضافه کردن به جدول
    for material in materials:

        materials_table.insert(
            "",
            tk.END,
            values=(
                material["name"],
                int(material["width"]),
                int(material["height"]),
                f"{int(material['price']):,}"
            )
        )


def add_new_material():

    try:

        name = name_entry.get().strip()

        width = float(width_entry.get())
        height = float(height_entry.get())

        price_text = price_entry.get()

        # حذف کاما
        price_text = price_text.replace(",", "")

        price = float(price_text)

        # چک خالی بودن
        if not name:
            result_label.config(
                text="Material name is required."
            )
            return

        # ذخیره
        add_material(
            name,
            width,
            height,
            price
        )

        # آپدیت جدول
        refresh_materials()

        # پاک کردن input ها
        clear_inputs()
        update_combobox()

        result_label.config(
            text="Material added successfully."
        )

    except ValueError:

        result_label.config(
            text="Please enter valid numbers."
        )


def clear_inputs():

    name_entry.delete(0, tk.END)

    width_entry.delete(0, tk.END)
    height_entry.delete(0, tk.END)

    price_entry.delete(0, tk.END)


def update_combobox():

    materials = load_materials()

    names = []

    for material in materials:

        names.append(material["name"])

    material_combobox["values"] = names


def calculate_price():
    print("button works")
    try:

        selected_material = material_combobox.get()

        piece_width = float(piece_width_entry.get())
        piece_height = float(piece_height_entry.get())

        materials = load_materials()

        for material in materials:

            if material["name"] == selected_material:

                final_price = calculate_piece_price(
                    material["width"],
                    material["height"],
                    material["price"],
                    piece_width,
                    piece_height
                )

                formatted_price = f"{int(final_price):,}"

                price_result_label.config(
                    text=f"Final Price: {formatted_price}"
                )

                return

    except ValueError:

        price_result_label.config(
            text="Please enter valid numbers."
        )


def delete_selected_material():
    selected_item = materials_table.selection()

    if not selected_item:
        result_label.config(text="Please select a material.")
        return

    item_data = materials_table.item(selected_item)
    material_name = item_data["values"][0]
    delete_material(material_name)
    refresh_materials()
    update_combobox()
    result_label.config(text="Material deleted successfully!")


def select_material(event):
    global selected_material_name

    selected_item = materials_table.selection()

    if not selected_item:
        return

    item_data = materials_table.item(selected_item)

    values = item_data["values"]

    selected_material_name = values[0]

    #پاک کردن input
    clear_inputs()

    #قرار دادن اطلاعات
    name_entry.insert(0, values[0])

    width_entry.insert(0, values[1])

    height_entry.insert(0, values[2])

    #حذف کاما از قیمت
    price = str(values[3]).replace(',', '')

    price_entry.insert(0, price)


def edit_selected_material():

    global selected_material_name

    if not selected_material_name:

        result_label.config(
            text="Please select a material."
        )

        return

    try:

        new_name = name_entry.get().strip()

        width = float(width_entry.get())

        height = float(height_entry.get())

        price = float(
            price_entry.get().replace(",", "")
        )

        update_material(
            selected_material_name,
            new_name,
            width,
            height,
            price
        )

        refresh_materials()

        update_combobox()

        clear_inputs()

        selected_material_name = None

        result_label.config(
            text="Material updated successfully."
        )

    except ValueError:

        result_label.config(
            text="Please enter valid numbers."
        )


# -------------------------
# WINDOW
# -------------------------

root = tk.Tk()

root.title("MDF Calculator")

root.geometry("700x900")
root.resizable(True, True)

# -------------------------
# TITLE
# -------------------------

title_label = tk.Label(
    root,
    text="Materials Manager",
    font=("Arial", 18, "bold")
)

title_label.pack(pady=10)


# -------------------------
# INPUTS FRAME
# -------------------------

input_frame = tk.Frame(root)

input_frame.pack(pady=10)


# Row 1
tk.Label(
    input_frame,
    text="Material Name"
).grid(row=0, column=0, padx=5, pady=5)

name_entry = tk.Entry(
    input_frame,
    width=20
)

name_entry.grid(row=0, column=1, padx=5, pady=5)


tk.Label(
    input_frame,
    text="Width"
).grid(row=0, column=2, padx=5, pady=5)

width_entry = tk.Entry(
    input_frame,
    width=10
)

width_entry.grid(row=0, column=3, padx=5, pady=5)


tk.Label(
    input_frame,
    text="Height"
).grid(row=0, column=4, padx=5, pady=5)

height_entry = tk.Entry(
    input_frame,
    width=10
)

height_entry.grid(row=0, column=5, padx=5, pady=5)


tk.Label(
    input_frame,
    text="Price"
).grid(row=0, column=6, padx=5, pady=5)

price_entry = tk.Entry(
    input_frame,
    width=15
)

price_entry.grid(row=0, column=7, padx=5, pady=5)

# -------------------------
# BUTTON
# -------------------------

add_button = tk.Button(
    root,
    text="Add Material",
    width=20,
    command=add_new_material
)

add_button.pack(pady=5)

delete_button = tk.Button(
    root,
    text="Delete",
    width=20,
    command=delete_selected_material
)

delete_button.pack(pady=5)

edit_button = tk.Button(
    root,
    text="Edit Selected",
    width=20,
    bg="orange",
    command=edit_selected_material
)

edit_button.pack(pady=5)

# -------------------------
# RESULT LABEL
# -------------------------

result_label = tk.Label(
    root,
    text="",
    fg="green"
)

result_label.pack()


# -------------------------
# TABLE
# -------------------------

materials_table = ttk.Treeview(
    root,
    columns=("Name", "Width", "Height", "Price"),
    show="headings",
    height=7
)

materials_table.heading("Name", text="Name")
materials_table.heading("Width", text="Width")
materials_table.heading("Height", text="Height")
materials_table.heading("Price", text="Price")


materials_table.column("Name", width=180)
materials_table.column("Width", width=100)
materials_table.column("Height", width=100)
materials_table.column("Price", width=180)

materials_table.bind("<<TreeviewSelect>>", select_material)

materials_table.pack(pady=20)


# -------------------------
# CALCULATOR SECTION
# -------------------------

separator = tk.Label(
    root,
    text="-----------------------------------"
)

separator.pack(pady=10)


calculator_title = tk.Label(
    root,
    text="Piece Calculator",
    font=("Arial", 16, "bold")
)

calculator_title.pack(pady=10)


# Material Select
tk.Label(
    root,
    text="Select Material"
).pack()

material_combobox = ttk.Combobox(
    root,
    state="readonly"
)

material_combobox.pack(pady=5)


# Piece Width
tk.Label(
    root,
    text="Piece Width"
).pack()

piece_width_entry = tk.Entry(root)

piece_width_entry.pack(pady=5)


# Piece Height
tk.Label(
    root,
    text="Piece Height"
).pack()

piece_height_entry = tk.Entry(root)

piece_height_entry.pack(pady=5)

tk.Label(root, text="").pack(pady=5)

calculate_button = tk.Button(
    root,
    text="Calculate Price",
    command=calculate_price
)

calculate_button.pack(pady=10)

# Result Label
price_result_label = tk.Label(
    root,
    text="Final Price: ",
    font=("Arial", 14, "bold"),
    fg="blue"
)

price_result_label.pack(pady=10)

# -------------------------
# START
# -------------------------

refresh_materials()
update_combobox()
root.mainloop()