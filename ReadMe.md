# Data Base for FastAPI

**Data Base for FastAPI** is a module for **FastAPI** designed to simplify working with PostgreSQL databases. It includes ready-to-use CRUD modules for database interactions.

## Project Features

Database interactions are performed asynchronously. The pre-built models include the following relationships:

1. **products - attachments**: One-to-Many relationship.
2. **orders - users**: One-to-Many relationship.
3. **orders - products**: Many-to-Many relationship through the `order_product_association` table.

---

## Installation

This project requires **Python 3.12**.

### Dependencies

To work with this module, install the following dependencies:

1. **FastAPI[all]**
2. **psycopg** (for asynchronous PostgreSQL support)
3. **SQLAlchemy**
4. **Alembic**
5. **pytest**

### Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/raykes11/Data_Base_for_FastAPI.git
   ```

2. Navigate to the project directory:
   ```bash
   cd Data_Base_for_FastAPI
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

Feel free to explore and contribute! 🎉

