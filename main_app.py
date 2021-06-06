import streamlit as st
import real_time_capture
import user_cust_pannel


class MultiApp:
    def __init__(self):
        self.apps = []

    def add_app(self, title, func):
        self.apps.append({
            "title": title,
            "function": func
        })

    def run(self):
        app = st.selectbox(
            'Navigation',
            self.apps,
            format_func=lambda app: app['title'])

        app['function']()


app = MultiApp()
st.markdown("""# Gesture Recognition System.
This is an Gesture Recognition which uses CNN 
to classify hand gesture to text with user customization""")

# Add all your application here
app.add_app("Gesture Reconizer", real_time_capture.app)
app.add_app("User Customization", user_cust_pannel.app)
# The main app
app.run()
