#!/usr/bin/python

print "Content-Type: text/html"
print  # a blank line must follow the last HTTP headers

from PrintBarsViews import *;
from views_contents import *;
from Queries import *;

import cgi
import cgitb; cgitb.enable()

if __name__ == "__main__":
	form = cgi.FieldStorage()
	
	
	if "newUserPress" in form:
		# 	add_user
		print "adding a user"
		add_user(form["regionChosen"].value)
		
		printPlainTopBar()
		print_all_users(login_page())		
		printBlankSideBar()		
	elif "page_id" not in form or form["page_id"].value==1:
		print "login page"
		printPlainTopBar()
		print_all_users(login_page())		
		printBlankSideBar()
	elif form["page_id"].value==7:
		print "admin page" 
	elif form["page_id"].value==6:
		print "outside region, view individual post"
	elif form["page_id"].value==5:
		print "Outside region, view posts"
	elif form["page_id"].value==4:
		print "profile page"
	elif form["page_id"].value==3:
		print "Individual post page"
	elif form["page_id"].value==2:
		print "Home page, view posts in your region"
		
# 	elif "pageid" not in form or "userid" not in form or form["userid"].value =="-1":
# 		print "userid is logging in!"
# 		printPlainTopBar("-1", "-1")
# 		print_all_users(login_page())		
# 		printBlankSideBar()
# 	elif form["userid"].value == "admin":
# 		print
# 	elif "pid" in form:
# 		print "in a post now xD"
# 		uid = form["uid"].value
# 		rid = form["rid"].value
# 		printPlainTopBar(uid,rid)
# 		
# 	elif "newUserPress" in form:
# 		print "user was just added"
# 		# create the new person
# 		added_user_region = form["regionChosen"].value
# 		add_user(added_user_region)
# 		printPlainTopBar("-1", "-1")
# 		print_all_users(login_page())		
# 		printBlankSideBar()
# 		
# 	elif "userid" in form:
# 		print "loggedin"
# 		uid = form["userid"].value
# 		rid = form["regionid"].value
# 		printSortTopBar(uid,rid)
# 		posts = posts_region(rid);
# 		print_posts_from_region(posts)
# 		printAllPosts()
# 		print "userid is in form"
# 		
# 	elif "userid" not in form or form["userid"].value =="-1":
# 		print "userid is logging in!"
# 		printPlainTopBar("-1", "-1")
# 		print_all_users(login_page())		
# 		printBlankSideBar()
		