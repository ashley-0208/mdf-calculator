import json

from database import (
    create_table,
    add_material_db
)

create_table()

with open(
    "materials.json",
    "r",
    encoding="utf-8"
) as file:

    materials = json.load(file)

for material in materials:

    add_material_db(
        material["name"],
        material["width"],
        material["height"],
        material["price"]
    )

print("Migration complete.")