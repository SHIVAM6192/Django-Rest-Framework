# Django REST Framework – API Implementations 🚀

This repository contains **multiple Django REST Framework (DRF) API implementations**, showcasing different ways to build RESTful APIs using Django.

The goal of this project is to **understand, compare, and practice** various DRF approaches, starting from basic function-based views to advanced viewsets.

---

## 📌 What This Project Covers

This project demonstrates the following API implementation styles:

- Function-Based Views (FBV)
- Class-Based Views (CBV)
- Generic Views
- Mixins
- ViewSets
- ModelViewSets

Each approach is implemented with simple examples to clearly understand their usage, advantages, and differences.

---

## 🧩 API Implementation Types

### 1️⃣ Function-Based Views (FBV)
- Uses standard Python functions
- Simple and easy to understand
- Best for small and straightforward APIs
- Requires manual handling of HTTP methods

📌 Example use case: Small projects or learning basics of DRF.

---

### 2️⃣ Class-Based Views (CBV)
- Uses Python classes instead of functions
- Better code organization
- Supports reusable logic
- Handles HTTP methods using class methods (`get`, `post`, etc.)

📌 Example use case: Medium-sized APIs with better structure.

---

### 3️⃣ Generic Views
- Built-in DRF generic classes
- Reduces boilerplate code
- Provides common CRUD operations
- Easily customizable

📌 Example use case: Standard CRUD APIs with minimal custom logic.

---

### 4️⃣ Mixins
- Adds reusable behavior to generic views
- Allows combining different CRUD operations
- Provides flexibility and cleaner code

📌 Example use case: When you want partial CRUD functionality.

---

### 5️⃣ ViewSets
- Groups related views into a single class
- Automatically maps HTTP methods to actions
- Works seamlessly with DRF routers

📌 Example use case: Clean and scalable API design.

---

### 6️⃣ ModelViewSet
- Most powerful and concise approach
- Provides full CRUD operations by default
- Minimal code with maximum functionality

📌 Example use case: Production-ready REST APIs.

---

## 🛠️ Tech Stack Used

- Python
- Django
- Django REST Framework
- SQLite (for development)
- Git & GitHub

---

## 📂 Project Structure (Simplified)

