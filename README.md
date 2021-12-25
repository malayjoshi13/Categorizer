# Product_Categorizer

Aim of this project is to develop a system which could first scrape Mamaearth's product details (like Product Name, Product Link, Rating, Reviews, MRP, Pack Size, Discount/Offers running on the product, Product Category, Ingredient) and then use that data to train a product categorizer. Task of product categorizer will be to tell the category and key ingredient of a product based on the name of the product. So, taking Mamaearth Onion Hair Oil as an example, the key ingredient here is Onion and the category is Hair Oil.

Lets see the two files used in this project:

## 1) web_scraping.py
This file scrapes data (like Product Name, Product Link, Rating, Reviews, MRP, Pack Size, Discount/Offers running on the product, Product Category, Ingredient) from mamaearth's website and save it in csv format file **scrapped_data.csv**.

A) Input (mamaearth's **webpage** on link 'https://mamaearth.in/product-category/beauty')
![bandicam 2021-12-26 00-41-11-436](https://user-images.githubusercontent.com/71775151/147391998-b9e1621f-a785-400f-8711-c4b20d722230.jpg)

B) Output (**scrapped_data.csv** file)
![bandicam 2021-12-26 00-41-50-033](https://user-images.githubusercontent.com/71775151/147392009-e5f9309b-ce44-4c61-9494-bd047c44b2ce.jpg)
<br><br>

## 2) classifier.py
This file first try to learn csv data given by web_scraping.py file using various **SVM and its multiple variants**. Then it predicts category and key ingredient of products present in test data by just using their names. The test data is prepared from csv data given by web_scraping.py file by just dropping down product category and key ingredient columns from the total csv file. Its done so that the trained model could only see features and then predict category and key ingredient by itself.

For ingredient prediction, weighted precision is 0.8006891068115558, weighted recall is 0.8367346938775511 and weighted fscore is 0.8156537340210809. While for category prediction, weighted precision is 0.673469387755102, weighted recall is 0.6530612244897959, weighted fscore is 0.6288806431663574.

a) Input (product category and key ingredient columns dropped **scrapped_data.csv** file)<br>

B) Output (**output_data.csv**)

![bandicam 2021-12-26 01-06-22-299](https://user-images.githubusercontent.com/71775151/147392366-a950ae36-153e-4f33-8d5c-b16b1914d845.jpg)
