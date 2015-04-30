#!/usr/bin/python

print "Content-Type: text/html"
print  # a blank line must follow the last HTTP headers

from PrintBarsViews import *;
from views_contents import *;
from Queries import *;

import cgi
import cgitb; cgitb.enable()


def print_all_posts_from_region(order_rule="recent"):
	uid = form["user_id"].value
	rid = form["region_id"].value
	printSortTopBar(uid,rid)
	print_posts_from_region(posts_region(rid, order_rule), uid, rid)
	printAllPosts(uid, rid)

def display_login_page():
	printPlainTopBar()
	print_all_users(login_page())		
	printBlankSideBar()

if __name__ == "__main__":
	form = cgi.FieldStorage()
	

	if "page_id" not in form or form["page_id"].value=="1":
		print "login page"
		if "newUserPress" in form:
			print "adding a user"
			add_user(form["regionChosen"].value)
		
		display_login_page()
		
	elif form["page_id"].value=="2": 
 # 		Home page, view posts in your region"
 		print "Home page, view posts in your region"
 		if "writePost" in form:
			print "Posting a post"
			uid = form["user_id"].value
			rid = form["region_id"].value
			content = form["textBox"].value
			create_post(uid, content, rid)
		
		elif "like" in form:
			pid = form["like"].value
			uid = form["user_id"].value
			ouid = str(get_ouid(pid)[0])
			try:
				create_post_like(uid, pid, "1", ouid)
			except:
				pass
# 				print "<p> FAILED: trying to alter to like"
# # 				like/dis already exists
# 				if str(check_post_like(uid,pid)[0]) =="0": 
# 					print "<p> changing to like"
# # 					if disliked, change to like
# 					print "<p> 1" + uid + pid
# 					update_post_like("1",uid,pid)
# 					
# 					print "<p> changed from dislike to like"
# 				else:
# 				print "<p> NOTHING HAPPENED"
				
		elif "down" in form:
			pid = form["down"].value
			uid = form["user_id"].value
			ouid = get_ouid(pid)[0]
			try:
				create_post_like(uid, pid, "0", ouid)
			except:
				pass
# 				print "trying to alter to like"
# 				# 				like/dis already exists
# 				print "CHECK TO DIS" + str(check_post_like(uid,pid)[0])
# 				if str(check_post_like(uid,pid)[0]) =="1": 
# 					print "CHANGE TO DIS" + str(check_post_like(uid,pid))
# # 					if liked, change to dislike
# 					update_post_like("0",uid,pid)
# 					print "<p> changed like to dislike"
# 				else:
# 					print "<p> NOTHING HAPPENED"
 		
 		if "order_by" in form:
 			print"Chosen Order"
		 	order_rule = form["order_by"].value
		else:
			print "Default order"
			order_rule ="recent"
			
 		print_all_posts_from_region(order_rule)
		
	else:
		print"NOT SUPPOSED TO SEE THIS"
		



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