import streamlit as st
import pandas as pd
import numpy as np


## Main body

def cs_body():
    # Import/Export
    df=pd.DataFrame({
        "a" : [4,5,6],
        "b": [7,8,9],
        "c": [10,11,12]},
        index=[1,2,3])
    df1=pd.DataFrame({
        "a" : [4,5,6],
        "b": [7,8,9],
        "c": [10,11,12]},
        index=pd.MultiIndex.from_tuples(
            [('d',1),('d',2),('e',2)],names=['n','v']
            ))
    col1, col2, col3 = st.columns(3)
    st.text('')
    col1.subheader('Creating DataFrames')
    col1.code('''
# Spesify values for each column
>>> df1=pd.DataFrame({
        "a" : [4,5,6],
        "b": [7,8,9],
        "c": [10,11,12]},
        index=pd.MultiIndex.from_tuples(
            [('d',1),('d',2),('e',2)],names=['n','v']
            ))


    ''')

    col1.code('''
# Spesify values for each column
>>> df=pd.DataFrame({
"a" : [4,5,6],
"b": [7,8,9],
"c": [10,11,12]},
index=[1,2,3])

# Specify values for each row
>>> df1=pd.DataFrame([
    [4,7,10],
    [5,8,11],
    [6,9,12]],
index=[1,2,3],
columns=['a','b','c'])


    ''')
    col1.text('Output : ')
    
    
    col1.dataframe(df)
    col1.dataframe(df1)

    col1.subheader('Method Chaining')
    df = (pd.melt(df)
        .rename(columns={
        'variable':'var',
        'value':'val'})
        .query('val >= 200')
        )

    col1.code('''
 #Most pandas methods return a DataFrame so that
 #another pandas method can be applied to the result.
 #This improves readability of code.
 df = (pd.melt(df)
 .rename(columns={
 'variable':'var',
 'value':'val'})
 .query('val >= 200')
 )
    ''')
    col1.text('Output : ')    
    col1.dataframe(df)

    col2.subheader('Reshaping Data')
    col2.text('- Change layout, sorting, reindexing, renaming')
    df=pd.DataFrame({
        "a" : [4,5,6],
        "b": [7,8,9],
        "c": [10,11,12]},
        index=[1,2,3])
    
    

    col2.code('''
 pd.melt(df)
 #Gather columns into rows.
 df.pivot(columns='var', values='val')
 # Spread rows into columns.
 pd.concat([df1,df2])
 #Append rows of DataFrames
 pd.concat([df1,df2], axis=1)
 #Append columns of DataFrames
 df.sort_values('mpg')
 #Order rows by values of a column (low to high).
 df.sort_values('mpg', ascending=False)
 #Order rows by values of a column (high to low).
 df.rename(columns = {'y':'year'})
 #Rename the columns of a DataFrame
 df.sort_index()
 #Sort the index of a DataFrame
 df.reset_index()
 #Reset index of DataFrame to row numbers, moving
 #index to columns.
 df.drop(columns=['Length', 'Height'])
 #Drop columns from DataFrame
    ''')
    
    col2.subheader('Subset Observations')
    col2.text('-Rows')
    col2.code('''
 df[df.Length > 7]
 #Extract rows that meet logical criteria.
 df.drop_duplicates()
 #Remove duplicate rows (only considers columns).
 df.sample(frac=0.5)
 #Randomly select fraction of rows.
 df.sample(n=10)
 #Randomly select n rows.
 df.nlargest(n, 'value')
 #Select and order top n entries.
 df.nsmallest(n, 'value')
 #Select and order bottom n entries.
 df.head(n)
 #Select first n rows.
 df.tail(n)
 #Select last n rows.
    ''')
    col2.subheader('Subset Variables')
    col2.text('-Columns')
    col2.code('''
 df[['width', 'length', 'species']]
 #Select multiple columns with specific names.
 df['width'] or df.width
 #Select single column with specific name.
 df.filter(regex='regex')
 #Select columns whose name matches regular expression regex.
    ''')
    col2.subheader('Using Query')
    col2.code('''
 #query() allows Boolean 
 #expressions for filtering rows.
 df.query('Length > 7')
 df.query('Length > 7 and Width < 8')
 df.query('Name.str.startswith("abc")',engine="python")
    ''')








def main():
    st.title("Pandas Cheat sheet : ")
    st.header('')
    cs_body()