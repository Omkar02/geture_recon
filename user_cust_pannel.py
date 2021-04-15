import streamlit as st
import json
import time
from PIL import Image


def app():
    def edit_messaged():
        with open('messages/symbol_to_text.json') as f:
            data = json.load(f)
        usr_int = usr_customization(data)
        if usr_int:
            key, val = usr_int
            if key not in data:
                st.error("Wrong gesture symbol selected!")
            else:
                data[key] = val
                with open('messages/symbol_to_text.json', 'w') as json_file:
                    json.dump(data, json_file)
                st.success("Message updated successfully!")

    def usr_customization(data_dict):
        gesture_code = st.text_input("Gesture Code:")
        if gesture_code:
            if gesture_code in data_dict:
                st.markdown(f'> :sparkle: Gesture with code **{gesture_code}**  is mapped to  **{data_dict[gesture_code]}**')
            else:
                st.markdown(f'> :no_entry: 404! No gesture code found.')
        gesture_meaning = st.text_input("Gesture Meaning:")

        if gesture_code and gesture_meaning:
            submit = st.button('Apply')
            if submit:
                return(gesture_code, gesture_meaning)

    def initilize():
        alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G',
                    'H', 'I', 'K', 'L', 'M', 'N', 'O',
                    'P', 'Q', 'R', 'S', 'T', 'U', 'V',
                    'W', 'X', 'Y']
        data = {}
        for idx, alp in enumerate(alphabet):
            data[idx] = alp

        with open('messages/symbol_to_text.json', 'w') as json_file:
            json.dump(data, json_file)

            # print(usr_customization())
            # time.sleep(5)
            # st.error("Wrong gesture symbol selected!")

    st.title("User Customization Menu")
    image = Image.open('Datasets/amer_sign2.png')
    st.image(image)

    reset = st.button('Reset')

    if reset:
        initilize()
        st.success("Message restored successfully!")

    edit_messaged()
