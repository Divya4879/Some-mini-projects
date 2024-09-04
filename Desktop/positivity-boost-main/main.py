from anthropic import Anthropic 
import streamlit as st
import anthropic
import os
from dotenv import load_dotenv

load_dotenv()


background_image = """
<style>
[data-testid="stAppViewContainer"] > .main {
    background-image: url("https://images.rawpixel.com/image_800/cHJpdmF0ZS9sci9pbWFnZXMvd2Vic2l0ZS8yMDIzLTAzL3JtNjA2ZGVzaWduLXJlbWl4LWJnLTEzLWIuanBn.jpg");
    background-size: 100vw 100vh;
    background-position: center;  
    background-repeat: no-repeat;
    opacity:0.9
}
</style>
"""

st.markdown(background_image, unsafe_allow_html=True)

# # Set your API key

client = Anthropic(
    # defaults to os.environ.get("ANTHROPIC_API_KEY")
    api_key=os.environ.get("ANTHROPIC_API_KEY"),
)


# # Create the API client
# client = anthropic.Client(api_key="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")

title = '<h1 style="font-family:serif;color:#9e0771; font-size: 54px">Your customized mood booster</h1>'
st.markdown(title, unsafe_allow_html=True)

subheading1 = '<h2 style="color:#be0a88; font-size: 40px;font-style:italic">Feeling down? Here\'s something to help you out 🫶🏻🥹❤️‍🩹</h1>'
st.markdown(subheading1, unsafe_allow_html=True)


n = f":blue[Enter your name]"
name = st.text_input(n,value=None,placeholder="Enter your name here...")

i = f":blue[Issue]"
issue = st.text_input(i,value=None,placeholder="Enter what's bothering you- eg. self-esteem, inferiority,....")

t = f":blue[Type of content:]"
type = st.selectbox(t,
                     ['Poem', 'Quote', 'Inspiring Story','Shaayari'])

i = f":blue[Identity]"
identity = st.text_input(i,value=None,placeholder="You're a student/developer/professional,....")


if st.button("Generate something good for me"):
    message = client.messages.create(
    model="claude-3-5-sonnet-20240620",
    max_tokens=800,
    temperature=0.05,
    system="""You are a motivational speaker, a leader and someone who's great with words. 
    You've been doing these and have been world-wide famous for these for more than 20 years.
    """,
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": f"Write a positive uplifting {type} in English for {name}, a {identity} suffering with {issue}."
                }
            ]
        }
        ])
    try:
        story = message.content[0].text
    
    
        st.text_area(label ="",value=story,height=320)

    except:
        st.text("The API is currently facing some issues. Please try later.")

    

footer="""<style>
a:link , a:visited{
color: red;
background-color: transparent;
text-decoration: underline;
}

a:hover,  a:active {
color: red;
background-color: transparent;
text-decoration: underline;
}

.footer {
position: fixed;
left: 0;
bottom: 0;
width: 100%;
background-color: white;
color: black;
text-align: center;
}
.footer{
    background-color:black
}
p{
    color: pink
}
</style>
<div class="footer">
<p>Built with ❤️ by <a href="https://x.com/Divya_devtics47" target="_blank">Divya</a></p>
</div>
"""
st.markdown(footer,unsafe_allow_html=True)

