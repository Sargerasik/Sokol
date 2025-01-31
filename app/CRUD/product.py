from app.models import Product
import inspect

def create_product(price, name, articul, description, image, material, category):
    item = Product(
        price=price, name=name, articul=articul, description=description,
        image=image, material=material, category=category
    )
    item.save()
    return item
