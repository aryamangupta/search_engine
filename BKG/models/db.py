db = DAL('sqlite://storage.sqlite')

from gluon.tools import Auth
auth = Auth(db)															#,secure=True to force authenticate pages to go over HTTPS							
auth.define_tables(username=True)							
				
#db.auth_user.password.requires=IS_STRONG()								# password requires some strongness such as one uppercase one number etc
#auth.settings.login_after_registration = True							#automatic login after registration


db.define_table('Restaurants',
			Field('name','string',required=True),
			Field('area',required=True),
			Field('city',required=True),
			Field('comments'),
			Field('images','upload'))



db.define_table('Comments',Field('comment','string'),
			Field('user','string',readable=False,writable=False),
			Field('rid','integer',readable=False,writable=False))

db.define_table('Images',Field('image','upload'),
			Field('user','string',readable=False,writable=False),
			Field('rid','integer',readable=False,writable=False))



#from gluon.contrib.login_methods.rpx_account import RPXAccount
#auth.settings.actions_disabled=['register','change_password','
#request_reset_password']
#auth.settings.login_form = RPXAccount(request,
#api_key='...',
#domain='...',
#url = "http://your-external-address/%s/default/user/login" % request.
#application)
																		#3rd party authentication								

