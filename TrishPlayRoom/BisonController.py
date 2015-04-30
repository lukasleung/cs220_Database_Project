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
	
	
	if "order_by" in form:
		
		uid = form["userid"].value
		rid = form["regionid"].value
		order_rule = form["order_by"].value
		printSortTopBar(uid,rid)
		print_posts_from_region(posts_region(rid, order_rule), uid, rid)
		printAllPosts(uid, rid)
		
	elif "writePost" in form:
		print "Posting a post"
		uid = form["user_id"].value
		rid = form["region_id"].value
		content = form["textBox"].value
		create_post(uid, content, rid)
		printSortTopBar(uid,rid)
		print_posts_from_region(posts_region(rid), uid, rid)
		printAllPosts(uid, rid)
		
	elif "newUserPress" in form:
		# 	add_user
		print "adding a user"
		add_user(form["regionChosen"].value)
		printPlainTopBar()
		print_all_users(login_page())		
		printBlankSideBar()		
		
	elif "page_id" not in form or form["page_id"].value=="1":
		print "login page"
		printPlainTopBar()
		print_all_users(login_page())
		printBlankSideBar()
		
	elif form["page_id"].value=="2": 
# 		Home page, view posts in your region"
		print "Home page, view posts in your region"
		uid = form["user_id"].value
		rid = form["region_id"].value
		printSortTopBar(uid,rid)
		print_posts_from_region(posts_region(rid), uid, rid)
		printAllPosts(uid, rid)
		
	else:
		print"NOT SUPPOSED TO SEE THIS"
		
		
		
# 		create_post(uid, content, rid)


# 	elif form["page_id"].value==7:
# 		print "admin page" 
# 	elif form["page_id"].value==6:
# 		print "outside region, view individual post"
# 	elif form["page_id"].value==5:
# 		print "Outside region, view posts"
# 	elif form["page_id"].value==4:
# 		print "profile page"
# 	elif form["page_id"].value==3:
# 		print "Individual post page"
# # 		uid = form["uid"].value
# #  		rid = form["rid"].value
# #  		printPlainTopBar(uid,rid)



# 		uid = form["userid"].value
#  		rid = form["regionid"].value
#  		printSortTopBar(uid,rid)
#  		posts = posts_region(rid);
#  		print_posts_from_region(posts)
#  		printAllPosts()
# 		
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
# 	elif "userid" in form:
# 		print "loggedin"
# 		uid = form["userid"].value
# 		rid = form["regionid"].value
# 		printSortTopBar(uid,rid)
# 		posts = posts_region(rid);
# 		print_posts_from_region(posts)
# 		printAllPosts()
# 		print "userid is in form"