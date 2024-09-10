
from randomuser import RandomUser
import pandas as pd



r = RandomUser()


some_list = r.generate_users(10)


some_list



name = r.get_full_name()
name


for user in some_list:
    print (user.get_full_name()," ",user.get_email())
    

    
print(user.get_full_name())
some_list




for user in some_list:
    print (user.get_picture())



def get_users():
    users =[]
     
    for user in RandomUser.generate_users(10):
        users.append({"Name":user.get_full_name(),"Gender":user.get_gender(),"City":user.get_city(),"State":user.get_state(),"Email":user.get_email(), "DOB":user.get_dob(),"Picture":user.get_picture()})
      
    return pd.DataFrame(users)     



get_users()



df1 = pd.DataFrame(get_users())  


import requests
import json



data = requests.get("https://fruityvice.com/api/fruit/all")



results = json.loads(data.text)



pd.DataFrame(results)


df2 = pd.json_normalize(results)


# In[38]:


df2


cherry = df2.loc[df2["name"] == 'Cherry']
(cherry.iloc[0]['family']) , (cherry.iloc[0]['genus'])


import requests
import json
data = requests.get("https://fruityvice.com/api/fruit/all")
data.text
results = json.loads(data.text)
results
dane=pd.DataFrame(results)
#results[1]['name']
results
dane.head()
dane2 = pd.json_normalize(results)
dane2
#dane.loc[dane["name"] == 'Banana','nutritions']
ufo=dane2.loc[dane["name"] == 'Banana']
print('kalorii w bannanku: ',ufo['nutritions.calories'])

data_banana = df2.loc[df2["name"] == 'Banana']
type(data_banana.iloc[0])

