import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title('Streamlit 超入門')
# st.write('DataFrame')
# st.write('Display Image')

# st.write('Interactive Wiggets')
st.write('プログレスバーの表示')
'Start!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration{i+1}')
    bar.progress(i + 1)
    time.sleep(0.1)

left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラム')

expander1 = st.expander('問い合わせ')
expander1.write('問い合わせ内容1の回答')
expander2 = st.expander('問い合わせ')
expander2.write('問い合わせ内容2の回答')
expander3 = st.expander('問い合わせ')
expander3.write('問い合わせ内容3の回答')

# text = st.text_input('あなたの趣味を教えてください')
# condision = st.slider('あなたの今の調子は？', 100, 50)

# 'あなたの趣味は：', text
# 'コンディション', condision



# option = st.selectbox(
#     'あなたが好きな数字を教えてください',
#     list(range(1, 10))
# )

# 'あなたが好きな数字は、', option, 'です。'

# if st.checkbox('Show Image'):
#     img = Image.open('sample.jpg')
#     st.image(img, caption='higashi', use_column_width=True)


# df = pd.DataFrame(
#     np.ramdom.rand(100,2)/[50, 50] + [35.69, 139.70],
#     column=['lat', 'lon']
# )

# st.table(df.style.highlight_max(axis=0))
# st.map(df)