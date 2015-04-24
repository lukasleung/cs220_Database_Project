def printSortTopBar():
	print """
	<!DOCTYPE html>
<html>
    <head>
		<title>Bison Unlimited</title>
		<link rel="stylesheet" type="text/css" href="css/stylesheet.css" media="screen" />
    </head>
    <body>
		<div id="header">
			<img src="css/bison.jpg" height=30px width=50px style="float:left;">  <!-- CLICK THIS TO GO TO HOMEPAGE -->
		    <h3> Bison...Say Something 
			<FORM method=POST style="float:right;padding-right:12%;">
				<select name="orderby">
					<option value="recent">Most Recent</option>
			  		<option value="positi">Most Positive</option>
			  		<option value="negati">Most Negative</option>
			  		<option value="contro">Most Controversial</option>
				</select> 	
			</FORM>
		</div>

		<div class="colmask leftmenu">
			<div class="colleft">
				<div class="col1">
    """

def printPlainTopBar():
    print """
        <!DOCTYPE html>
    <html>
        <head>
            <title>Bison Unlimited</title>
            <link rel="stylesheet" type="text/css" href="css/stylesheet.css" media="screen" />
        </head>
        <body>
            <div id="header">
            <img src="css/bison.jpg" height=30px width=50px style="float:left;">  <!-- CLICK THIS TO GO TO HOMEPAGE -->
            <h3> Bison...Say Something
          
            </div>
        
        <div class="colmask leftmenu">
            <div class="colleft">
                <div class="col1">
                
        """

def printLoggedInDisplayAllPost():
    print """
        </div> <!-- close col1 -->
				<div class="col2">
					<div id="menu">
						<a href="./----.py"><div class="menuitem">Profile</div></a>

						<FORM METHOD=POST class=menuitem> 
							Choose A Region 
							<select name=chooseRegion >
			  					<option value="NE">New England</option>
			  					<option value="WC">West Coast</option>
			  					<option value="BB">Bible Belt</option>
							</select>
						</FORM>

						<FORM METHOD=POST class=menuitem> 
							Choose A Topic
							<select name=chooseTopic>
								<option value="ALL">All Topics</option>
			  					<option value="SW">Sport/Wellness</option>
			  					<option value="P">Party</option>
			  					<option value="SC">School</option>
							</select>
						</FORM>
						
				
						<a href="./----.py?logout"><div class="menuitem">Logout</div></a>
						<br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>
					</div>
				</div> <!-- close col 2 -->

			</div> <!-- close colleft -->
		</div> <!-- close colmask leftmenu -->

		<div id="footer">
			<p>This is the Home Page when users first log in, displaying all post in their region</p>
		</div>
    </body>
</html>	

"""

def printLoggedInIndivPost():
	print """
	</div> <!-- close col1 -->
				<div class="col2">
					<div id="menu">
						<a href="./----.py"><div class="menuitem">Profile</div></a>
						<a href="./----.py"><div class="menuitem">Home</div></a>
						<a href="./----.py?logout"><div class="menuitem">Logout</div></a>
						<br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>
					</div>
				</div> <!-- close col 2 -->

			</div> <!-- close colleft -->
		</div> <!-- close colmask leftmenu -->

		<div id="footer">
			<p>This page shown to people who are logged in and is looking at a single post</p>
		</div>
    </body>
</html>	

"""
        
def printLoggedInProfile():
	print """
	</div> <!-- close col1 -->
				<div class="col2">
					<div id="menu">
					
						<a href="./----.py"><div class="menuitem">Home</div></a>
						<a href="./----.py?logout"><div class="menuitem">Logout</div></a>
						<br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>
					</div>
				</div> <!-- close col 2 -->

			</div> <!-- close colleft -->
		</div> <!-- close colmask leftmenu -->

		<div id="footer">
			<p>This page shown to people who are logged in and is at their profile page</p>
		</div>
    </body>
</html>	

"""

def printLoggedOutIndivPost(): 
	print """
	</div> <!-- close col1 -->
				<div class="col2">
					<div id="menu">
					
						<a href="./----.py"><div class="menuitem">Log In</div></a>
						<a href="./----.py"><div class="menuitem">Home</div></a>
						<br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>
					</div>
				</div> <!-- close col 2 -->

			</div> <!-- close colleft -->
		</div> <!-- close colmask leftmenu -->

		<div id="footer">
			<p>This someone that is logged out/not sign in and is looking at a single post </p>
		</div>
    </body>
</html>	
"""
	
def printLoggedOutDisplayAllPost():
	print """
	     </div> <!-- close col1 -->
				<div class="col2">
					<div id="menu">
						<a href="./----.py"><div class="menuitem">Log In</div></a>

						<FORM METHOD=POST class=menuitem> 
							Choose A Region 
							<select name=chooseRegion >
			  					<option value="NE">New England</option>
			  					<option value="WC">West Coast</option>
			  					<option value="BB">Bible Belt</option>
							</select>
						</FORM>

						<FORM METHOD=POST class=menuitem> 
							Choose A Topic
							<select name=chooseTopic>
								<option value="ALL">All Topics</option>
			  					<option value="SW">Sport/Wellness</option>
			  					<option value="P">Party</option>
			  					<option value="SC">School</option>
							</select>
						</FORM>
						
				
						
						<br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>
					</div>
				</div> <!-- close col 2 -->

			</div> <!-- close colleft -->
		</div> <!-- close colmask leftmenu -->

		<div id="footer">
			<p>This page is for those that are logged out and is viewing all post from the main page</p>
		</div>
    </body>
</html>	
	""" 
	
	
def printToLogIn():
	print """
	
	</div> <!-- close col1 -->
				<div class="col2">
					<div id="menu">
					
						<a href="./----.py"><div class="menuitem">Home</div></a>
						<br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>
					</div>
				</div> <!-- close col 2 -->

			</div> <!-- close colleft -->
		</div> <!-- close colmask leftmenu -->

		<div id="footer">
			<p>This page is for users to sign in </p>
		</div>
    </body>
</html>	
"""

def showLoggedInIndivPost():
	printSortTopBar()
	printLoggedInIndivPost() 
	
	
	
	
        
