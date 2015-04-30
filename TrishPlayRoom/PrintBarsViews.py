def printSortTopBar(uid,rid):
    print """
        <!DOCTYPE html>
        	<html>
        		<head>
        			<title>Bison Unlimited</title>
        			<link rel="stylesheet" type="text/css" href="css/stylesheet.css" media="screen" />
        		</head>
        				<body>
        					<div id="header">
        					<img src="css/bison.jpg" height=30px width=50px style="float:left;">
        					<h3> Bison...Say Something
        						<FORM method=POST style="float:right;padding-right:12%;">
        							<select name="order_by">
        								<option value="recent">Most Recent</option>
        								<option value="positi">Most Positive</option>
       									<option value="negati">Most Negative</option>
        								<option value="contro">Most Controversial</option>
        								<option value="comments">Most Comments</option>
        								<option value="interaction">Most Interaction</option>
       				 				</select>
       				 					<input type=submit name=post> 
        								<input type=hidden name=userid value=""" +uid+""" >"""
            				print """ <input type=hidden name=regionid value=""" + rid + """>
                				</FORM>
                			</div>
                
                <div class="colmask leftmenu">
            <div class="colleft">
        <div class="col1">
		"""

def printPlainTopBar(uid, rid):
    print """
        <!DOCTYPE html>
        	<html>
        	<head>
        		<title>Bison Unlimited</title>
        		<link rel="stylesheet" type="text/css" href="css/stylesheet.css" media="screen" />
        	</head>
        		<body>
        			<div id="header">
        			<img src="css/bison.jpg" height=30px width=50px style="float:left;">
        			<h3> Bison...Say Something
        				<FORM>
        					<input type=hidden name=regionid value=""" + rid + """>"""
            	print """	<input type=hidden name=userid  value="""+ uid + """ >
                
            			</FORM>
                
                	</div>
                
                <div class="colmask leftmenu">
            <div class="colleft">
        <div class="col1">
                
            """

def printBlankSideBar():
    print """
        </div> <!-- CLOSE COL1 -->
        
        	<div class="col2">
        		<div id="menu">
        
        <br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>
        <br><br><br><br><br><br><br><br><br><br><br><br><br><br>
        		</div>
        			</div>
        
        </div>
        </div>
        <div id="footer">
        <p>For Log_In_page </p>
        </div>
        </body>
        </html>
        """

def printAllPosts():
    print """
        </div> <!-- close col1 -->
        	<div class="col2">
        		<div id="menu">
        			<a href="./BisonController.py"><div class="menuitem">Profile</div></a>
        			<a href="BisonController.py"><div class="menuitem">Home</div></a>
        				<FORM METHOD=POST class=menuitem>
        					Choose A Region
       					 		<select name=chooseRegion >
        							<option value="NE">New England</option>
        							<option value="WC">West Coast</option>
        							<option value="BB">Bible Belt</option>
       		 					</select>
       		 					<input type=submit name=post> 
        				</FORM>
        
        				<FORM METHOD=POST class=menuitem>
        				Choose A Topic
        				<select name=chooseTopic>
								<option value="ALL">All Topics</option>
                                <option value="SW">Sport/Wellness</option>
                                <option value="P">Party</option>
                                <option value="SC">School</option>
                        </select>
                        <input type=submit name=post> 
                        </FORM>
                                
                                
                                <a href="BisonController.py?logout"><div class="menuitem">Logout</div></a>
                                <br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>
                                </div>
                            </div> <!-- close col 2 -->
                                
                        </div> <!-- close colleft -->
                    </div> <!-- close colmask leftmenu -->
                                
                <div id="footer">
                        <p>For users that is in a region</p>
                </div>
            </body>
        </html>
        """

def printInvPosts_Admin():
    print """
        </div> <!-- close col1 -->
        	<div class="col2">
        		<div id="menu">
        			<a href="./BisonController.py"><div class="menuitem">Profile</div></a>
        			<a href="./BisonController.py"><div class="menuitem">Home</div></a>
        				<FORM METHOD=POST class=menuitem> 
        				Choose A Region 
        					<select name=chooseRegion >
        						<option value="NE">New England</option>
        						<option value="WC">West Coast</option>
        						<option value="BB">Bible Belt</option>
        					</select>
        					<input type=submit name=post> 
        				</FORM>
        
        
        				<a href="./BisonController.py?logout"><div class="menuitem">Logout</div></a>
        <br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>
        		</div>
        	</div> <!-- close col 2 -->
        
    </div> <!-- close colleft -->
</div> <!-- close colmask leftmenu -->
        
        <div id="footer">
        		<p>admin page</p>
    </div>
</body>
</html>	
        """
