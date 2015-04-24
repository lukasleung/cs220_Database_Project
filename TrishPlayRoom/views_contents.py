print "Content-Type: text/html"

# Print posts from a specific region 
# 	This will work for both logged in users and logged out users
def print_posts_from_region(posts):
	# print out each post, likes number of comments
	for row in posts:
		(pid, content, comments, pos, neg) = row
		print """
						<div id="pcb"> <!--post_comment_block-->
							<div class="l_d_buttons">	<!-- UPDATE PROPER TABLES AND RELOAD PAGE? -->
								<FORM METHOD="POST">
										<button type=submit name="like" value="""
		print str(pid) + ">+ " + str(pos) + """ </button> </br>
										<button type=submit name="down" value="""
		print str(pid) + ">- " + str(neg) + """ </button>
								</FORM>
							</div>
							<div class="p_c"> <!-- THESE WILL TAKE YOU TO THE POST PAGE WHERE WE WILL DISPLAY THE POST AND COMMENTS AFFILIATED -->
								<a href="./----.py?pid="""
		print str(pid) + "> <p class=post>" + content + """</p> </a>						
								<a href="./----.py?pid="""
		print str(pid) + "> <p class=comment>" + str(commets) + """ comment(s) </p> </a>
							</div>
							<hr>
						</div>
			"""


def print_posts_from_region_not_logged_in(posts):
	# print out each post, likes number of comments
	for row in posts:
		(pid, content, comments, pos, neg) = row
		print """
						<div id="pcb"> <!--post_comment_block-->
							<div class="l_d_buttons">	<!-- UPDATE PROPER TABLES AND RELOAD PAGE? -->
								<FORM METHOD="POST">
										<button type=submit name="cannot_like" value="""
		print str(pid) + ">+ " + str(pos) + """ </button> </br>
										<button type=submit name="cannot_down" value="""
		print str(pid) + ">- " + str(neg) + """ </button>
								</FORM>
							</div>
							<div class="p_c"> <!-- THESE WILL TAKE YOU TO THE POST PAGE WHERE WE WILL DISPLAY THE POST AND COMMENTS AFFILIATED -->
								<a href="./----.py?pid="""
		print str(pid) + "> <p class=post>" + content + """</p> </a>						
								<a href="./----.py?pid="""
		print str(pid) + "> <p class=comment>" + str(commets) + """ comment(s) </p> </a>
							</div>
							<hr>
						</div>
			"""


# Prints the text box for when the user is veiwing 
def print_text_box():
	# print out the text box
	print """
					<div id="my_pc"> 
						<h2> Whats on your mind? </h2>
						<FORM align="center" action="" value=postContents>
							<textarea name="textBox"> </textarea>
						</FORM>
						<FORM METHOD="POST" action="----.py">							
								<input name="writePost" value="Post" type="submit">					
						</FORM>
							<br>	
					</div> """

# print out a single post at the top of the page with options to like or dislike
def print_indv_post(post):
	(pid, content, pos, neg) = post

	print """
						<div>
						<div class="l_d_buttons">
							<FORM METHOD="POST">
									<button type=submit id="like" value="""
	print str(pid) + ">+" + str(pos) + """ </button> </br>
									<button type=submit id="down" value= """
	print str(pid) + ">-" + str(neg) + """ </button>
							</FORM>
						</div>
						<div class="p_c"> 
							<p class=indv_post>"""
	print content + "</p></div></div> "


# print out the txt box to write a comment in
def print_comment_on_box():
	print """
					<div id="leave_comment"> 
						<h4> leave a comment </h4>
						<FORM align="center" action="" value=postContents>
							<textarea id=comment_txt name="comment_contents"> </textarea>
						</FORM>
						<FORM METHOD="POST" action="----.py">							
								<input name="write_comment" value="comment" type="submit">					
						</FORM>
							<br>	
					</div>"""

# print out all the comments associated with a single post
def print_all_comments(comments):
	for row in comments
		(cid, content, pos, neg) = row
		print """
					<div id="pcb"> <!--post_comment_block-->
						<div class="l_d_buttons">
							<FORM METHOD="POST">
									<button type=submit id="like" value="""
		print str(cid) + " >+ " + str(pos) + " </button> </br><button type=submit id=down value="
		print str(cid) + " >- " + str(neg) + """ </button>
							</FORM>
						</div>
						<div class="p_c"> 
							<p class="post in_comment">"""
		print content + "</p></div><hr></div>"

# Prints out all Users
def print_all_users(users):
	print """
				<table class="user_table">
					<tr>
 						<td><u><b>User-Id</b></u></font></td>
						<td><u><b>Region</b></u></font></td>
					</tr>
					<tr>
						<a href=?userid=admin><td>Admin</td></a>
						<td>N/A</td>
					</tr>"""
	for row in users
		(uid, region_name) = row
		print "<tr>	<a href=?userid=" + uid + "><td>" + uid + "</td></a>"
		print "<td>" + region_name + "</td> </tr>"
	print "</table>"

# Print out the user profile page
# 	Single row for each one (fetch one)
def print_user_profile(user, num_posts, regions, num_comments)
	(uid, urid, pos, neg) = user
	num_p = num_posts[0]
	num_c = num_comments[0]
	print "<div id=pos_neg><p>Total:  "+ pos + "up votes, " + neg +""" down votes </p>
					<hr>
				</div>


				<div id=profile_container>
					<a href=?uid=""" + uid + """><p> My Posts (""" + num_posts + """) </p></a>
					<FORM method=POST action=BisonController.py>
						<SELECT name=newRegion>"""
	for row in regions:
		(rid, location) = row
		if rid == urid:
			print "<option select=selected value=old>" + location + "</opion>"
		else:	
			print "<option value=" + rid + ">" + location + "</opion>"

	print """						
						</SELECT>
						<INPUT type="SUBMIT" name="newRegion" value="Change">
					</FORM>
					<a href=?uid=""" + uid + """><p> My Comments (""" + num_posts + """)</p></a>
				</div>
		"""
