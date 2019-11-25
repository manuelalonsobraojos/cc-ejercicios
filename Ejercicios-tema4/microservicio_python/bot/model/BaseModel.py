from peewee import *

db = PostgresqlDatabase(None)

class BaseModel(Model):
    """
    Modelo base desde el cual heredan el resto de modelos y desde el cual se realizará la conexión a ña BD
    """
    class Meta:
        database = db
