print "Content-Type: text/html"


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
		(uid, rid, region_name) = row
		print "<tr>	<a href=?userid=" + uid + "><td>" + uid + "</td></a>"
		print "<td>" + region_name + "</td> </tr>"
		print "<input type=hidden name=regionid value=" + rid ">
	print "</table>"


# Print posts from a specific region 
# 	This will work for both logged in users and logged out users
def print_posts_from_region(posts):
	# print text box
	print """
					<div id="my_pc"> 
						<h2> Whats on your mind? </h2>
						<FORM align="center" Method=POST action="BisonController.py" value=postContents>
							<textarea name="textBox"> </textarea>
						</FORM>
						<FORM METHOD="POST" action="BisonController.py">							
								<input name="writePost" value="Post" type="submit">					
						</FORM>
							<br>	
					</div> """
	# print out each post, likes number of comments
	for row in posts:
		(pid, content, comments, pos, neg) = row
		print """
						<div id="pcb"> <!--post_comment_block-->
							<div class="l_d_buttons">
								<FORM METHOD="POST" action=BisonController.py>
										<button type=submit name="like" value="""
		print str(pid) + ">+ " + str(pos) + """ </button> </br>
										<button type=submit name="down" value="""
		print str(pid) + ">- " + str(neg) + """ </button>
								</FORM>
							</div>
							<div class="p_c">
								<a href="./BisonController.py?pid="""
		print str(pid) + "> <p class=post>" + content + """</p> </a>						
								<a href="./BisonController.py?pid="""
		print str(pid) + "> <p class=comment>" + str(commets) + """ comment(s) </p> </a>
							</div>
							<hr>
						</div>
			"""


def print_posts_from_not_region(posts):
	# print out each post, likes number of comments
	for row in posts:
		(pid, content, comments, pos, neg) = row
		print """
						<div id="pcb"> <!--post_comment_block-->
							<div class="l_d_buttons">	<!-- UPDATE PROPER TABLES AND RELOAD PAGE? -->
								<FORM METHOD="POST" action=BisonController.py>
										<button type=submit name="cannot_like" value="""
		print str(pid) + ">+ " + str(pos) + """ </button> </br>
										<button type=submit name="cannot_down" value="""
		print str(pid) + ">- " + str(neg) + """ </button>
								</FORM>
							</div>
							<div class="p_c"> <!-- THESE WILL TAKE YOU TO THE POST PAGE WHERE WE WILL DISPLAY THE POST AND COMMENTS AFFILIATED -->
								<a href="./BisonController.py?pid="""
		print str(pid) + "> <p class=post>" + content + """</p> </a>						
								<a href="./BisonController.py?pid="""
		print str(pid) + "> <p class=comment>" + str(commets) + """ comment(s) </p> </a>
							</div>
							<hr>
						</div>
			"""

# print out a single post at the top of the page with options to like or dislike
def print_indv_post_in_region(post, comments):
	# prints out the post
	(pid, content, pos, neg) = post

	print """
						<div>
						<div class="l_d_buttons">
							<FORM METHOD="POST" action=BisonController.py>
									<button type=submit name="like" value="""
	print str(pid) + ">+" + str(pos) + """ </button> </br>
									<button type=submit name="down" value= """
	print str(pid) + ">-" + str(neg) + """ </button>
							</FORM>
						</div>
						<div class="p_c"> 
							<p class=indv_post>"""
	print content + "</p></div></div> "
	
	# prints out comment text box
	print """
					<div id="leave_comment"> 
						<h4> leave a comment </h4>
						<FORM align="center" action="BisonController.py" value=postContents>
							<textarea id=comment_txt name="comment_contents"> </textarea>
						</FORM>
						<FORM METHOD="POST" action="BisonController.py">							
								<input name="write_comment" value="comment" type="submit">					
						</FORM>
							<br>	
					</div>"""

	# print out all comments
	for row in comments
		(cid, content, pos, neg) = row
		print """
					<div id="pcb"> <!--post_comment_block-->
						<div class="l_d_buttons">
							<FORM METHOD="POST" action=BisonController.py>
									<button type=submit name="like" value="""
		print str(cid) + " >+ " + str(pos) + " </button> </br><button type=submit name=down value="
		print str(cid) + " >- " + str(neg) + """ </button>
							</FORM>
						</div>
						<div class="p_c"> 
							<p class="post in_comment">"""
		print content + "</p></div><hr></div>"


# print out a single post at the top of the page with options to like or dislike
def print_indv_post_out_region(post, comments):
	# prints out the post
	(pid, content, pos, neg) = post

	print """
						<div>
						<div class="l_d_buttons">
							<FORM METHOD="POST" action=BisonController.py>
									<button type=submit id="cantlike" value="""
	print str(pid) + ">+" + str(pos) + """ </button> </br>
									<button type=submit id="cantdown" value= """
	print str(pid) + ">-" + str(neg) + """ </button>
							</FORM>
						</div>
						<div class="p_c"> 
							<p class=indv_post>"""
	print content + "</p></div></div> "

	# print out all comments
	for row in comments
		(cid, content, pos, neg) = row
		print """
					<div id="pcb"> <!--post_comment_block-->
						<div class="l_d_buttons">
							<FORM METHOD="POST" action=BisonController.py>
									<button type=submit id="cantlike" value="""
		print str(cid) + " >+ " + str(pos) + " </button> </br><button type=submit id=cantdown value="
		print str(cid) + " >- " + str(neg) + """ </button>
							</FORM>
						</div>
						<div class="p_c"> 
							<p class="post in_comment">"""
		print content + "</p></div><hr></div>"


# Print out the user profile page
# 	Single row for each one (fetch one)
def print_user_profile(user, num_posts, regions, num_comments):
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

# Display Admin Page with functionallities already inputted
# 	takes (tuple, tuple, tuple, number, tuple)
def print_admin_page(comms_more_post, like_comm_more_post, up_down_post, count_topics, min_topics):
	print """
						<div id=adminfunc>
						<ul>
							<li> <b> Who comments more than they post? </b> 
								<ul>"""
	# print out all people who comment more than they post
	for row in comms_more_post:
		(uid, region_name) = row
		print "<li>" + str(uid) + " from " + region_name + "</li>"

	print """					</ul>
							</li>
							
							<li> <b> Who gets more likes from comments as opposed to posts </b>
								<ul> """
	# print out all people who get more likes from comments vs. posts
	for row in like_comm_more_post:
		(uid, region_name) = row
		print "<li>" + str(uid) + " from " + region_name + "</li>"

	print """					</ul>
							</li>

							<li> <b> Total number of Up/Down votes for each reagion </b>
								<ul>"""
	
	# print out all regions with their total up/down values
	for row in up_down_region:
		(region_name, pos, neg) = row
		print "<li>" + region_name + " has " + str(pos) + " Upvotes and " + str(neg) + " Downvotes </li>"

	print """					</ul>
							</li>
							<li> 
								<!-- Need the number of different topics, then do for loop -->
								<FORM METHOD="POST" action=BisonController.py>
									<b> Who posts in at least 
										<select name="numTopics">"""
	# get the number of topics and the print out the possible options
	num = int(count_topics[0])
	for i in range(num):
		print "<option>" + str(i+1) + "</option>"
	print """
										</select>
									 Topics </b> 
									<input type=submit name=minTopic value=Go>
								</FORM>
								
								<ul> <u> At least""" + num + """:</u>"""
	for row in min_topics:
		(uid, region_name) = row
		print "<li>" + str(uid) + " from " + Region.name + "</li>"

	print """					</ul>
							</li>
						</ul>
					</div>
	"""
