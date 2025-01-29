from bson.objectid import ObjectId

 # Use a valid ObjectId string
stateID = '678020dcfad4aca99728741a'

def get_state(db):
    """Check the state from the database."""
    state_doc = db['login_stated'].find_one({"_id": ObjectId(stateID)})

    print(state_doc, "Status")
    if state_doc['state'] == 'open':
        print("State is open")
        return state_doc.get('value', 'open')
    return 'closed'

def login_user(db, collection_name, username, password):
    """Check if the username and password match a record in the database."""
    collection = db[collection_name]
    user = collection.find_one({"user": username, "password": password})
    
    if user:
        return True
    return False