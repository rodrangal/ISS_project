import time
import requests
import json
import plotly.express as px
import pandas as pd

#function to get data using the API
def get_data():
    baseurl = 'http://api.open-notify.org/iss-now.json'
    resp = requests.get(baseurl)
    return resp.json()

#user's inouts
interval = input('Interval between datapoints (in seconds)? ')
print('Press ctl+c to stop!')

#prints the data and saves it into a list until the loop is stopped by the user
datapoints = 0
lst = []
try:
    while True:
        #calls function to get data
        location = get_data()
        #rearranges data in json format
        df = pd.DataFrame([[location['timestamp'], location['iss_position']['latitude'], location['iss_position']['longitude']]], columns=['timestamp', 'latitude', 'longitude'])
        df.to_json(orient='index')
        #plots data
        fig = px.scatter_geo(df, lat = 'latitude', lon = 'longitude', hover_name = 'timestamp')
        #title
        fig.update_layout(title = 'ISS Trajectory', title_x = 1)
        #prints plot
        fig.show()
        #saves data into list
        lst.append(location)
        #this is used later to save the data into a csv file
        datapoints += 1
        #sleeps for the indicated value given by the user
        time.sleep(int(interval))
except KeyboardInterrupt:
    pass

#writes the data into a csv file
outfile = open('results.csv', 'w')
outfile.write('Timestamp,Latitude,Longitude')
outfile.write('\n')
for t in range(datapoints):
    row_string = '{},{},{}'.format(lst[t]['timestamp'], lst[t]['iss_position']['latitude'], lst[t]['iss_position']['longitude'])
    outfile.write(row_string)
    outfile.write('\n')
outfile.close