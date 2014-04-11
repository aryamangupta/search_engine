# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## This is a sample controller
## - index is the default action of any application
## - user is required for authentication and authorization
## - download is for downloading files uploaded in the db (does streaming)
## - call exposes all registered services (none by default)
#########################################################################


def index():
    """
    example action using the internationalization operator T and flash
    rendered by views/default/index.html or views/generic.html

    if you need a simple wiki simply replace the two lines below with:
    return auth.wiki()
    """
    response.flash = T("Welcome to web2py!")
    return dict(message=T('Hello'), var=request.vars)

def ace():
    th=[]
    key = request.get_vars["key"]
    roll = request.get_vars["roll"]
    rows = db(db.newtable.name1.startswith(key)).select()
    #rows = db(db.newtable.id > 0).select()
    json = '{"names":['
    i=0
    for r in rows:
        if(i!=0):
             json += ","
        json += '"'+r['name1']+'"'
        i+=1
    json+= "]}"
    return dict(j = json)  

def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/manage_users (requires membership in
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    """
    return dict(form=auth())

@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)


def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()


@auth.requires_signature()
def data():
    """
    http://..../[app]/default/data/tables
    http://..../[app]/default/data/create/[table]
    http://..../[app]/default/data/read/[table]/[id]
    http://..../[app]/default/data/update/[table]/[id]
    http://..../[app]/default/data/delete/[table]/[id]
    http://..../[app]/default/data/select/[table]
    http://..../[app]/default/data/search/[table]
    but URLs must be signed, i.e. linked with
      A('table',_href=URL('data/tables',user_signature=True))
    or with the signed load operator
      LOAD('default','data.load',args='tables',ajax=True,user_signature=True)
    """
    return dict(form=crud())

def me():   
    form = SQLFORM(db.t)
    form.process()
    return dict(form=form, rows = db(db.t.name.startswith('c')).select())
    
def login():
    return dict(form = auth())
    
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
   # form.process()    
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
