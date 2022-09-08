import streamlit as st
import pandas as pd
import plotly.express as px
house = pd.read_csv('House_Rent_Dataset.csv')
st.header('House Rent Prediction Analysis')
option = st.selectbox(
     'Which Analysis you want to see?',
     ('bar chart', 'histogram', 'pie chart '))

if option == 'bar chart':
     fig = px.bar(data_frame=house, x='City', y='Size', template='simple_white', color='BHK',
                  color_continuous_scale=px.colors.sequential.Burg, barmode='overlay')
     fig.update_layout(title={'text': ' Citywise BHK on basis of AreaSq'}, title_x=0.5,
                       title_font_family="Time New Roman", title_font_color="red")
     fig.update_layout(yaxis_title={'text': 'Sizstree', 'font': {'size': 15}},
                       xaxis_title={'text': 'City', 'font': {'size': 15}})
     fig.update_xaxes(title_font_color='red')
     fig.update_yaxes(title_font_color='red')
     fig.update_coloraxes(showscale=False)
     fig.update_xaxes(tickangle=45)
     st.plotly_chart(fig)
elif option == 'histogram':
      fig = px.histogram(house, x="Size", title='Size Distribution')
      st.plotly_chart(fig)
else:
     fig = px.pie(data_frame=house, names='Bathroom',
                  color_discrete_sequence=px.colors.sequential.deep)
     fig.update_layout(
          title={'text': 'Pie Chart for different number of Bathrooms present in Houses available for Rent'},
          title_x=0.5, title_font_family="Time New Roman", title_font_color=" blue")
     fig.update_traces(textfont_size=15)
     st.plotly_chart(fig)
