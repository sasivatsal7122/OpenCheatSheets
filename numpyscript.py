import streamlit as st
import pandas as pd
import numpy as np

# Initial page config

st.set_page_config(
     page_title='Numpy cheat sheet',
     layout="wide",
     initial_sidebar_state="expanded",
)

# Thanks to streamlitopedia for the following code snippet

# def img_to_bytes(img_path):
#     img_bytes = Path(img_path).read_bytes()
#     encoded = base64.b64encode(img_bytes).decode()
#     return encoded


#     # sidebar

# def cs_sidebar():

#     st.sidebar.markdown('''[<img src='data:image/png;base64,{}' class='img-fluid' width=32 height=32>](https://streamlit.io/)'''.format(img_to_bytes("logomark_website.png")), unsafe_allow_html=True)
#     st.sidebar.header('Numpy cheat sheet')



#     return None
## Main body

def cs_body():
    # Import/Export

    col1, col2, col3 = st.columns(3)

    col1.subheader('Importing/Exploring')
    col1.code('''
     np.loadtxt('file.txt')
     #From a text file
     np.genfromtxt('fille.csv',delimiter=',') 
     # from a CSV file
     np.savetxt('file.txt',arr,delimiter=' ') 
     # Writes to a text
     np.savetxt('file.csv',arr,delimiter=',') 
     # Write to CSV file
    ''')
    #Creating arrays
    col1.subheader('Creating Array')
    col1.code('''
     np.array([1,2,3])
     # One dimention Array
     np.array([(1,2,3),(4,5,6)])
     # Two Dimentttion Array
     np.zeros(3)
     # 1D array with lenght 3.All values 0
     np.ones((3,4))
     # 3x4 array with all values 1.
     np.eye(5)
     # 5x5 array of 0 with 1 on diagonal(identity matrix)
     np.linespace(0,100,6)
     # Arrray of 6 evenly divided values from 0 to 100
     np.arrange(0,10,3)
     # Array of values from 0 to less than 10 with step 3
     #Eg:- [0,3,6,9]
     np.full((2,3),8)
     # 2x3 array  with all values 8
     np.random.rand(4,5)
     # 4x5 Array of random floats between 0-1
     np.random.rand(6,7)*100
     # 6x7 Array of random floats between 0-100
     np.random.randint(5,size=(2,3))
     # 2x3 array with random ints between 0-4
     ''')

    col1.subheader('Inspecting Properties')
    col1.code('''
     arr.size
     # Returns number of elements in arr
     arr.shape
     # Returns dimensions of arr(Rows,Columns)
     arr.dtype 
     # Returns type f elements in  the arr
     arr.astype(dtype)
     # Convert arr element to type dtype
     arr.tolist()
     # Convert arr to a python list
     np.info(np.eye)
     # View documentation for np.eye
     ''')

    col1.subheader('Copying/Sorting/Reshaping')
    col1.code('''
    np.copy(arr)
    # Copies arr to new memory
    arr.view(dtype)
    # Creates view of arr elements with type dtype
    arr.sort()
    # Sort arr
    arr.sort(axis=0)
    # Sorts specific axis of arr
    two_d_arr.flatten()
    # Flatten 2D array two_d_arr to 1D
    arr.T
    # Transposes arr(Rows become Columns and Vise Versa)
    arr.reshape(3,4)
    # Reshapes arr to 3 roe=ws and 4 columns without changing the data
    arr.resize((5,6))
    #Changes arr shape to 5x6 and fills new values with 0
    ''')

    






def main():
    # cs_sidebar()
    cs_body()


    return None