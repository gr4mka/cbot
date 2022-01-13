from pymongo import mongo_client
from datetime import datetime
import settings

client = mongo_client.MongoClient(settings.MONGO_LINK)
db = client[settings.MONGO_DB]


def get_or_create_user(db, effective_user, chat_id):
    user = db.users.find_one({"user_id": effective_user.id})
    if not user:
        user = {
            "user_id": effective_user.id,
            "first_name": effective_user.first_name,
            "last_name": effective_user.last_name,
            "username": effective_user.username,
            "chat_id": chat_id
        }
        db.users.insert_one(user)
    return user

def save_reg(db, user_id, reg_data):
    user = db.users.find_one({"user_id": user_id})
    reg_data['created'] = datetime.now()
    if 'registration' not in user:
        db.users.update_one(
            {'_id': user['_id']},
            {'$set': {'registration': [reg_data]}}
        )
    else:
        db.users.update_one(
            {'_id': user['_id']},
            {'$push': {'registration': reg_data}}
        )
def subscriber(db, user_data):
    if not user_data.get('subscribed'):
        db.users.update_one(
            {'_id': user_data['_id']},
            {'$set': {'subscribed': True}}
        )
def unsubscriber(db, user_data):
        db.users.update_one(
            {'_id': user_data['_id']},
            {'$set': {'subscribed': False}}
        )
def get_subscribed(db):
    return db.users.find({"subscribed": True})