import geopandas as gpd
import matplotlib.pyplot as plt
import pandas as pd
import pysal as ps


def binaryClassifier(row, source_col, output_col, threshold):
    if row[source_col] < threshold:
        row[output_col] = 0
    else:
        row[output_col] = 1
    return row


# set txt file path
filep = './shp_lab/TravelTimes_to_5878087_Dixi.txt'
shapep = './shp_lab/MetropAccess_YKR_grid_EurefFIN.shp'

# read file with delimiter ';'
data = pd.read_csv(filep, sep=';', usecols=['pt_r_tt', 'car_r_t', 'from_id', 'to_id'])

gdata = gpd.read_file(shapep).to_crs(epsg=3879)

data = gdata.join(data)

# класифікований час подорожі
data.plot(column='pt_r_tt', linewidth=0.05, )
plt.title('Гражданский транспорт')
plt.tight_layout()
plt.show()

data.plot(column='car_r_t', linewidth=0.05)
plt.title('Автомобили')
plt.tight_layout()

pr_time = data['pt_r_tt']
pr_mean_time = pr_time.mean()

# print(pr_mean_time)

# detect suitable trip by using binary classifier

class_data = data.copy()

class_data['suitable_trip'] = None

class_data = class_data.apply(binaryClassifier, source_col='pt_r_tt', output_col='suitable_trip',
                    threshold=pr_mean_time, axis=1)

class_data.plot(column='suitable_trip', linewidth=0.05, cmap="seismic", legend=True)
plt.tight_layout()
plt.show()
