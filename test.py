from database import *

create_table()

update_material_db(
    "MDF Test",
    "MDF Premium",
    366,
    183,
    9000000
)

print(get_all_materials())