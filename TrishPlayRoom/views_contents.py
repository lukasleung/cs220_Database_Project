print "Content-Type: text/html"

def print_posts_from_region(posts):
	# print out each post, likes number of comments
	for row in posts:
		(pid, content, comments, pos, neg) = posts
		print """
						<div id="pcb"> <!--post_comment_block-->
							<div class="l_d_buttons">	<!-- UPDATE PROPER TABLES AND RELOAD PAGE? -->
								<FORM METHOD="POST">
										<button type=submit id="like" value="like" >+ """
		print pos + """ </button> </br>
										<button type=submit id="down" value="dislike">-  """
		print neg + """ </button>
								</FORM>
							</div>
							<div class="p_c"> <!-- THESE WILL TAKE YOU TO THE POST PAGE WHERE WE WILL DISPLAY THE POST AND COMMENTS AFFILIATED -->
								<a href="./----.py?pid="""
		print pid + "> <p class=post>" + content + """</p> </a>						
								<a href="./----.py?pid="""
		print pid + "> <p class=comment>" + commets + """ comment(s) </p> </a>
							</div>
							<hr>
						</div>
			"""

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
