# DS-BizCardX-Extracting-Business-Card-Data-with-OCR

Welcome to the BizCard Project!

We are here to introduce you to an innovative solution that will transform the way you manage your contact information. Our project is centered around simplifying the process of storing and accessing business cards by creating a digital database.

Gone are the days of manually entering contact details from visiting cards. With our cutting-edge technology, all you need to do is scan the card using our integrated scanner, and voila! A soft copy of the card is created and securely stored in our database.

Imagine the convenience of having all your contacts readily available at your fingertips. No more digging through stacks of business cards or struggling to remember where you put that important contact. Our system ensures that your contacts are organized and easily searchable, saving you time and effort.

Not only does our BizCard Project offer a streamlined approach to managing contacts, but it also provides a cost-effective solution. Eliminating the need for physical storage and reducing the risk of losing important cards, our digital database ensures that your valuable connections are preserved for the long term.

We understand the importance of building and nurturing relationships in the business world. That's why our project empowers you to strengthen your network efficiently. With quick access to contact information, you can reach out to potential clients, collaborators, or partners effortlessly, helping you seize every opportunity that comes your way.

Join us on this journey of revolutionizing contact management. Say goodbye to cluttered desks and hello to a digital future. Explore our BizCard Project and discover the ease and efficiency of keeping your contacts in a secure, accessible, and organized format.

Start scanning, start connecting, and start building lasting relationships with the BizCard Project.

# WorkFlow

* Installing the required packages.
* Using Streamlit creating made UI with header, subheader, tabs, writebox, forms etc.
* Establishing DataBase connection through sqlalchemy-engine and engine.connecter.execute(text()) were used to write queries.
* Made upload button where only img file are allowded to select.
* streamlite loads img file to object so it is made again as file for further cv2 reading.
* Easy-ocr execution is made and raw text is extracted from image.
* using regex deeply i've made out every pattern for identification.
* company,name,designation,mobile,email,website,area,city,state,pincode all are extreacted individually using re, loops and conditions.
* finally extracted data is displaced using a form where user is allowed to edit the extracted details.
* submit button in form is uded to asign edited data to their varialble names and each column is assigned for each variable in the table
* additionally card image as object is uploaded to DB with the other details.
