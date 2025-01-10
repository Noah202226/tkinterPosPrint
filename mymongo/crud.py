from bson.objectid import ObjectId

 # Use a valid ObjectId string
object_id = '678020dcfad4aca99728741a'

def get_state(db):
    """Check the state from the database."""
    state_doc = db['login_stated'].find_one({"_id": ObjectId(object_id)})

    if state_doc['state'] == 'open':
        return state_doc.get('value', 'open')
    return 'closed'

