from model.ship import Ship


# Create a ship
def create_ship(db):
    print("------ Add Ship Util ------")
    ship = Ship(50, 100, 150, 200, 250, 300, "hello", True)
    print(ship)
    db.collection("Ship").document().set(ship.to_dict())
