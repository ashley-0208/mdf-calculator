import json
import os

FILE_NAME = "materials.json"


def load_materials():

    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)

    except json.JSONDecodeError:
        print("Json file is corrupted!")
        return []
    except FileNotFoundError:
        return []


def save_materials(materials):

    with open(FILE_NAME, "w") as file:
        json.dump(
            materials,
            file,
            indent=4
        )
    print(os.path.abspath(FILE_NAME))


def add_material(name, width, height, price):

    materials = load_materials()

    new_material = {
        "name": name,
        "width": width,
        "height": height,
        "price": price
    }

    materials.append(new_material)

    save_materials(materials)


def delete_material(name):
    materials = load_materials()
    updated_materials = []
    for material in materials:
        if material["name"] != name:
            updated_materials.append(material)
    save_materials(updated_materials)


def update_material(old_name, new_name, width, height, price):
    materials = load_materials()

    for material in materials:
        if material["name"] == old_name:
            material["name"] = new_name
            material["width"] = width
            material["height"] = height
            material["price"] = price

            break

    save_materials(materials)
