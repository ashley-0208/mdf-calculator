from flask import Flask
from flask import render_template
from flask import request
from flask import redirect

from data_manager import (
    load_materials,
    add_material,
    delete_material,
    update_material
)

from calculator import calculate_piece_price

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():

    final_price = None

    if request.method == "POST":

        form_type = request.form["form_type"]

        # Add Material
        if form_type == "add_material":

            name = request.form["name"]

            width = float(request.form["width"])

            height = float(request.form["height"])

            price = float(request.form["price"])

            add_material(
                name,
                width,
                height,
                price
            )

            return redirect("/")

        # Calculate Price
        elif form_type == "calculate_price":

            selected_material = request.form["material"]

            piece_width = float(
                request.form["piece_width"]
            )

            piece_height = float(
                request.form["piece_height"]
            )

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

                    break

    materials = load_materials()

    return render_template(
        "index.html",
        materials=materials,
        final_price=final_price
    )


@app.route("/delete/<material_name>")
def delete(material_name):

    delete_material(material_name)

    return redirect("/")


@app.route("/edit/<material_name>", methods=["GET", "POST"])
def edit(material_name):

    materials = load_materials()

    selected_material = None

    for material in materials:

        if material["name"] == material_name:

            selected_material = material

            break

    if request.method == "POST":

        new_name = request.form["name"]

        width = float(request.form["width"])

        height = float(request.form["height"])

        price = float(request.form["price"])

        update_material(
            material_name,
            new_name,
            width,
            height,
            price
        )

        return redirect("/")

    return render_template(
        "edit.html",
        material=selected_material
    )


if __name__ == "__main__":
    app.run(debug=True)