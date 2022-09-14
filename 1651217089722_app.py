import pandas as pd
import streamlit as st
import helper
import matplotlib.pyplot as plt

st.sidebar.title("Amazon Review Analysis!")

uploaded_file = st.sidebar.file_uploader("Choose a file")
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df)
    user_rating = df['Stars'].unique().tolist()

    user_rating.sort()
    #user_rating.insert(0, "overall")
    selected_review = st.sidebar.selectbox("Show Analysis wrt", user_rating)
    if st.sidebar.button("Show Analysis"):
        num_review, words = helper.fetch_stats(selected_review, df)
        col1, col2 = st.columns(2)
        with col1:
            st.header("Total Reviews")
            st.title(num_review)
        with col2:
            st.header("Total words")
            st.title(words)
    most_common_df = helper.most_common_words(selected_review, df)
    fig, ax = plt.subplots()
    ax.bar(most_common_df[0],most_common_df[1])
    plt.xticks(rotation='vertical')
    st.pyplot(fig)

    st.dataframe(most_common_df)

    emoji_df = helper.emoji_helper(selected_review, df)
    st.title("Emoji Analysis")
    fig, ax = plt.subplots()
    #ax.bar(emoji_df[0], emoji_df[1])
    plt.xticks(rotation='vertical')
    st.pyplot(fig)
    st.dataframe(emoji_df)
