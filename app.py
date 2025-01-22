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

            # Define custom logic for query execution
            if "electronics" in query.lower():
                sql_query = "SELECT * FROM products WHERE category = 'Electronics'"
            elif "under $1000" in query.lower():
                sql_query = "SELECT * FROM products WHERE price < 1000"
            else:
                sql_query = "SELECT * FROM products"

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
