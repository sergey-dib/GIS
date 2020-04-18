import geopandas as gpd
import pandas as pd
import pysal.viz.mapclassify as mc
import matplotlib.pyplot as plt


list_path = [
    './shp_lab/TravelTimes_to_5878070_Jumbo.txt',
    './shp_lab/TravelTimes_to_5878087_Dixi.txt',
    './shp_lab/TravelTimes_to_5902043_Myyrmanni.txt',
    './shp_lab/TravelTimes_to_5944003_Itis.txt',
    './shp_lab/TravelTimes_to_5975373_Forum.txt',
    './shp_lab/TravelTimes_to_5978593_Iso_omena.txt',
    './shp_lab/TravelTimes_to_5980260_Ruoholahti.txt'
]

list_name = ["Jumbo", "Dixi", "Myyrmanni", "Itis", "Forum", "Iso_omena", "Ruoholahti"]
shapep = './shp_lab/MetropAccess_YKR_grid_EurefFIN.shp'

gdata = gpd.read_file(shapep).to_crs(epsg=3879)

dt_columns = ['pt_r_tt', 'from_id', 'to_id']

column_list = []

for i in  range(len(list_path)):
    # create list of selected rows
    # read file with delimiter ';'
    # print(list_name[i])
    data = pd.read_csv(list_path[i], delimiter=';')
    # column_name = dt_columns[0] + "_" + str(data["to_id"][0])
    column_name = list_name[i]
    column_list.append(column_name)
    gdata[column_name] = data["pt_r_tt"]

gdata["min_time_pt"] = gdata[column_list].min(axis=1)
gdata["dominant_service"] = gdata[column_list].idxmin(axis=1)

n_classes = 3

classifier = mc.NaturalBreaks.make(k=n_classes)

classifications = gdata[['min_time_pt']].apply(classifier)

# output(classifications)

classifications.columns = ['nb_min_pt_r_tt']

acc = gdata.join(classifications)

acc.plot(column="nb_min_pt_r_tt", linewidth=0, legend=True)
plt.title('min_time_pt')
plt.tight_layout()

# the best origin by time
plt.show()


acc.plot(column="dominant_service", linewidth=0, legend=True)
plt.tight_layout()
plt.title('dominant_service')
plt.show()

