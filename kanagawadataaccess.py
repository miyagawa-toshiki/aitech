from var import Var
from  db import DB
class DataAccess:
    def get_spots(self):
        query = "SELECT * FROM spot "
        data = ()
        db = DB(Var.hostname, Var.port, Var.dbname, Var.username, Var.password)
        return db.execute(query, data)
    def get_spots_by_area(self, spot_area):
        query = "SELECT * FROM data_spot WHERE spot_area = %s "
        data = (str(spot_area), )
        db = DB(Var.hostname, Var.port, Var.dbname, Var.username, Var.password)
        return db.execute(query, data)