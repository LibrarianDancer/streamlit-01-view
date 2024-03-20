import streamlit as st #별명 붙이기
view = [100, 150, 30]
st.write('# Youtube Views')
st.write('## raw')
st.write('### bar chart')
view
st.bar_chart(view)

import pandas as pd
sView = pd.Series(view)
sView