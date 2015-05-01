#!/usr/bin/python

print "Content-Type: text/html"
print  # a blank line must follow the last HTTP headers

from PrintBarsViews import *;
from views_contents import *;
from Queries import *;

import cgi
import cgitb; cgitb.enable()

############################################################
def print_all_posts_from_region(order_rule="recent"):
    uid = form["user_id"].value
    rid = form["region_id"].value
    pgid = "2"
    printSortTopBar(uid,rid,pgid)
    print_posts_from_region(posts_region(rid, order_rule), uid, rid)
    printAllPosts(uid, rid,pgid)
############################################################
def login(form):
    if "newUserPress" in form:
#         print "adding a user"
        add_user(form["regionChosen"].value)
    printPlainTopBar()
    print_all_users(login_page())
    printBlankSideBar()
############################################################
def home(form):
    if "writePost" in form:
#         print "Posting a post"
        uid = form["user_id"].value
        rid = form["region_id"].value
        content = form["textBox"].value
        create_post(uid, content, rid)

    elif "like" in form:
        pid = form["like"].value
        uid = form["user_id"].value
        ouid = str(get_ouid_post(pid)[0])
        try:
            create_post_like(uid, pid, "1", ouid)
        except:
            pass
            # print "<p> FAILED: trying to alter to like"
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
        ouid = get_ouid_post(pid)[0]
        try:
            create_post_like(uid, pid, "0", ouid)
        except:
            pass
            # print "trying to alter to like"
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
#         print"Chosen Order"
        order_rule = form["order_by"].value
    else:
#         print "Default order"
        order_rule = "recent"
    print_all_posts_from_region(order_rule)
############################################################
def profile(form):
    uid = form["user_id"].value
    rid = form["region_id"].value
    pgid = "4"

    num_posts = count_posts_from_user(uid)
    regions = get_regions()
    num_comments = count_comments_from_user(uid)

    if "new_region" in form:
        rid = str(form["newRegion"].value)
#         print uid+" "+rid
        update_user_region(rid, uid)
#         print "<p>UPDATED"
    else:
        pass

    user = get_user(uid)
    printPlainTopBar()
    print_user_profile(user, num_posts, regions, num_comments)
    printAllPosts(uid, rid, pgid)


############################################################
def individual_post(form):
    pid = form["post_id"].value
    uid = form["user_id"].value
    rid = form["region_id"].value
    if "write_comment" in form:
        content = form["comment_contents"].value
        create_comment(pid, uid, content)
    elif "post_like" in form:
#         print "trying to like"
        ouid = str(get_ouid_post(pid)[0])
        try:
            create_post_like(uid, pid, "1", ouid)
        except:
            pass
    elif "post_down" in form:
#         print "trying to dislike"
        ouid = str(get_ouid_post(pid)[0])
        try:
            create_post_like(uid, pid, "0", ouid)
        except:
            pass
    elif "comment_like" in form:
#         print "<p>trying to like a comment"
        cid = form["comment_like"].value
        ouid = str(get_ouid_comment(cid)[0])
#         print uid + cid + "1" + ouid
        try:
            create_comment_like(uid, cid, "1", ouid)
        except:
            pass
#             print "FAIL"
    elif "comment_down" in form:
#         print "<p>trying to not-like a comment"
        cid = form["comment_down"].value
        ouid = str(get_ouid_comment(cid)[0])
        try:
            create_comment_like(uid, cid, "0", ouid)
        except:
            pass
#             print "FAIL"
    else:
        pass
#         print "<p> I HAVE FAILED YOU MOMMA!"
    post = get_post(pid)
    comments = get_comments(pid)
    printPlainTopBar()
    print_indv_post_in_region(post, comments, uid, rid)
    printAllPosts(uid, rid, "3")

############################################################
def posts_outside():
    global uid, rid, posts, order_rule, nrid
    uid = form["user_id"].value
    rid = form["region_id"].value
    if "chooseRegion" in form:
        #print "<h1>IN CHOOSEREGION!"
        nrid = form["chooseRegion"].value
    
    if "view_user_posts" in form:
        printPlainTopBar()
        posts = get_posts_from_user(uid)
    elif "view_user_comments" in form:
#         print "view user comments"
        printPlainTopBar()
        posts = get_posts_from_user_comments(uid)
    else:
        if "order_by" in form:
#             print"Chosen Order"
            order_rule = form["order_by"].value
        else:
#             print "Default order"
            order_rule = "recent"
        printNewRegionSortBar(uid, rid, "5", nrid)
        posts = posts_region(nrid, order_rule)  # posts = #posts from this region
    # print contents
    print_posts_from_not_region(posts, uid, rid)
    printAllPosts(uid, rid, "5")

############################################################
def individual_outside():
    global uid, rid, pid, post, comments
    uid = form["user_id"].value
    rid = form["region_id"].value
    pid = form["post_id"].value
    post = get_post(pid)
    comments = get_comments(pid)
    printPlainTopBar()
    print_indv_post_out_region(post, comments)
    printAllPosts(uid, rid, "6")

############################################################
def admin():
    printPlainTopBar()
    printAdminBar()

############################################################
if __name__ == "__main__":
    global form
    form = cgi.FieldStorage()

    if "chooseRegion" in form:
#         print "pressed change region button"
        if (form["chooseRegion"].value == form["region_id"].value):
            home(form)
        else:
            posts_outside()
    elif "page_id" not in form or form["page_id"].value=="1" or "log_out" in form:
#         print "login page"
        login(form)
    elif form["page_id"].value=="2" or "go_home" in form:
#         print "Home page, view posts in your region"
        home(form)
    elif form["page_id"].value=="3":
#         print "Individual post in region"
        individual_post(form);
    elif form["page_id"].value=="4" or "go_profile" in form:
#         print "profile"
        profile(form)
    elif form["page_id"].value=="5":
#         print "All posts, outside region"
        posts_outside()

    elif form["page_id"].value=="6":
#         print "individual post, outside region"
        individual_outside()
    elif form["page_id"].value=="7":
#         print "admin page"
        admin()
    else:
        print"THIS IS EMBARRASSING, YOU ARE NOT SUPPOSED TO SEE THIS!"
