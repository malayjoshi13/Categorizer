# Product_Categorizer

Aim of this project is to develop a system which could first scrape Mamaearth's product details (like Product Name, Product Link, Rating, Reviews, MRP, Pack Size, Discount/Offers running on the product) and then use that data to train a product categorizer. Task of product categorizer will be to tell the category and key ingredient of a product based on the name of the product. So, taking Mamaearth Onion Hair Oil as an example, the key ingredient here is Onion and the category is Hair Oil.

Lets see the two files used in this project:

## 1) web_scraping.py
This file scrapes data (like Product Name, Product Link, Rating, Reviews, MRP, Pack Size, Discount/Offers running on the product) from mamaearth's website and save it in csv format file **scrapped_data.csv**.

a) Input 
![bandicam 2021-12-26 00-41-11-436](https://user-images.githubusercontent.com/71775151/147391998-b9e1621f-a785-400f-8711-c4b20d722230.jpg)

B) Output
![bandicam 2021-12-26 00-41-50-033](https://user-images.githubusercontent.com/71775151/147392009-e5f9309b-ce44-4c61-9494-bd047c44b2ce.jpg)
