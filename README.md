# 🛍️ ProductStore

A simple Django product management system.

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
- **Admin Panel**: Full Django admin integration
- **PostgreSQL Database**: Robust database backend
- **Template Inheritance**: Clean, maintainable code structure
- **Named URLs**: SEO-friendly and maintainable URL patterns