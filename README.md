# Shopify-Challenge-DevOps-F2022

Fall 2022 - Shopify

Developer Intern Challenge

My web app runs using Python3's [Django](https://www.djangoproject.com/) and [Django REST Framework](https://www.django-rest-framework.org/) libraries. To run the code, do the following:
1. Set up a Python3 environment using the included [`requirements.txt`](./requirements.txt) file.
2. open the [`inventory`](./inventory) directory.
3. Run `python3 manage.py runserver`.
* Note that this defaults to running an IPv4 local server on port 8000. A full server setup with load balancing and reverse proxying and so on is not the focus of this project, so it is not included.

For the additional feature, I chose to implement warehouses. 
There is a seperate endpoint for CRUD operations on warehouses, and warehouses have a one-to-many relationship with items. (that is, one warehouse can have manyy items, or many items can be at one warehouse.) 
Since items may not be at a warehouse (ex. if they're in transit or processing), Items may have *no* warehouse, represented as a `null` in the `location` field of the item.

Replit located [here](https://replit.com/@magiclight731/Shopify-Challenge-DevOps-F2022).
