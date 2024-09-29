# Author: VS
# Script_name: dict_data_processor.py
# Description: This script processes a list of dictionaries representing sales data and aggregates total sales per product, handling duplicate product IDs and sorting the output by total sales in descending order.

#!/usr/bin/env python3
# Sample sales data
sales_data = [
    {"product_id": 1, "product_name": "Amway", "quantity_sold": 160, "price_per_unit": 285.50},
    {"product_id": 2, "product_name": "Hair_dryer", "quantity_sold": 57, "price_per_unit": 175.00},
    {"product_id": 3, "product_name": "gaming_Mouse", "quantity_sold": 125, "price_per_unit": 562.50},
    {"product_id": 4, "product_name": "Xbox_PS5", "quantity_sold": 13, "price_per_unit": 89347.50},
    {"product_id": 5, "product_name": "Portable_AC", "quantity_sold": 2, "price_per_unit": 56715.00},
    {"product_id": 6, "product_name": "Iphone_15max", "quantity_sold": 12, "price_per_unit": 89620.00},
    {"product_id": 7, "product_name": "Boat_ANC_Earpods", "quantity_sold": 32, "price_per_unit": 155.00},
    {"product_id": 8, "product_name": "Portable_fan", "quantity_sold": 122, "price_per_unit": 12265.00},
    {"product_id": 9, "product_name": "office_desk", "quantity_sold": 45, "price_per_unit": 3095.00},
    {"product_id": 10, "product_name": "Mt_15", "quantity_sold": 223, "price_per_unit": 126185.00}
]

# Function to process sales data
def process_sales_data(data):
    # Initialize a dictionary to hold aggregated sales data
    aggregated_sales = {}

    # Loop through each sale record in the input data
    for record in data:
        product_id = record["product_id"]
        product_name = record["product_name"]
        quantity_sold = record["quantity_sold"]
        price_per_unit = record["price_per_unit"]
        total_revenue = quantity_sold * price_per_unit

        # Check if the product is already in the aggregated sales dictionary
        if product_id in aggregated_sales:
            # Update existing product data
            aggregated_sales[product_id]["quantity_sold"] += quantity_sold
            aggregated_sales[product_id]["total_revenue"] += total_revenue
        else:
            # Add new product data
            aggregated_sales[product_id] = {
                "product_name": product_name,
                "quantity_sold": quantity_sold,
                "total_revenue": total_revenue
            }

    # Convert the aggregated sales dictionary to a list of tuples for sorting
    sorted_sales = sorted(aggregated_sales.items(), key=lambda item: item[1]["total_revenue"], reverse=True) #false means items are sorted in ascending order

    # Print the aggregated and sorted sales data
    print("Total Sales per Product:")
    for product_id, sales_info in sorted_sales:
        print(f"Product ID: {product_id}, Product Name: {sales_info['product_name']}, Quantity Sold: {sales_info['quantity_sold']}, Total Revenue: ${sales_info['total_revenue']:.2f}")

# Main program execution
if __name__ == "__main__":
    process_sales_data(sales_data)