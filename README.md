# uber-eats-app

## **Description**
This repository contains Python-based APIs for the following features:

### **Features**
1. **Restaurant Search and Filter**:
   - Filter restaurants by location and cuisine.
   - Browse a list of restaurants.

2. **Menu Management**:
   - View the menu of a specific restaurant.

3. **Order Checkout**:
   - Place an order with item price, tax calculation, and final amount.

4. **Payment**:
   - Simulated payment endpoint requiring card details.

---

## **API Endpoints**

### **Restaurant Endpoints**
| Method | Endpoint                                             | Description                      |
|--------|------------------------------------------------------|----------------------------------|
| `GET`  | `/api/restaurants/filter?location=<location>&cuisine=<cuisine>` | Search and filter restaurants.   |
| `GET`  | `/api/restaurants`                                   | Fetch a list of all restaurants. |

### **Menu Endpoints**
| Method | Endpoint       | Description                      |
|--------|----------------|----------------------------------|
| `GET`  | `/api/menu/<id>` | Fetch the menu of a restaurant. |

### **Order Endpoints**
| Method | Endpoint             | Description                       |
|--------|----------------------|-----------------------------------|
| `POST` | `/api/order/checkout`| Checkout for an order.           |

### **Payment Endpoints**
| Method | Endpoint       | Description                       |
|--------|----------------|-----------------------------------|
| `POST` | `/api/payment` | Process payment for an order.    |

---

## **Testing with Postman**

You can test the endpoints using Postman. Below are example requests:

### **1. Filter Restaurants**
```plaintext
GET http://127.0.0.1:5000/api/restaurants/filter?location=new%20york&cuisine=italian
