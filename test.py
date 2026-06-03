from data_manager import add_material
from data_manager import load_materials


add_material(
    "MDF",
    366,
    183,
    5000000
)

materials = load_materials()

print(materials)
