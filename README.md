# 🛍️ ProductStore

1. **Product app**
   - Created `products` app

   - Built `Product` model with fields:
     name, description, price, stock, image

   - Set up CRUD using generic views:
     ListView, DetailView, CreateView, UpdateView, DeleteView
   
   - Added product URLs to `urls.py`:
     /products/, /products/<id>/, /create/, /update/, /delete/


2. **Category app**
   - Created `categories` app

   - Built `Category` model with:
     name, description, image

   - Added category to Product:
     category = ForeignKey(Category, on_delete=CASCADE)

   - Updated product forms with category field

   - Set up category views with generics:
     CategoryListView, CategoryDetailView, CategoryCreateView...

   - Connected URLs:
     /categories/, /categories/<id>/, /create/...


3. **Finally**
   - Added user authentication
   - Styled with Tailwind CSS
   - Protected category operations

## 📍 Endpoints

### Products
- `GET /products/` - List all products
- `GET /products/<id>/` - View product details
- `GET /products/create/` - Show product creation form
- `POST /products/create/` - Create new product
- `GET /products/<id>/delete/` - Delete a product

### Categories
- `GET /categories/` - List all categories
- `GET /categories/<id>/` - View category details
- `GET /categories/create/` - Show category creation form
- `POST /categories/create/` - Create new category
- `GET /categories/<id>/delete/` - Delete a category



## � Screenshots

### Login
![Login](images/1.png)

### Register
![Register](images/2.png)

### Products page
![Products page](images/3.png)

### Categories page
![Categories page](images/4.png)

### Category creation
![Category creation](images/5.png)

### Category page after adding
![Category page after adding](images/6.png)

### Adding product
![Adding product](images/7.png)

### After creation
![After creation](images/8.png)

### Viewing details and edit or delete
![Viewing details and edit or delete](images/9.png)

### Delete alert
![Delete alert](images/10.png)

### Viewing products in specefic category
![Viewing products in specefic category](images/11.png)

