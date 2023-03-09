from math import radians, cos, sin, asin, sqrt
import pandas as pd

def haversine_distance(lat1, lon1, lat2, lon2):
    '''
    this function will take the user input address as reference and calculate the distance to each parking, 
    then return the top n closest parking
    '''
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # Haversine formula
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 

    r = 3956

    distance = c * r

    return distance

# use user input as reference, this needs to link with flask
ref_lat, ref_lng = 47.6949, -122.3394

df_paid = pd.read_pickle("df_paid.pkl")
df_free = pd.read_pickle("df_free.pkl")
merged_df = pd.concat([df_paid,df_free])

distances = []
for index, row in merged_df.iterrows():
    lat= row['lngs'][0]
    lon = row['lats'][0]
    distance = haversine_distance(ref_lng,ref_lat,lon, lat)
    distances.append((lat, lon, distance,row['unit_desc'],row['parking_cat'],row['lats'],row['lngs'],row['colors']))
    
distances = pd.DataFrame(distances, columns = ['lat', 'lon', 'distance','unit_desc','parking_cat','lats','lngs','colors'])
output_df = distances.sort_values(by=['distance'])[:10]
