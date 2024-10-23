
# Final Project
## Restaurant Administration Program
### General Description:

In this coding exercise, you are tasked with developing a restaurant administration program that will help streamline various aspects of restaurant management. The program is designed to be used by restaurant owners, managers, and staff to handle day-to-day operations and ensure smooth functioning of the establishment.

The restaurant administration program will be built as a console application and will provide a user-friendly interface for easy navigation and interaction. It will offer a range of features to facilitate efficient management and organization of the restaurant's operations, including:

1. **Menu Management**: The program will allow users to create, edit, and manage the restaurant's menu. They can add or remove dishes, set prices, and categories. The menu can be categorized into different sections such as appetizers, main courses, desserts, etc.

2. **Order Processing**: Users will be able to receive and process customer orders through the program. Orders can be taken manually or integrated with a POS (Point of Sale) system. The program will generate order tickets, track their status (e.g., pending, in progress, delivered), and calculate the total bill for each order.

3. **Table Management**: The program will assist in managing the restaurant's seating arrangement. Users can create and assign tables to customers, track table availability, and monitor occupied tables.

4. **Reporting and Analytics**: The program will generate various reports and analytics to provide insights into the restaurant's performance. This includes sales reports, revenue analysis, popular menu items, and other key metrics. These reports will help in making informed decisions and optimizing the restaurant's operations.

Overall, the restaurant administration program aims to streamline and automate various tasks involved in managing a restaurant. It will enhance operational efficiency, improve customer service, and provide valuable insights for decision-making. The coding exercise will involve designing and implementing the necessary data structures, user interface components, and logic to achieve these functionalities.

---

### Requirements:

The development of the restaurant administration program will require the implementation of various programming concepts to ensure its functionality and effectiveness. The following concepts will play a crucial role in achieving the desired program requirements:

- Conditionals
- Lists
- Dictionaries
- Loops
- Error handling
- Functions
- Text Files
- Modules

---

### Program Structure:

The structure of the restaurant administration program will consist of several files, each serving a specific purpose to organize and manage the codebase effectively. Below is a description of the typical files in the program:

1. **Main Program File**: This is the main entry point of the program, often named something like `main.py` or `restaurant_administration.py`. It initializes the program, sets up any necessary configurations, and orchestrates the execution of other modules and files.

2. **Menu File**: This file, such as `menu.py`, contains code related to menu management. It defines functions to create, modify, and retrieve menu items. It may include lists or dictionaries to store menu information, such as dish names, prices, and dietary details.

3. **Order Processing File**: The order processing file, such as `order_manager.py`, handles the processing of customer orders. It contains functions responsible for creating order tickets, managing order status, calculating bill totals, and updating inventory levels accordingly.

4. **Table Management File**: The table management file, such as `table_management.py`, deals with managing the seating arrangements in the restaurant. It may define functions to create and assign tables to customers, track table availability, handle seat availability, and estimate food preparation times.

5. **Reporting and Analytics Files**: These files, such as `reporting.py`, are responsible for generating various reports and analytics to provide insights into the restaurant's performance. They may contain functions to calculate sales reports, revenue analysis, popular menu items, and other key metrics.

6. **Text Files**: These files, such as `menu.txt`, `table_management.txt`, or `configuration.txt`, store data persistently in a readable text format. They are used to save and retrieve information required for the program's functioning.

---

### Functions and Operations:

Here is a list of the functions and their operations for each file in the restaurant administration program:

#### 1. Menu:
- `create_menu_item`: Creates a new menu item with specified details.
- `edit_menu_item`: Modifies the details of an existing menu item.
- `delete_menu_item`: Removes a menu item from the menu.
- `get_menu_item`: Retrieves the details of a specific menu item.
- `get_menu_items`: Returns a list of all menu items.
- `get_menu_section`: Retrieves all menu items within a specific menu section.
- `search_menu_item`: Searches for menu items based on a keyword or criteria.
- `save_menu`: Saves the menu to a `.txt` file.

#### 2. Order Processing:
- `create_order_ticket`: Generates a new order ticket for a customer's order.
- `update_order_status`: Updates the status of an order ticket (e.g., pending, in progress, delivered).
- `calculate_bill_total`: Calculates the total bill amount for an order and payment.
- `update_inventory`: Adjusts the inventory levels based on the ingredients used in an order.

#### 3. Table Management:
- `show_seats`: Shows the available seats for a specific table.
- `assign_table`: Assigns a customer to an available table.
- `get_table_status`: Retrieves the current status (occupied or available) of a table.
- `get_occupied_tables`: Returns a list of all currently occupied tables.
- `estimate_food_time`: Estimates the time duration of a customer's food preparation.

#### 4. Reporting and Analytics:
- `generate_sales_report`: Calculates and generates a report on sales for a specific time period.
- `perform_revenue_analysis`: Analyzes revenue data for the orders.
- `get_popular_menu_items`: Identifies the most popular menu items based on customer orders.

---

### Files Content:

#### 1. Configuration File:
This file will contain the requisite configurations for the program's overall behavior. The file must be read at the start of the program's execution and used to set the global parameters:

- Tax percent: 16%
- Reporting name format: `yyyy/mm/dd-{report_name}.txt`
- Meal times:
  - Breakfast: 8 AM - 1 PM
  - Lunch: 1 PM - 7 PM
  - Dinner: 7 PM - 11 PM
- Restaurant name
- Opening time: 8:00 AM
- Closing time: 11:00 PM
- Menu file path: `menu.txt`
- Order tickets file path: `order_tickets.txt`
- Table file path: `tables.txt`
- Sales report file path: `sales_report.txt`
- Revenue analysis file path: `revenue_analysis.txt`
- Popular analysis file path: `popular_items.txt`

#### 2. Menu Items File:
This file will contain all the dishes, with the values separated by pipes and in the following structure:

- **Category**: Sections such as “Appetizers”, “Main Courses”, or “Desserts”.
- **Dish name**: Name of the dish.
- **Dish description**: A brief description of the dish.
- **Dish price**: Price of the dish.
- **Dish cost**: Cost to the restaurant to make the dish.
- **Time preparation**: Time required to prepare the dish, in minutes.
- **Menu type**: “Breakfast”, “Lunch” or “Dinner”.

Example:

```
Appetizers|Bruschetta|Tomato and basil on toasted bread|8.99|5.99|20|Dinner
```

#### 3. Tables File:
This file will contain the initial table status, with the values separated by pipes and in the following structure:

- Table number
- Capacity (total number of seats)
- Status: “Available” or “Occupied”.

Example:

```
1|4|Available
2|6|Occupied
3|2|Available
```

---

### Output Example:

```
Welcome to PizzaHub Administration Program!

1. Menu Management
2. Order Processing
3. Table Management
4. Reporting and Analytics
5. Exit

Please enter your choice: 1

Menu Management Options:
1. Add New Menu Item
2. Edit Menu Item
3. Delete Menu Item
4. View Menu
5. Search Menu Item
6. Go back

Please enter your choice: 4

Menu:
1. Appetizers:
   - Bruschetta - Tomato and basil on toasted bread - $8.99
   - Spinach and Artichoke Dip - Creamy spinach and artichoke dip served with tortilla chips - $10.99

2. Main Courses:
   - Grilled Salmon - Grilled salmon fillet with lemon butter sauce, served with roasted vegetables - $18.99
   - Spaghetti Bolognese - Classic spaghetti with meat sauce and Parmesan cheese - $14.99
   - Margherita Pizza - Fresh mozzarella, tomatoes, and basil on thin crust - $12.99

3. Desserts:
   - Chocolate Lava Cake - Warm chocolate cake with a gooey chocolate center, served with vanilla ice cream - $7.99
   - New York Cheesecake - Creamy cheesecake with a graham cracker crust, topped with strawberry sauce - $9.99

Please enter your choice: 6

Thank you for using PizzaHub Administration Program! Have a great day!
```