# Webscraping
COSC490 Senior Project Submission
This is a tool used to pull data from the Open Data Network using the Socrata Api, and scrape the Bureau of Labor Statistics website to get data tables to upload onto the EIDC Redivis database.

Every tables is labeled in the format of [table source abbreviated]_[YYYY-MM-DD], with the date being the date of access.

The soures are the:
CDC Behavioural Risk Factor Surveillance System 2010 and 2011 (BRF2010, BRF2011)
Labor Area Unemployment Statistics current/historical highs and lows, as well as auto, which downloads every table listed https://www.bls.gov/lau/tables.htm (LAU_Auto and LAU_Data_Current)
Open Data Chicago energy Transformed Usage from 2010 (ODC)
CDC PLACES Local data for better health 2022 and 2021 release (PLACES2021, PLACES2022)

In the future, this tool must be expanded to cover more websites and API, with the eventual goal of being to automatically update any and every dataset listed on the EIDC Redivis Platform.

**To run the scripts**: 
Download scrapy: pip install scrapy
To use the scripts either run the RunAll.py file or Use the following command lines:
  LAU_Data.py: scrapy runspider LAU_Data.py -o filename.csv
  LAU_tables.py: scrapy runspider LAU_tables.py
  LAU_Auto.py: scrapy runspider LAU_Auto.py

Known Issues:
Issue: Occasionally, LAU_Auto.py will have the error "twisted.internet.error.ReactorNotRestartable" and will not properly scrape the tables.
Solution: in the process.start() command, include stop_after_crawl=False, which will cause the scraper to keep running indefinitely rather than restarting for each table.

Issue: LAU_Auto.py runs indefinitely, causeing anything after it to never run.
Solution: Still being worked on.
