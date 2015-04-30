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
        								<option value="positive">Most Positive</option>
       									<option value="negative">Most Negative</option>
        								<option value="controversial">Most Controversial</option>
        								<option value="comments">Most Comments</option>
        								<option value="interaction">Most Interaction</option>
       				 				</select>
       				 					<input type=submit name=post> 
        								<input type=hidden name=userid value=""" + str(uid) +""" >
										<input type=hidden name=regionid value=""" + str(rid) + """>
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
		    			<img src="css/bison.jpg" height=30px width=50px style="float:left;">
		    			<h3> Bison...Say Something
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
        
        <br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>
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

def printAllPosts(uid, rid):
    print """
        </div> <!-- close col1 -->
        	<div class="col2">
        		<div id="menu">
        			<a href="./BisonController.py"><div class="menuitem">Profile</div></a>
        			<a href="BisonController.py"><div class="menuitem">Home</div></a>
        				<div class=menuitem>
            				<FORM METHOD=POST action=BisonController.py>
            					Choose A Region
           					 		<select name=chooseRegion >
            							<option value="1">Under Where?</option>
            							<option value="3">Over There</option>
            							<option value="2">Outside Your Window</option>
           		 					</select>
           		 					<input type=submit name=post> 
    								<input type=hidden name=user_id value="""+ str(uid) +"""
    								<input type=hidden name=user_id value="""+ str(uid) +"""
            				</FORM>
        				</div>
        				<div class=menuitem>
            				<FORM METHOD=POST action=BisonController.py>
    		    				Choose A Topic
    		    				<select name=chooseTopic>
    									<option value="1">Food</option>
    		                            <option value="2">Brandon's Basement</option>
    		                            <option value="3">Coffee</option>
    		                    </select>
    		                    <input type=submit name=post>
    							<input type=hidden name=user_id value="""+ str(uid) +"""
    							<input type=hidden name=user_id value="""+ str(uid) +"""
                            </FORM>
                          </div>      
                                
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

def printInvPosts(uid, rid):
    print """
        </div> <!-- close col1 -->
        	<div class="col2">
        		<div id="menu">
        			<a href="./BisonController.py"><div class="menuitem">Profile</div></a>
        			<a href="./BisonController.py"><div class="menuitem">Home</div></a>
    				<FORM METHOD=POST action=BisonController.py class=menuitem>
    					Choose A Region
   					 		<select name=chooseRegion >
    							<option value="1">Under Where?</option>
    							<option value="3">Over There</option>
    							<option value="2">Outside Your Window</option>
   		 					</select>
   		 					<input type=submit name=post> 
							<input type=hidden name=user_id value="""+ str(uid) +"""
							<input type=hidden name=user_id value="""+ str(uid) +"""
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
