# GameMaxStore
***GameMaxStore*** is an online shop that includes products, categories of products, search by names products, cart, and also history of orders. Every authorized user can order items that are available. If the user has done an order, an email will be send with details about the order as well as the user can check details about the previous orders in the tab 'My Orders'.

# Details of the project: 
The project was written in the Python used Django framework, in project as well are used:
- Heroku as a cloud for all project 
- Amazon S3 as a cloud for saving static files
- PostgresSQL as a database
- Google API Place Autocomplete service for simplification of inputting destination delivery
- ZoHo mail for sending emails specifying our domain
- Celery for the asynchronization of some process
- and many others...

# 📸 Screenshots :
User is not authorized |  User is authorized
:-------------------------:|:-------------------------:
![home_log_in](https://user-images.githubusercontent.com/79806840/178934430-4fb60bbb-9fbf-4d27-bbb1-d73b77b460c0.png)  |![auth_home](https://user-images.githubusercontent.com/79806840/178935566-73a900b7-5296-4316-966c-a854fc370d83.png)
Login page | Registration page
|
![log_in](https://user-images.githubusercontent.com/79806840/178937188-8d328a13-5a40-41cb-ae7a-787734deba5d.png)|![registration](https://user-images.githubusercontent.com/79806840/178937228-f554826a-acf2-459a-8f1d-2383f63a74bb.png) 
Home page | Cart page
:-------------------------:|:-------------------------:
![auth_home_below](https://user-images.githubusercontent.com/79806840/178937699-5f9bedd1-b88e-4164-ac32-a09ac6e197b9.png)|![cart](https://user-images.githubusercontent.com/79806840/178937823-0921087d-6d39-49cb-8d2a-e08d34a283bd.png)
Order confirmation page | Order confirmation page
:-------------------------:|:-------------------------:
![ordre_confirm_with_google_api](https://user-images.githubusercontent.com/79806840/178938266-ca721a69-0911-4717-8dfe-876359559042.png) |![sign_order](https://user-images.githubusercontent.com/79806840/178938409-4feb9971-9099-4824-80bb-d77e8be43693.png)
Email confirmation | My orders page
:-------------------------:|:-------------------------:
![email](https://user-images.githubusercontent.com/79806840/178938762-688883b5-6b05-4311-85bc-727006869b0d.png) | ![my_orders](https://user-images.githubusercontent.com/79806840/178938901-97fe5cf3-6c86-4a57-b1bb-0d84cb52b215.png)
