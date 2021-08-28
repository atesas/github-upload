import pandas as pd
import plotly.express as px

import plotly.graph_objects as go

channel_name = ["E-Mail",
"Internet Phone",
"Gather info about prod/service/company/research",
"Purchase Prod/Service",
"Financial Services",
"International News/Current Affairs",
"Local News/Current Affairs",
"Read Electronic Magazine",
"Listen To Music",
"Watch Movie/TV Prog",
"Watch short clips",
"Play Games",
"Instant Messaging",
"Job Hunting",
"To blog/Read blog",
"Download video/TV programs/movies",
"Listen to local radio stations",
"Listen to international radio stations",
"Social networking",
"Using search engines",
"Microblogging/twittering",
"Download/listen to podcast"]
all_ages = [7300,
10400,
4475,
6063,
5894,
7258,
9251,
76,
2290,
4531,
9601,
4397,
14219,
1247,
1575,
3150,
1159,
508,
13647,
10017,
5164,
749]
age_25_39 = [3072,
3978,
1888,
2765,
2693,
3058,
3939,
27,
966,
1884,
3782,
1859,
5309,
551,
712,
1265,
544,
236,
5301,
3960,
2034,
349]


data = {'channel_name': channel_name,
        'all_ages': all_ages,
        'age_25_39': age_25_39
        }

df = pd.DataFrame(data, columns=["channel_name", "all_ages", "age_25_39"])

df["r_age"]=round(df["age_25_39"]/df["all_ages"],2)


print(df)



fig = px.bar_polar(df, r="r_age", theta="channel_name", template="seaborn",
                   color_continuous_scale='Bluered_r',)#color_discrete_sequence= px.colors.sequential.Plasma_r)
fig.show()
