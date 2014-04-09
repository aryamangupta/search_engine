def index():
    response.flash = T("Welcome to web2py!")
    return dict(message=T('Hello World'), var=request.vars)


def user():
    return dict(form=auth())


def me():   
    form = SQLFORM(db.t)
    form.process()
    return dict(form=form, rows = db(db.t.name.startswith('c')).select())
        
def add():
    form = SQLFORM(db.Restaurants,upload=URL('download'))
    form.process()
    return dict(form=form)
    
def download():
	return response.download(request, db)
    
def found():
    val = request.vars
    c = val.keys()
    a = val[c[0]]
    if db((db.Restaurants.name == a) | (db.Restaurants.city == a) | (db.Restaurants.area == a)).isempty():
       return HTML(H1(P("Page not found"))).xml()
    b = db((db.Restaurants.name == a) | (db.Restaurants.city == a) | (db.Restaurants.area == a)).select()
    return dict(tab=b)
    
def info():
    args = request.args
    var = request.vars
    arg = request.args[0]
    print 'row:',arg
    b = db(db.Restaurants.id == arg).select()
    c = db(db.Comments.rid == arg).select()
    d = db(db.Images.rid == arg).select()
    print arg,d
    return dict(arg = arg, record = b, comments = c, images = d)

def download():
    return response.download(request, db)

@auth.requires_login()    
def home_user():
    response.flash = T("Welcome  " + auth.user.first_name)
    return dict(message=T('Hello  ' + auth.user.first_name))

@auth.requires_login()    
def add_comment():
    print request.args
    form = SQLFORM(db.Comments)    
    form.vars.user = auth.user.first_name
    form.vars.rid = request.args[0]
    if form.process().accepted:
    	response.flash=T("entry inserted")
    elif form.errors:
    	response.flash=T("gaannd mara")
    else:
    	response.flash=T("welcome")
    return dict(form=form)

@auth.requires_login()     
def add_image():
    print "image:",request.args[0]
    form = SQLFORM(db.Images)    
    form.vars.user = auth.user.first_name
    print request.args
    form.vars.rid = request.args[0]
    if form.process().accepted:
    	response.flash=T("entry inserted")
    elif form.errors:
    	response.flash=T("gaannd mara")
    else:
    	response.flash=T("welcome")
    return dict(form=form)
