
# Bag of Bugs
e-commerce application to manage the stock of the shop that is selling bugs. 

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



instead of getting code from random it would be good to generate qr code for each stock item. 
https://emmanuelkwakyenyantakyi.medium.com/qr-code-generator-api-with-django-369cae1d556f

DRF tutorials:
Very Academy: Django + React, Restful API Course, Building a restful API

https://youtu.be/soxd_xdHR0o

Dennis Ivy DRF + React

https://youtu.be/c0x_AaPjNCY