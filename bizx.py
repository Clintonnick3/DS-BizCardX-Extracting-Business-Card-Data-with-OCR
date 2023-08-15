
import streamlit as st
from PIL import Image
import easyocr
import sqlite3
import cv2
import numpy as np 
import pandas as pd


# Connect to sqlite3 database
conn = sqlite3.connect('Bzcard.db')
c = conn.cursor()


# Create a table to store the business card information
c.execute('''CREATE TABLE IF NOT EXISTS Business_card 
              (id INT AUTO_INCREMENT PRIMARY KEY,
              name TEXT,
              position TEXT,
              address TEXT,
              pincode VARCHAR(25),
              phone VARCHAR(25),
              email TEXT,
              website TEXT,
              company TEXT
              )''')

# Using easyOCR for reading data
reader = easyocr.Reader(['en'])


# Set the title and page icon
st.set_page_config(page_title="BIZCARD-X", page_icon=":credit_card:")


# Title 
st.title(":blue[OCR] :orange[Tool For Extracting Card Data]:credit_card:")


# Create a file uploader
file_upload = st.file_uploader(":green[UPLOAD YOUR IMAGE TO EXTRACT DATA]", type=["jpg", "jpeg", "png"])


# Create a sidebar menu with options to Add, Show, Update business card information
st.sidebar.title(":blue[BIZCARD-]:red[X]  (OCR)")
pict = Image.open('biz.jpg')
st.sidebar.image(pict, width=250)


m = ['Insert Data', 'Show Data', 'Edit Card Info']
choose = st.sidebar.selectbox("Select An Option", m)


if choose == 'Insert Data':
    if file_upload is not None:
        
        # Read the image using OpenCV
        image = cv2.imdecode(np.fromstring(file_upload.read(), np.uint8), 1)
        
        # Display the uploaded image
        st.image(image, caption='Uploaded Successfully', use_column_width=True)
        
        # Button to extract information from the image
        if st.button('Extract Data'):
            bsc = reader.readtext(image, detail=0)

            #Extracted ocr data
            name = bsc[0]
            position = bsc[1]
            address = bsc[2]
            pincode = bsc[3]
            phone = bsc[4]
            email = bsc[5]
            website = bsc[6]
            company = bsc[7]

            
            # Insert the extracted information and image into the database
            sql_data = "INSERT INTO Business_card (name, position, address, pincode, phone, email, website, company) VALUES ( ?, ?, ?, ?, ?, ?, ?, ?)"
            values = (name, position, address, pincode, phone, email, website, company)
            c.execute(sql_data, values)
            conn.commit()
            
            # Display message
            st.success("Card Data Captured")

elif choose == 'Show Data':
    
    # Display the stored business card information
    c.execute("SELECT rowid, * FROM Business_card")
    result = c.fetchall()

    # Form the formatted result data
    formatted_result = []
    for row in result:
        rowid = row[0]
        rest_of_row = row[1:]  # Extract the rest of the row values
        formatted_result.append((rowid,) + rest_of_row)

    # Specify the column names
    columns = ['rowid', 'id', 'name', 'position', 'address', 'pincode', 'phone', 'email', 'website', 'company']

    # Create a DataFrame from the formatted result data
    df = pd.DataFrame(formatted_result, columns=columns)

    # Display the DataFrame with delete buttons
    for index, row in df.iterrows():
        st.write(row)
        delete_button = st.button(f"Delete {row['name']}'s card", key=f"delete_button_{row['rowid']}")
        if delete_button:
            c.execute("DELETE FROM Business_card WHERE rowid=?", (row['rowid'],))
            conn.commit()
            st.success(f"Deleted {row['name']}'s card")
            df = df[df['rowid'] != row['rowid']]
    conn.close()

elif choose == 'Edit Card Info':
    
    # Create a dropdown menu to select a business card to edit
    c.execute("SELECT id, name FROM Business_card")
    result = c.fetchall()
    business_cards = {}
    
    for row in result:
        business_cards[row[1]] = row[0]
    select_card_name = st.selectbox("Select Card To Edit", list(business_cards.keys()))
    
    # Get the current information for the selected business card
    c.execute("SELECT * FROM Business_card WHERE name=?", (select_card_name,))
    result = c.fetchone()

    # Get edited information 
    name = st.text_input("Name", result[1])
    position = st.text_input("Position", result[2])
    address = st.text_input("Address", result[7])
    pincode = st.text_input("Pincode", result[4])
    phone = st.text_input("Phone", result[3])
    email = st.text_input("Email", result[6])
    website = st.text_input("Website", result[5])
    company = st.text_input("Company_Name", result[8])

    
    # Create a button to update the business card
    if st.button("Edit Card Data"):
        
        # Update the information for the selected business card in the database
        c.execute("UPDATE Business_card SET name=?, position=?, address=?, pincode=?, phone=?, email=?, website=?, company=? WHERE name=?", 
                             (name, position, address, pincode, phone, email, website, company, select_card_name))
        conn.commit()
        st.success("Card Data Updated")
