def calculate_piece_price(
    material_width,
    material_height,
    material_price,
    piece_width,
    piece_height
):

    # مساحت ورق کامل
    material_area = material_width * material_height

    # مساحت قطعه
    piece_area = piece_width * piece_height

    # قیمت هر سانتی متر
    price_per_cm = material_price / material_area

    # قیمت قطعه
    final_price = piece_area * price_per_cm

    return final_price
