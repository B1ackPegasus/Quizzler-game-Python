import  requests

dict={
    'amount':20,
    'type':'boolean'

}

respond = requests.get("https://opentdb.com/api.php",params=dict)
respond.raise_for_status()
data = respond.json()
question_data=data['results']
