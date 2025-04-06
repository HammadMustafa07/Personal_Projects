# # import the streamlit library
# import streamlit as st
 
# # give a title to our app
# st.title('Welcome to BMI Calculator')
 
# # TAKE WEIGHT INPUT in kgs
# weight = st.number_input("Enter your weight (in kgs)")
 
# # TAKE HEIGHT INPUT
# # radio button to choose height format
# status = st.radio('Select your height format: ',
#                   ('cms', 'meters', 'feet'))
 
# # compare status value
# if(status == 'cms'):
#     # take height input in centimeters
#     height = st.number_input('Centimeters')
 
#     try:
#         bmi = weight / ((height/100)**2)    
#     except:
#         st.text("Enter some value of height")
 
# elif(status == 'meters'):
#     # take height input in meters
#     height = st.number_input('Meters')
 
#     try:
#         bmi = weight / (height ** 2)
#     except:
#         st.text("Enter some value of height")
 
# else:
#     # take height input in feet
#     height = st.number_input('Feet')
 
#     # 1 meter = 3.28
#     try:
#         bmi = weight / (((height/3.28))**2)
#     except:
#         st.text("Enter some value of height")
 
# # check if the button is pressed or not
# if(st.button('Calculate BMI')):
 
#     # print the BMI INDEX
#     st.text("Your BMI Index is {}.".format(bmi))
 
#     # give the interpretation of BMI index
#     if(bmi < 16):
#         st.error("You are Extremely Underweight")
#     elif(bmi >= 16 and bmi < 18.5):
#         st.warning("You are Underweight")
#     elif(bmi >= 18.5 and bmi < 25):
#         st.success("Healthy")
#     elif(bmi >= 25 and bmi < 30):
#         st.warning("Overweight")
#     elif(bmi >= 30):
#         st.error("Extremely Overweight")

# # import the streamlit library
# import streamlit as st
 
# # give a title to our app
# st.title('🏋️‍♂️ Welcome to the BMI Calculator! 🍏')

# # give a description to the app
# st.markdown("Find out your Body Mass Index (BMI) by entering your weight and height. It's simple and easy! 😄")

# # TAKE WEIGHT INPUT in kgs
# weight = st.number_input("Enter your weight (in kilograms) 👇", min_value=1.0, max_value=500.0, step=0.1)

# # TAKE HEIGHT INPUT
# # radio button to choose height format
# status = st.radio('Select your height format: 📏',
#                   ('cms', 'meters', 'feet'))

# # compare status value
# if(status == 'cms'):
#     # take height input in centimeters
#     height = st.number_input('Enter your height in centimeters (cm) 📏', min_value=1.0, max_value=300.0, step=0.1)
 
#     try:
#         bmi = weight / ((height/100)**2)    
#     except:
#         st.text("Please enter a valid height value. ❌")
 
# elif(status == 'meters'):
#     # take height input in meters
#     height = st.number_input('Enter your height in meters (m) 📏', min_value=0.1, max_value=3.0, step=0.01)
 
#     try:
#         bmi = weight / (height ** 2)
#     except:
#         st.text("Please enter a valid height value. ❌")
 
# else:
#     # take height input in feet
#     height = st.number_input('Enter your height in feet (ft) 📏', min_value=1.0, max_value=10.0, step=0.1)
 
#     # 1 meter = 3.28
#     try:
#         bmi = weight / (((height/3.28))**2)
#     except:
#         st.text("Please enter a valid height value. ❌")
 
# # check if the button is pressed or not
# if(st.button('Calculate BMI 📊')):
 
#     # print the BMI INDEX
#     st.text(f"Your BMI Index is: **{bmi:.2f}** 🧑‍⚕️")
 
#     # give the interpretation of BMI index
#     if(bmi < 16):
#         st.error("🚨 You are Extremely Underweight")
#     elif(bmi >= 16 and bmi < 18.5):
#         st.warning("⚠️ You are Underweight")
#     elif(bmi >= 18.5 and bmi < 25):
#         st.success("✅ You have a Healthy BMI")
#     elif(bmi >= 25 and bmi < 30):
#         st.warning("⚠️ You are Overweight")
#     elif(bmi >= 30):
#         st.error("🚨 You are Extremely Overweight")


# import the streamlit library
import streamlit as st
 
# give a title to our app
st.title('📏 BMI Calculator ')
# 🧑‍⚕️

# give a description to the app
st.markdown("Welcome to the BMI Calculator. Please enter your weight and height to calculate your Body Mass Index (BMI). This tool helps you understand your health status based on your BMI value. 💪")

# TAKE WEIGHT INPUT in kgs
weight = st.number_input("Enter your weight (in kilograms) ⚖️", min_value=1.0, max_value=500.0, step=0.1)

# TAKE HEIGHT INPUT
# radio button to choose height format
status = st.radio('Select your height format: 📏',
                  ('cms', 'meters', 'feet'))

# compare status value
if(status == 'cms'):
    # take height input in centimeters
    height = st.number_input('Enter your height in centimeters (cm) 📐', min_value=1.0, max_value=300.0, step=0.1)
 
    try:
        bmi = weight / ((height/100)**2)    
    except:
        st.text("Please enter a valid height value. ❌")
 
elif(status == 'meters'):
    # take height input in meters
    height = st.number_input('Enter your height in meters (m) 📐', min_value=0.1, max_value=3.0, step=0.01)
 
    try:
        bmi = weight / (height ** 2)
    except:
        st.text("Please enter a valid height value. ❌")
 
else:
    # take height input in feet
    height = st.number_input('Enter your height in feet (ft) 📐', min_value=1.0, max_value=10.0, step=0.1)
 
    # 1 meter = 3.28
    try:
        bmi = weight / (((height/3.28))**2)
    except:
        st.text("Please enter a valid height value. ❌")
 
# check if the button is pressed or not
if(st.button('Calculate BMI 📊')):
 
    # print the BMI INDEX
    st.text(f"Your BMI Index is: **{bmi:.2f}**")

    # give the interpretation of BMI index
    if(bmi < 16):
        st.error("You are Extremely Underweight 🚨")
    elif(bmi >= 16 and bmi < 18.5):
        st.warning("You are Underweight ⚠️")
    elif(bmi >= 18.5 and bmi < 25):
        st.success("You have a Healthy BMI ✅")
    elif(bmi >= 25 and bmi < 30):
        st.warning("You are Overweight ⚠️")
    elif(bmi >= 30):
        st.error("You are Extremely Overweight 🚨")
