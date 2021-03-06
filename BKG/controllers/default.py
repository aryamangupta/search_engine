def index():
    response.flash = T("Welcome")
    if auth.user != None:
        redirect(URL('home_user'))
    return dict( var=request.vars)


def ace():
    th=[]
    key = request.get_vars["key"]
    roll = request.get_vars["roll"]
    rows = db(db.Restaurants.name.startswith(key)).select()

    json = '{"names":['
    i=0
    for r in rows:
        if(i!=0):
             json += ","
        json += '"'+r['name']+'"'
        i+=1
    json+= "]}"
    return dict(j = json)  


def user():
    return dict(form=auth())


@cache.action()
def download():
    return response.download(request, db)


@auth.requires_signature()
def data():
    return dict(form=crud())


def me():   
    form = SQLFORM(db.t)
    form.process()
    return dict(form=form, rows = db(db.t.name.startswith('c')).select())
    

def login():
    return dict(form = auth())

      
def download():
	return response.download(request, db)

    
def found():
    val = request.vars
    c = val.keys()
    a = val[c[0]]
    a = a.lower()
    a = a.strip()
    print a
    if db((db.Restaurants.name == a) | (db.Restaurants.city == a) | (db.Restaurants.area == a) | (db.Movie_Halls.area == a) | (db.Movie_Halls.name == a) | (db.Movie_Halls.city == a)).isempty():
       return HTML(H1(P("Page not found"))).xml()
    b = db((db.Restaurants.name == a) | (db.Restaurants.city == a) | (db.Restaurants.area == a)).select()
    c = db((db.Movie_Halls.name == a) | (db.Movie_Halls.city == a) | (db.Movie_Halls.area == a)).select()
    return dict(tab=b, mov=c)

    
def info():
    args = request.args
    var = request.vars
    arg = request.args[0]
    print 'row:',arg
    b = db(db.Restaurants.id == arg).select()
    c = db((db.Comments.rid == arg) & (db.Comments.table_name == 'Restaurants')).select()
    d = db(db.Images.rid == arg).select()
    print arg,d
    message = "Hi"
    if c == [] or d == []:
       message = "Nothing to Show"
    
    form_comment = SQLFORM(db.Comments)    
    form_comment.vars.user = auth.user.first_name
    form_comment.vars.rid = request.args[0]
    form_comment.vars.table_name = 'Restaurants'
    if form_comment.process().accepted:
    	response.flash=T("entry inserted")
    elif form_comment.errors:
    	response.flash=T("fill again")
    else:
    	pass
   	    
    form_images = SQLFORM(db.Images)    
    form_images.vars.user = auth.user.first_name
    #print request.args
    form_images.vars.rid = request.args[0]
    if form_images.process().accepted:
    	response.flash=T("entry inserted")
    elif form_images.errors:
    	response.flash=T("fill again")
    else:
    	pass
    return dict(arg = arg, record = b, comments = c, images = d, message = message,form_comment=form_comment,form_images=form_images)


@auth.requires_login()    
def home_user():  
    form_movie = SQLFORM(db.Movie_Halls)
    form_restaurant = SQLFORM(db.Restaurants)
    
    if form_movie.process().accepted:
    	response.flash=T("entry inserted")
    elif form_movie.errors:
    	response.flash=T("fill again")
    else:
    	pass
    	
    if form_restaurant.process().accepted:
    	response.flash=T("entry inserted")
    elif form_restaurant.errors:
    	response.flash=T("fill again")
    else:
    	pass	
    return dict(message=T('Hello  ' + auth.user.first_name),
    				form_movie=form_movie,
    				form_restaurant=form_restaurant)

    
def infom():
    args = request.args
    var = request.vars
    arg = request.args[0]
    print 'row:',arg
    b = db(db.Movie_Halls.id == arg).select()
    c = db((db.Comments.rid == arg) & (db.Comments.table_name == 'Movie_Halls')).select()
    print arg
    message = "Hi"
    if c == []:
       message = "Nothing to Show"
       
    form_mcomment = SQLFORM(db.Comments)    
    form_mcomment.vars.user = auth.user.first_name
    form_mcomment.vars.rid = request.args[0]
    form_mcomment.vars.table_name = 'Movie_Halls'
    if form_mcomment.process().accepted:
    	response.flash=T("entry inserted")
    elif form_mcomment.errors:
    	response.flash=T("fill" )
    else:
    	pass   
    return dict(arg = arg, record = b, comments = c, message = message, form_mcomment=form_mcomment)
  
