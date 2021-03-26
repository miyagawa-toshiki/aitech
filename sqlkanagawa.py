from dataaccess import DataAccess
from db import DB
da = DataAccess()
print("----")
spot_list = da.get_spots_by_area("神奈川")
for spot in spot_list:
    print(spot)
# spot_list = da.get_spots("神奈川")
# for spot in spot_list:
#     print(spot)