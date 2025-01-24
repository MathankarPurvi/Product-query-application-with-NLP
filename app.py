from phi.agent import Agent
from phi.storage.agent.sqlite import SqlAgentStorage
import sqlite3
import streamlit as st

# Create a storage backend using the SQLite database
storage = SqlAgentStorage(
    table_name="agent_sessions",  # Stores session logs in this table
    db_file="tmp/data.db",        # Path to the SQLite database file
)

# Initialize the agent
agent = Agent(
    storage=storage,
    description="Agent for querying the products database."
)

# Streamlit UI
st.title("AI-Powered SQLite Query Application")
st.subheader("Ask questions about the products database!")

# User Input
query = st.text_input("Enter your query (e.g., 'Show all electronics under $1000'):").strip()

if st.button("Search"):
    if query:
        try:
            # Connect to the SQLite database
            conn = sqlite3.connect("tmp/data.db")
            cursor = conn.cursor()

            # Initialize conditions
            conditions = []

            # Check for categories
            possible_categories = [
                "Electronics", "Clothing", "Appliances", "Footwear",
                "Accessories", "Furniture", "Sports", "Kitchenware", "Home Decor"
            ]
            for category in possible_categories:
                if category.lower() in query.lower():
                    conditions.append(f"category = '{category}'")

            # Check for price conditions
            if "under" in query.lower() and "$" in query:
                try:
                    price_limit = float(query.split("under $")[-1].strip())
                    conditions.append(f"price < {price_limit}")
                except ValueError:
                    st.warning("Invalid price value detected.")
            elif "above" in query.lower() and "$" in query:
                try:
                    price_limit = float(query.split("above $")[-1].strip())
                    conditions.append(f"price > {price_limit}")
                except ValueError:
                    st.warning("Invalid price value detected.")

            # Check for colors
            possible_colors = [
                "Black", "Silver", "Blue", "Red", "White", "Gray",
                "Yellow", "Green", "Brown", "Purple", "Navy Blue",
                "Orange", "Transparent", "Gold"
            ]
            for color in possible_colors:
                if color.lower() in query.lower():
                    conditions.append(f"color = '{color}'")

            # Build SQL query
            sql_query = "SELECT * FROM products"
            if conditions:
                sql_query += " WHERE " + " AND ".join(conditions)

            # Execute query
            cursor.execute(sql_query)
            rows = cursor.fetchall()

            # Display results
            if rows:
                st.write("**Results:**")
                st.table(rows)
            else:
                st.write("No results found.")

            # Close the database connection
            conn.close()
        except Exception as e:
            st.error(f"Error: {str(e)}")
    else:
        st.warning("Please enter a query!")
