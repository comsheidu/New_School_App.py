
if st.button("Check admission status"):
   


    if Jamb_scores > 250 and Waec_result == "Yes":
        st.write(f'Congratulations.\n You have been offered admission')
    elif Jamb_scores > 250 and Waec_result == "No":
        st.write(f'Congratulations.\n You have been offered admission')
    elif Jamb_scores != 250 and Waec_result == "Yes":
        st.write(f'Wait for the next admission list')
    elif Jamb_scores != 250 and Waec_result == "No":
        st.write(f'Not qualified to be admitted')
   
    else:
        st.write(f'Not qualified to be admitted')
        
