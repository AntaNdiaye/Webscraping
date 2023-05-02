import pandas as pd
from sodapy import Socrata
from pathlib import Path
import schedule
import datetime 
import random

key= '8s3p9j9zmrv1zdms76or14y76'
secretKey = '4wirg8yv4g6z8ln9d3ph1smrik9h3fhu1wrlefnamhskvajjgl'
token = 'LH3i88LqbgkhXO9mZjew0cQJS'
secretToken = 'KcTli0ejvXUKC4uPtuJNgaMAj2MJpjr3CYie'

#Open Data Chicago https://data.cityofchicago.org/resource/8yq3-m6wp.json
#behavioral risk factor 2011 to present = dttw-5yxu
#behavioral risk factor 2010 and prior = waxm-p5qv
#PLACES: Local Data for Better Health, County Data 2022 = swc5-untb
#PLACES: Local Data for Better Health, Census Tract Data 2021 = 373s-ayzu

codes = {
  "BRF2011": "dttw-5yxu",
  "BRF2010": "y4ft-s73h",
  "PLACES2022": "swc5-untb",
  "PLACES2021": "373s-ayzu",
  "ODC": "8yq3-m6wp"
}
#print("randomly choosing from Open Data Chicago 2010 Energy Usage, Behavioral Risk Factor SS 2011 and 2010, and CDC PLACES 2022 and 2021")
#choice = random.randint(0, 4)
codeslist=list(codes)
#print(choice)
for i in codes:
  if i =="ODC":
    client = Socrata("data.cityofchicago.org", token, username= 'blakeeller00@gmail.com', password='zH5Euqjd6S9aCW3', timeout=10)
  else:
    client = Socrata("chronicdata.cdc.gov", token, username= 'blakeeller00@gmail.com', password='zH5Euqjd6S9aCW3', timeout=10)
  results = client.get(codes[i], limit=2000)
  client.close()
  results_df = pd.DataFrame.from_records(results)
  #print(results_df.head())

  filename = i + "_" + str(datetime.date.today())
  filepath = Path("C:\\Users\\Blake's PC\\Documents\\GitHub\\Webscraping\\senior_project\\senior_project\\CSVs\\{}.csv".format(filename))

  filepath.parent.mkdir(parents=True, exist_ok=True)  
  results_df.to_csv(filepath) 
