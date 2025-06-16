from ...extensions import ma
from ...models     import Mechanic

class MechanicSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Mechanic
        load_instance = True
        include_fk   = True
        load_only    = ('assignments',)
