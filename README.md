
# Bag of Bugs
e-commerce application to manage the stock of the shop that is selling bugs. 


## Database Design

Database was design to handle the stock levels of the products. 

The products for this e-commerce store are bugs. Model representing products is Species. User can make a decision which species he would like to buy. The [dbdiagram.io](https://dbdiagram.io/d/63d732e7296d97641d7ce68b) service was used to design the database

![database](docs/db_schema.png)

## List available products:

The list of all available products is effectively the list of all bugs. From models perspecitve this is a list of all Species. These are the items available for the user to purchase.

http://127.0.0.1:8000/species/


## View stock levels for each product

Url pointing to slug of a particular species gives the details of this species and the stock level using foreign key reverse lookup

http://127.0.0.1:8000/species/onufry/


## Incrementing stock levels
Stock items can be added in the stock endpoint.

http://127.0.0.1:8000/stock/

## Decrementing stock levels

if the stock has been sold / lost / destroyed, it should not be deleted from the database, it should be marked as in_stock = False and manual stock update should be added 

### Decrementing stock levels with manual stock update
Decrementing stock value can happen if the stock runs away or dies. The Manual Stock Upade model handles such event. User can input manual stock update and add stock affected to many to many field

the reason for manual stock update - model has option loss or gain.

The signal from many to many field on ManualStockUpdate model updates stock item objects in stock field to true or false - depending on loss or gain.

http://127.0.0.1:8000/stock/stock_update/


### Decrementing stock levels with customer orders
Creating orders happens in two steps. First user needs to create order with his address

http://127.0.0.1:8000/orders/

than take the order refference number and go to this order's url to add order items into this order

http://127.0.0.1:8000/orders/86610F6843874357B44F91F8A9A4CD39/

### Handling stock levels for customer orders

Order item serializer checks which species are available and displays only available species in the dropdown options
http://127.0.0.1:8000/orders/86610F6843874357B44F91F8A9A4CD39/

As a next step - if customer chose quantity above current stock level of this species, the error is displayed to say that there isn't enough stock.

### Further development

need to add signals from order to mark stock as in_stock = False
need to add suppliers and handle stock intake - to create invoices and stock items. 

instead of getting code from random it would be good to generate qr code for each stock item. 
https://emmanuelkwakyenyantakyi.medium.com/qr-code-generator-api-with-django-369cae1d556f


## DRF tutorials:
Very Academy: Django + React, Restful API Course, Building a restful API

https://youtu.be/soxd_xdHR0o

Dennis Ivy DRF + React

https://youtu.be/c0x_AaPjNCY