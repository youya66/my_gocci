from mongoengine import fields,connect,Document;

connect("my_gocci_test_db");

class Users (Document):
	_id = fields.IntField(required=True,primary_key=True);
	id_name = fields.StringField(required=True);
	user_name = fields.StringField(required=True);
	