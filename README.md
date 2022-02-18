# HEALTHCARE PRICE COMPARISON TOOL
#### Video Demo:  [https://youtu.be/jOi0XoNvrKs]
#### Description:

The healthcare system in the US is complicated. While healthcare costs continue to skyrocket, health insurance companies continually shift the cost of  care to the patient through  high deductibles, co insurance, copays and other cost sharing structures.  As an administrator of a women’s health clinic, I continually encounter patients who do not fully  understand what their insurance covers , and find themselves blindsided  when they receive their bills.

Until recently, hospitals, and insurance companies were not required to publish the actual prices of the services they perform nor the negotiated rate they charge health insurers..  One of the key portions of the Affordable Care Act now requires hospitals to publish these prices on their websites in a machine readable form.


The healthcare cost comparison tool was designed to aggregate these prices from  across multiple medical facilities and publish them in a central location. The goal is to assist patients  in developing a realistic estimate of their out of pocket costs.  This added price transparency will help patients make better informed financial decisions for their healthcare as well as encourage more competitive pricing among healthcare facilities.



The project consists of the following files:

**pricing.db**- SQLite database containing the hospital and procedure tables
**index.html**- contains radio buttons  to select the procedure, and a table to render the output
**app.py**-  Python/ flask app that executes the SQL based on the radio button selector
**styles.css**- stylesheet used to approximate the web styles we use on our existing website (www.drhesselmd.com) Bootstrap was also used for rendering the output.

I initially conceived this project to  access  and display pricing files from multiple facilities across the US as well as multiple medical specialties using python BeautifulSoup4  for web scraping/html parsing. I had to scrap this approach as several hospital sites blocked access to the data via this method.

In the interest of properly managing my time and scope, I opted to compile the data in .csv format  and import it  to the  pricing database. I decided to limit the scope to  5 OB/GYN procedures performed at 3 of the largest hospitals in New York City.  To that end, I configured a radio button list containing the procedures which are passed to  the sql database query when the user makes a selection.

As this is a tool that can benefit our patients, it's my intention to add this program  to our existing website(httpd://drhesselmd.com). Future iterations will contain all OB GYN pricing data across all of the major hospitals in the greater New York City area

