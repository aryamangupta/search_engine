db = DAL('sqlite://storage.sqlite')
from gluon.tools import Auth
auth = Auth(db) #secure=True
auth.define_tables(username=True)

#db.auth_user.password.requires=IS_STRONG()
#fr#om gluon.tools import Recaptcha
#auth.settings.captcha = Recaptcha(request,
 #   '6LcD0PESAAAAAAv8xXDZS_g39KeqDKVhdpw5Ui3B',
  #  '6LcD0PESAAAAACBYOTT1juQXfClchb_QP8BuXCOZ')

db.define_table('Restaurants',
                Field('name','string',required=True,requires=IS_LOWER()),       
                Field('area',required=True,requires=IS_LOWER()),
                Field('city',required=True,requires=IS_LOWER()),
                Field('address','string',requires=IS_NOT_EMPTY()),
                Field('cuisine','string',requires=IS_NOT_EMPTY()), 
                Field('comments'),
                Field('images','upload'))

db.Restaurants.name.requires=IS_NOT_EMPTY()
db.Restaurants.area.requires=IS_NOT_EMPTY()
db.Restaurants.city.requires=IS_NOT_EMPTY()

db.define_table('Comments',Field('comment','string',requires=IS_NOT_EMPTY()),
                Field('user','string',readable=False,writable=False),
                Field('rid','integer',readable=False,writable=False),
                Field('table_name','string',readable=False,writable=False))

db.define_table('Images',
                Field('image','upload',requires=IS_NOT_EMPTY()),
                Field('user','string',readable=False,writable=False),
                Field('rid','integer',readable=False,writable=False))

db.define_table('Movie_Halls',
            Field('name','string',required=True,requires=IS_LOWER()),
            Field('area',required=True,requires=IS_LOWER()),
            Field('city','string',required=True,requires=IS_LOWER()),
            Field('comments','string'),
            Field('location','string',required=True,requires=IS_NOT_EMPTY()),
            Field('images','upload'))

db.Movie_Halls.name.requires=IS_NOT_EMPTY()
db.Movie_Halls.area.requires=IS_NOT_EMPTY()
db.Movie_Halls.city.requires=IS_NOT_EMPTY()

