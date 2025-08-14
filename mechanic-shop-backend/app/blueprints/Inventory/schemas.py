from app.extensions import ma
from ...models import Inventory

class InventorySchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Inventory
        load_instance = True
        include_fk = True
        dump_only = ('item_id',)
