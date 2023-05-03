import pandas as pd
from sodapy import Socrata
from pathlib import Path
import schedule
import datetime 
import random

#someone who is an offical employee/member of EIDC should eventually replace these
key= '8s3p9j9zmrv1zdms76or14y76'
secretKey = '4wirg8yv4g6z8ln9d3ph1smrik9h3fhu1wrlefnamhskvajjgl'
token = 'LH3i88LqbgkhXO9mZjew0cQJS'
secretToken = 'KcTli0ejvXUKC4uPtuJNgaMAj2MJpjr3CYie'
user = 'blakeeller00@gmail.com'
passw = 'zH5Euqjd6S9aCW3'

#dictionary of every tables to be downloaded. To add new tables, use the format (name) : [(table_id), (base url)]
codes = {
  "BRF2011": ["dttw-5yxu","chronicdata.cdc.gov"],
  "BRF2010": ["y4ft-s73h","chronicdata.cdc.gov"],
  "PLACES2022": ["swc5-untb","chronicdata.cdc.gov"],
  "PLACES2021": ["373s-ayzu","chronicdata.cdc.gov"],
  "ODC": ["8yq3-m6wp","data.cityofchicago.org"]
}
for i in codes:
  client = Socrata(codes[i][1], token, username= user, password= passw, timeout=10)
  results = client.get(codes[i][0], limit=2000) #data table limited for testsing purposes, remove for proper use.
  client.close()
  results_df = pd.DataFrame.from_records(results)
  #print(results_df.head())

  filename = i + "_" + str(datetime.date.today())
  filepath = Path("senior_project\\senior_project\\CSVs\\{}.csv".format(filename))
  filepath.parent.mkdir(parents=True, exist_ok=True)  
  results_df.to_csv(filepath) 