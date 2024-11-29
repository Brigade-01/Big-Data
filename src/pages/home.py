from st_pages import show_pages_from_config, add_page_title
import streamlit as st
import pandas as pd
import time
# Either this or add_indentation() MUST be called on each page in your
# app to add indendation in the sidebar
add_page_title()
show_pages_from_config()

#Loading data from the CSV or Excel file
def load_data(file_path):
    data = pd.read_csv(file_path)  
    data = pd.read_excel(file_path)
    return data

def main():
    st.session_state.data = None
    #Home Tab
    st.title("Αρχική Σελίδα")
    st.write("Καλώς ορίσατε στην Εφαρμογή Μηχανικής Μάθησης & 2D Visualization της ομάδας Brigade-01. Προσθέστε ένα αρχείο CSV ή Excel παρακάτω για να ξεκινήσετε την επεξεργασία του μέσω της εφαρμογής μας.")
    st.markdown("""---""")

    # File uploading module
    uploaded_file = st.file_uploader("Φόρτωση αρχείου CSV ή Excel", type=["csv", "xlsx"])
    # Μέγιστο επιτρεπτό μέγεθος αρχείου (σε bytes, 500 MB)
    max_file_size = 500 * 1024 * 1024  # 500 MB in bytes
    if uploaded_file is not None:
        if uploaded_file.size > max_file_size:
            st.error("Το αρχείο υπερβαίνει το μέγιστο επιτρεπτό μέγεθος των 500 MB.")
            return
        if uploaded_file.name.endswith('.csv'):
            data = pd.read_csv(uploaded_file)
        elif uploaded_file.name.endswith('.xlsx'):
            data = pd.read_excel(uploaded_file)
        else:
            st.error("Τύπος αρχείου μη υποστηριζόμενος.")
            return
        
        # Check if the uploaded file contains letters
        if data.select_dtypes(include=['object']).empty:
            success_message = st.success("Τα δεδομένα φορτώθηκαν με επιτυχία!")
            
            
        else:
            st.error("Το αρχείο δεδομένων περιέχει γράμματα. Φορτώστε ένα αρχείο που περιέχει μόνο αριθμητικές τιμές.")
            st.markdown("""---""")
            
        st.markdown("""---""")
    # Check for labels in the data and set session state
        if 'label' in data.columns:
            st.warning("Το αρχείο περιέχει ετικέτες. Μπορείτε να εκτελέσετε τις Προσομοίωσεις clustering και classification.")
            st.session_state.has_labels = True
        else:
            st.session_state.has_labels = False
            st.warning("Το αρχείο δεν περιέχει ετικέτες. Δεν θα εκτελεστεί η διαδικασία ομαδοποίησης (clustering).")
        # Saving uploaded data for usage on the rest of the tabs
        st.session_state.data = data
if __name__ == "__main__":
    main()
