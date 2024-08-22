# Northwind Example

This example demonstrates how to use the **Natural Lens** tool with the Northwind PostgreSQL database. Follow the instructions below to set up the database using Docker and run the necessary commands.

## Setting Up the Database with Docker

To use this example, you can set up the Northwind PostgreSQL database using Docker Compose. Follow these steps:

1. Clone the Northwind PostgreSQL repository:

   ```bash
   git clone https://github.com/pthom/northwind_psql.git
   cd northwind_psql
   ```

2. Start the Docker containers:
   ```bash
   docker-compose up -d
   ```

## Running Natural Lens Commands

Once the database is up and running, you can execute the following commands to download the schema, generate profiles, and query the database:

1. **Download the Database Schema**

   ```bash
   nlens download --dbname northwind --user postgres --password postgres --host localhost --port 55432
   ```

   _Expected Output:_

   ```
   Schema fetched successfully! Sample data saved to `data/`.
   ```

2. **Generate Database Profiles**

   ```bash
   nlens profile
   ```

   _Expected Output:_

   ```
   Profiles generated successfully! Profile saved to `profiles/`.
   ```

3. **Query the Database**
   ```bash
   nlens query --query "What kind of SQL queries can you suggest me?"
   ```

## Query Output

Based on the diverse tables and profiles you've provided, there are several SQL query suggestions that can help you extract useful insights from the data. Here's a variety of SQL queries categorized by type of analysis:

### 1. **Data Retrieval Queries**

- **Retrieve Customer Information**

```sql
SELECT customer_id, company_name, contact_name, city, country
FROM customers
WHERE country = 'Germany';
```

- **Retrieve Products Under a Specific Category**

```sql
SELECT product_name, unit_price, units_in_stock
FROM products
WHERE category_id = 1; -- Example: Beverages
```

### 2. **Aggregative Queries**

- **Count of Customers by Country**

```sql
SELECT country, COUNT(customer_id) AS customer_count
FROM customers
GROUP BY country;
```

- **Average Freight Costs by Shipping Method**

```sql
SELECT ship_via, AVG(freight) AS average_freight
FROM orders
GROUP BY ship_via;
```

### 3. **Join Queries**

- **Orders with Customer and Shipping Information**

```sql
SELECT o.order_id, c.contact_name, o.ship_city, o.freight
FROM orders o
JOIN customers c ON o.customer_id = c.customer_id;
```

- **Products and Their Suppliers**

```sql
SELECT p.product_name, s.company_name
FROM products p
JOIN suppliers s ON p.supplier_id = s.supplier_id;
```

### 4. **Filtering Queries**

- **Products That Are Discontinued**

```sql
SELECT product_name, unit_price
FROM products
WHERE discontinued = 1; -- Indicates discontinued products
```

- **Employees Hired After a Certain Date**

```sql
SELECT first_name, last_name, hire_date
FROM employees
WHERE hire_date > '2020-01-01';
```

### 5. **Subqueries**

- **Get Customers with Orders**

```sql
SELECT customer_id, company_name
FROM customers
WHERE customer_id IN (SELECT DISTINCT customer_id FROM orders);
```

- **Find Products with Low Stock**

```sql
SELECT product_name
FROM products
WHERE units_in_stock < (SELECT AVG(units_in_stock) FROM products);
```

### 6. **Update & Modification Queries**

- **Update Customer Phone Number**

```sql
UPDATE customers
SET phone = '0345-555-1234'
WHERE customer_id = 'ALFKI';
```

- **Mark Product as Discontinued**

```sql
UPDATE products
SET discontinued = 1
WHERE product_name = 'Chai';
```

### 7. **Performance Analysis Queries**

- **Products by Sales Volume**
  (Assuming you have sales data interconnected with the product table)

```sql
SELECT p.product_name, SUM(od.quantity) AS total_sold
FROM products p
JOIN order_details od ON p.product_id = od.product_id
GROUP BY p.product_name
ORDER BY total_sold DESC;
```

- **Employee Performance by Territory**
  (If you link employee territories with sales/order data)

```sql
SELECT e.first_name, e.last_name, t.territory_description, COUNT(o.order_id) AS total_orders
FROM employees e
JOIN employee_territories et ON e.employee_id = et.employee_id
JOIN territories t ON et.territory_id = t.territory_id
JOIN orders o ON e.employee_id = o.employee_id
GROUP BY e.first_name, e.last_name, t.territory_description;
```

### 8. **Delete Queries**

- **Remove a Discontinued Product**

```sql
DELETE FROM products
WHERE discontinued = 1 AND product_id = 15; -- Example product ID
```

### 9. **Complex Queries with Case Statements**

- **Categorize Customers by Region**

```sql
SELECT customer_id, company_name,
       CASE
         WHEN country IN ('USA', 'Canada') THEN 'North America'
         WHEN country IN ('Germany', 'UK', 'France') THEN 'Europe'
         ELSE 'Other'
       END AS region_category
FROM customers;
```

### 10. **Create Views for Common Queries**

- **Create a View for Easy Access to Customer Orders**

```sql
CREATE VIEW customer_orders AS
SELECT c.customer_id, c.company_name, o.order_id, o.order_date
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id;
```

These SQL queries cover a wide range of functionalities, from retrieving and aggregating data to updating and deleting entries, which can be highly useful depending on your analysis goals and business requirements. Remember to adapt the queries according to your actual database structure and requirements.
