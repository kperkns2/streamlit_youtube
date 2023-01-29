# https://share.streamlit.io/kperkns2/streamlit_youtube/main/app.py

# Create a streamlit dashboard which shows displays youtube videos (thumbnail, title, number of views)

# pd.columns = ['videoId', 'numberOfLikes', 'numberOfDislikes', 'numberOfComments',
#       'videoDuration', 'videoCategory', 'videoTags', 'title', 'channel_title',
#       'description', 'publishTime', 'channel_id', 'url', 'thumbnails']

# import pandas as pd
# import streamlit as st
# # import altair as alt
# import numpy as np
# # import pydeck as pdk
# # import plotly.express as px
# # import plotly.graph_objects as go
# # import matplotlib.pyplot as plt


# @st.cache
# def load_data():
#      return pd.read_csv('traeger.csv')


# df = load_data()

# # Show a thumbnail, title and number of views together
# st.write('hi')
# st.write(df)
# def show_thumbnail_title_views(df):
#     st.write(
#         f'<div style="background-color:tomato;"><p style="color:white;font-size:50px;">{df.iloc[0]["title"]}</p></div>', unsafe_allow_html=True)
#     st.image(df.iloc[0]['thumbnails'], use_column_width=True)
#     st.write(f'<p style="font-size:20px;">{df.iloc[0]["numberOfViews"]} views</p>', unsafe_allow_html=True)


# show_thumbnail_title_views(df)


import streamlit as st
html_string = """<html><head>
    <style type="text/css">
.comment-container {
width: 100%;
}
.comment {
display: flex;
flex-direction: column;
align-items: flex-start;
margin-bottom: 40px;
}
.user-info {
display: flex;
align-items: center;
}
.user-photo {
width: 50px;
height: 50px;
border-radius: 25px;
margin-top: 25px;
}
.user-name {
margin-left: 10px;
font-weight: bold;
}
.comment-text {
margin-top: -15px;
margin-left: 60px;
width: 90%;
line-height: 1.1;
}
.reply-text {
margin-top: -15px;
margin-left: 60px;
width: 90%;
line-height: 1.1;
background-color:#eeee66;
}
.replies {
margin-top: 5px;
margin-left: 60px;
}
.reply-count {
color: blue;
font-size: 12px;
font-family: Sans-Serif;
}
.reply {
margin-left: 20px;
}
    </style>
</head><body><div class="comment-container">
    <div class="comment">
      <div class="user-info">
        <img src="https://yt3.ggpht.com/ytc/AL5GRJWc4wmOgspGcC4HONjKrW-S6LoXznbp1r_VShMX15g=s48-c-k-c0x00ffffff-no-rj" class="user-photo">
        <span class="user-name">Suzanne Wong</span>
      </div>
      <p class="comment-text">Pewds should definitely link up with Magnus Midtbø and do a bouldering video together. Would make for a very wholesome vid</p>
      <div class="replies">
        <span class="reply-count">▲ 1 Replies</span>
        <div class="reply">
          <div class="user-info">
            <img src="https://yt3.ggpht.com/5oUY3tashyxfqsjO5SGhjT4dus8FkN9CsAHwXWISFrdPYii1FudD4ICtLfuCw6-THJsJbgoY=s88-c-k-c0x00ffffff-no-rj" class="user-photo">
            <span class="user-name">PewDiePie</span>
          </div>
          <p class="reply-text">Yo, that's a solid idea! Magnus is a boss at bouldering and I'm always down for a new adventure. Let's make it happen 💪🏼🧗‍♂️</p>
        </div>
      </div>
    </div>
  </div><div class="comment-container">
    <div class="comment">
      <div class="user-info">
        <img src="https://yt3.ggpht.com/5nYeyko89Ul7E-bRnyzRmE6BAkMh3rpF75jGzMCyEUvRRorJGSGSgGEfruD9qJ7j5eHaub67YXI=s48-c-k-c0x00ffffff-no-rj" class="user-photo">
        <span class="user-name">Organicfruit</span>
      </div>
      <p class="comment-text">Mr Beast is a superman on a whole other level<br>I bet what will happen next is ending world hunger or World Peace!</p>
      <div class="replies">
        <span class="reply-count">▲ 1 Replies</span>
        <div class="reply">
          <div class="user-info">
            <img src="https://yt3.ggpht.com/ytc/AL5GRJV-BviaWnNvLLWoK18JTaIs6IC6adCul_JzqgQtkA=s88-c-k-c0x00ffffff-no-rj" class="user-photo">
            <span class="user-name">MrBeast</span>
          </div>
          <p class="reply-text">Ha, well I wish it was that easy! But unfortunately ending world hunger and achieving world peace is a bit out of my league. But I'll do my best to keep doing good and making a positive impact in the world through my videos and charity work. Maybe one day I'll unlock the secret to world peace, but for now, let's just stick to giving away money and having fun on YouTube!</p>
        </div>
      </div>
    </div>
  </div><div class="comment-container">
    <div class="comment">
      <div class="user-info">
        <img src="https://yt3.ggpht.com/ytc/AL5GRJXLcT--hymYrm3Z4FGMWizoYj5zMNurcaVLpg=s48-c-k-c0x00ffffff-no-rj" class="user-photo">
        <span class="user-name">Amy Farmer</span>
      </div>
      <p class="comment-text">you guys should do a trick shot wife additon video</p>
      <div class="replies">
        <span class="reply-count">▲ 1 Replies</span>
        <div class="reply">
          <div class="user-info">
            <img src="https://yt3.ggpht.com/ytc/AL5GRJVCLqs9ZCFaMcyRKYrm1dRwfbWkvERIpjejcILRng=s88-c-k-c0x00ffffff-no-rj" class="user-photo">
            <span class="user-name">Dude Perfect</span>
          </div>
          <p class="reply-text">Haha, we like the way you think! A trick shot wife addition video sounds like a blast. We'll have to see if our significant others are up for the challenge. Maybe we'll even have a Dude Perfect vs. Wives showdown! Stay tuned, folks.</p>
        </div>
      </div>
    </div>
  </div><div class="comment-container">
    <div class="comment">
      <div class="user-info">
        <img src="https://yt3.ggpht.com/ytc/AL5GRJXerqqVrex-fi7UoQhQmj1Py6jxQBFN2apm0z41_Q=s48-c-k-c0x00ffffff-no-rj" class="user-photo">
        <span class="user-name">Sanchit Agrawal</span>
      </div>
      <p class="comment-text">This is the best song ever written.</p>
      <div class="replies">
        <span class="reply-count">▲ 1 Replies</span>
        <div class="reply">
          <div class="user-info">
            <img src="https://yt3.ggpht.com/vSiSGj-VIayjhlqNZ3569zON3AWIfhHCLYkGwQVfCXt8cFZoRYZJqfsuuzDXezpRUyxtbSPR=s88-c-k-c0x00ffffff-no-nd-rj" class="user-photo">
            <span class="user-name">Ed Sheeran</span>
          </div>
          <p class="reply-text">Wow, thank you so much for the kind words! ❤️ It means a lot to me that you enjoy my music. I put a lot of heart and soul into every song I write, so it's great to hear that it's resonating with you. Keep on listening and singing along! 🎤🎵</p>
        </div>
      </div>
    </div>
  </div><div class="comment-container">
    <div class="comment">
      <div class="user-info">
        <img src="https://yt3.ggpht.com/ytc/AL5GRJWsbZGx7GaBthsZ7dTB40HlNJ3YuVK-L8NU8PCgfw=s48-c-k-c0x00ffffff-no-rj" class="user-photo">
        <span class="user-name">Anabelle Reynolds</span>
      </div>
      <p class="comment-text">Taylor swift can never write a terrible song even if she tried, this proves it!!!!</p>
      <div class="replies">
        <span class="reply-count">▲ 1 Replies</span>
        <div class="reply">
          <div class="user-info">
            <img src="https://yt3.ggpht.com/8IG_vczSZLUYnDvfHFusOMdIFRpPP8xoKX6z2BLoyALI2hep-PrlLjKEp8qnrnOjTDbAF2w4kQ=s88-c-k-c0x00ffffff-no-nd-rj" class="user-photo">
            <span class="user-name">Taylor Swift</span>
          </div>
          <p class="reply-text">Aww, thank you so much! 🥰 I really appreciate your kind words. Writing music is my passion and it means the world to me when fans connect with my songs. Keep spreading the love and let's keep creating magic together! 🎶🎵 #Taylorswift #music #fans</p>
        </div>
      </div>
    </div>
  </div><div class="comment-container">
    <div class="comment">
      <div class="user-info">
        <img src="https://yt3.ggpht.com/ytc/AL5GRJWK_xte4ortheRx26l6TEOZnGQLsVjAa70HS-dR8w=s48-c-k-c0x00ffffff-no-rj" class="user-photo">
        <span class="user-name">Sophia Freitas</span>
      </div>
      <p class="comment-text">Please Leave a bowl of walnuts every single day just for the squirrels</p>
      <div class="replies">
        <span class="reply-count">▲ 1 Replies</span>
        <div class="reply">
          <div class="user-info">
            <img src="https://yt3.ggpht.com/ytc/AL5GRJV8nNBYEmOJznUS8Lz6bZfOlZU4G6rM1zNbZyK2=s88-c-k-c0x00ffffff-no-rj" class="user-photo">
            <span class="user-name">Mark Rober</span>
          </div>
          <p class="reply-text">Haha, I love the idea of leaving a bowl of walnuts for the squirrels! 🐿️ As a scientist, I always like to think about the impact of our actions on the environment. So, I might conduct a little experiment and see how the squirrels react to the daily bowl of walnuts. 🔬 Will they come to rely on it? Will it disrupt their natural foraging habits? These are the questions we need to consider before making any decisions. But, I'll definitely keep you updated on the results! 🐿️🧪</p>
        </div>
      </div>
    </div>
  </div><div class="comment-container">
    <div class="comment">
      <div class="user-info">
        <img src="https://yt3.ggpht.com/ytc/AL5GRJUjhj7rcIiHlOVhqx6hrufrLuUvbtfK4ogrk4PoTA=s48-c-k-c0x00ffffff-no-rj" class="user-photo">
        <span class="user-name">Tana Maina</span>
      </div>
      <p class="comment-text">Raise your hand if you like sssniperwolf</p>
      <div class="replies">
        <span class="reply-count">▲ 1 Replies</span>
        <div class="reply">
          <div class="user-info">
            <img src="https://yt3.ggpht.com/ytc/AL5GRJWE52NGXoc_5xSmyR_xwHDUzVt8hezqFumC-WpBBw=s88-c-k-c0x00ffffff-no-rj" class="user-photo">
            <span class="user-name">SSSniperWolf</span>
          </div>
          <p class="reply-text">🙋‍♀️ Both of my hands are up! Thank you so much for your support, it means the world to me! ❤️🎮</p>
        </div>
      </div>
    </div>
  </div><div class="comment-container">
    <div class="comment">
      <div class="user-info">
        <img src="https://yt3.ggpht.com/b-XT4UgryGzYcT9TP6oxGoXuNDYWz8SUOtKFct0mCIB5irWhXK_ML6kbHM91nd8a0ApeMn2i=s48-c-k-c0x00ffffff-no-rj" class="user-photo">
        <span class="user-name">Abhi and Niyu</span>
      </div>
      <p class="comment-text">Can someone explain the act.</p>
      <div class="replies">
        <span class="reply-count">▲ 1 Replies</span>
        <div class="reply">
          <div class="user-info">
            <img src="https://yt3.ggpht.com/kMDc8fyf3CWH_QnICe0TRVMzVfbwTm7L8ylqUwU-w5W14TckEcxFPHOAuvMNBQnVKTIJCyy4=s88-c-k-c0x00ffffff-no-rj" class="user-photo">
            <span class="user-name">America's Got </span>
          </div>
          <p class="reply-text">The act you're referring to is a unique and talented performance by one of our contestants. We can't give away too many details, but we can assure you that it is a combination of skill, creativity, and entertainment that will leave you amazed and entertained. Be sure to tune in to our next episode to see it for yourself!</p>
        </div>
      </div>
    </div>
  </div><div class="comment-container">
    <div class="comment">
      <div class="user-info">
        <img src="https://yt3.ggpht.com/ytc/AL5GRJU0NVnkhofw-nvpEs0bSqDb8F-p15eDvIeQ9Q=s48-c-k-c0x00ffffff-no-rj" class="user-photo">
        <span class="user-name">Josh Ralph</span>
      </div>
      <p class="comment-text">Not particularly healthy. Notice the amount of sugar in the nutirion info for these, remembering that 4 grams of sugar = 1 teaspoon, and 3 teaspoons of anything = 1 tablespoon.</p>
      <div class="replies">
        <span class="reply-count">▲ 1 Replies</span>
        <div class="reply">
          <div class="user-info">
            <img src="https://yt3.ggpht.com/sx2UTbpCoLz6v3SwIs_dKSRclgfP3V4KcPNEGjXgijfF18lx-UG8xW_9kOoi-Fzntcw_OGtjng=s88-c-k-c0x00ffffff-no-rj" class="user-photo">
            <span class="user-name">Tasty</span>
          </div>
          <p class="reply-text">🍩 We know our recipes aren't exactly #healthgoals, but they sure are delicious! 🤤 And let's be real, a little sugar never hurt anyone. Just don't eat the whole batch in one sitting! 😅</p>
        </div>
      </div>
    </div>
  </div><div class="comment-container">
    <div class="comment">
      <div class="user-info">
        <img src="https://yt3.ggpht.com/ytc/AL5GRJUnZypIGam6KPYDXvDmtfM7fqETydk9V5wvTA=s48-c-k-c0x00ffffff-no-rj" class="user-photo">
        <span class="user-name">EJVaz</span>
      </div>
      <p class="comment-text">Mousaka more like Mou-sucks😅</p>
      <div class="replies">
        <span class="reply-count">▲ 1 Replies</span>
        <div class="reply">
          <div class="user-info">
            <img src="https://yt3.ggpht.com/bFpwiiOB_NLCVsIcVQ9UcwBjb1RzipnMmtNfLSWpeIaHboyGkBCq4KBitmovRbStk9WvIWIZOyo=s88-c-k-c0x00ffffff-no-rj" class="user-photo">
            <span class="user-name">Gordon Ramsay</span>
          </div>
          <p class="reply-text">Looks like you haven't tried my version of mousaka. Give it a taste and let me know if it still 'mou-sucks'.</p>
        </div>
      </div>
    </div>
  </div><div class="comment-container">
    <div class="comment">
      <div class="user-info">
        <img src="https://yt3.ggpht.com/ytc/AL5GRJXIPiOFR9SKR2IQuxaJRWVb2RBTuUbtLtiWtKyRIg=s48-c-k-c0x00ffffff-no-rj" class="user-photo">
        <span class="user-name">Sgt Meatball</span>
      </div>
      <p class="comment-text">Jimmy congratulations, you look more handsome than when you started this show, the facial hair really suits you</p>
      <div class="replies">
        <span class="reply-count">▲ 1 Replies</span>
        <div class="reply">
          <div class="user-info">
            <img src="https://yt3.ggpht.com/ytc/AL5GRJXxFVlr4sqedKckwfGOr5la8qPo5gkVYylw8xagYa4=s88-c-k-c0x00ffffff-no-rj" class="user-photo">
            <span class="user-name">Jimmy Kimmel Live</span>
          </div>
          <p class="reply-text">Thanks for the compliment, but let's be real here - it's not the facial hair making me more handsome, it's the lighting and camera angles. #HollywoodMagic</p>
        </div>
      </div>
    </div>
  </div><div class="comment-container">
    <div class="comment">
      <div class="user-info">
        <img src="https://yt3.ggpht.com/ytc/AL5GRJWcr5kCf7xzVm7kEuUcKFBJSOOcMCFhYOP5IIUV=s48-c-k-c0x00ffffff-no-rj" class="user-photo">
        <span class="user-name">Gabriel Whelan is cool</span>
      </div>
      <p class="comment-text">This video has convinced me that philosophers are really dumb people but brilliant orators.</p>
      <div class="replies">
        <span class="reply-count">▲ 1 Replies</span>
        <div class="reply">
          <div class="user-info">
            <img src="https://yt3.ggpht.com/ytc/AL5GRJWvTe2XC80z6_cZh5GZoYhRWaONosagXi6OnhiZGA=s88-c-k-c0x00ffffff-no-rj" class="user-photo">
            <span class="user-name">Vsauce</span>
          </div>
          <p class="reply-text">🤔 Hmm, I guess we'll have to work on our brilliance then 😉 But in all seriousness, philosophy is not just about being a good speaker, it's about exploring and understanding the world around us. So don't be too quick to judge, give us a chance to change your mind 😉</p>
        </div>
      </div>
    </div>
  </div><div class="comment-container">
    <div class="comment">
      <div class="user-info">
        <img src="https://yt3.ggpht.com/4HUFYedoR7shjFNsEy5vYfTdch9-wT_8HI8GPAcGoSi2C9xmyJw3WsHvbL1Edwhxs2XYytmk=s48-c-k-c0x00ffffff-no-rj" class="user-photo">
        <span class="user-name">Burger_kinginator</span>
      </div>
      <p class="comment-text">Dope conversation. Easy for a dummy like me to follow along..</p>
      <div class="replies">
        <span class="reply-count">▲ 1 Replies</span>
        <div class="reply">
          <div class="user-info">
            <img src="https://yt3.ggpht.com/MPHRyR3w30jtHJyXJB816RbucwThQm5nNqsODb5HWSSJDN_pYyz7YjEJkvEqxlX0vxzFqNJDAA=s88-c-k-c0x00ffffff-no-rj" class="user-photo">
            <span class="user-name">Joe Rogan</span>
          </div>
          <p class="reply-text">Glad you enjoyed it! Don't sell yourself short, being a dummy is a valuable asset in this crazy world. Keeps things simple and easy to understand.</p>
        </div>
      </div>
    </div>
  </div><div class="comment-container">
    <div class="comment">
      <div class="user-info">
        <img src="https://yt3.ggpht.com/2LRjPxflXm60m5zCQ6iZz4aGe79NUcI4N5o_xDU2VB_RnkPzfAmJPbGeG18OAe_Y8Fh4SmQILxU=s48-c-k-c0x00ffffff-no-rj" class="user-photo">
        <span class="user-name">Liham sandwich</span>
      </div>
      <p class="comment-text">What’s the deal with the ears on Paton Oswald’s Penguin</p>
      <div class="replies">
        <span class="reply-count">▲ 1 Replies</span>
        <div class="reply">
          <div class="user-info">
            <img src="https://yt3.ggpht.com/ytc/AL5GRJXipygOiNVCPQkTl1NIcpQqR9ezrvhlo0nZzq62ALI=s88-c-k-c0x00ffffff-no-rj" class="user-photo">
            <span class="user-name">CollegeHumor</span>
          </div>
          <p class="reply-text">Well, we hear they're quite the conversation starters at parties. They're also great for picking up FM radio signals, but we advise against using them as a substitute for headphones. Trust us, it's not a good look.</p>
        </div>
      </div>
    </div>
  </div><div class="comment-container">
    <div class="comment">
      <div class="user-info">
        <img src="https://yt3.ggpht.com/ytc/AL5GRJUjhj7rcIiHlOVhqx6hrufrLuUvbtfK4ogrk4PoTA=s48-c-k-c0x00ffffff-no-rj" class="user-photo">
        <span class="user-name">Sophia Freitas</span>
      </div>
      <p class="comment-text">Sombody in my family died beceaus of cancer last year thats why this song still hits me.</p>
      <div class="replies">
        <span class="reply-count">▲ 1 Replies</span>
        <div class="reply">
          <div class="user-info">
            <img src="https://yt3.ggpht.com/aXBmHKABw-J-0ZMxj39wkXpLDEHViOdL5UD71cDG2s5vbeQBWk9mdX3rRxT5U6Wfkvm6o8Uu-dU=s88-c-k-c0x00ffffff-no-nd-rj" class="user-photo">
            <span class="user-name">ImagineDragons</span>
          </div>
          <p class="reply-text">We are so sorry to hear about the loss of your loved one. Our hearts go out to you and your family. Music can be such a powerful healing force and we hope that our song brings you some comfort and memories of your loved one. Thank you for sharing your story with us.</p>
        </div>
      </div>
    </div>
  </div></body>
</html>"""
st.markdown(html_string, unsafe_allow_html=True)



