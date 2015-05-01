def printSortTopBar(uid,rid,pgid):
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
        						<FORM type=post action=BisonController.py style="float:right;padding-right:12%;">
        							<select name="order_by">
        								<option value="recent">Most Recent</option>
        								<option value="positive">Most Positive</option>
       									<option value="negative">Most Negative</option>
        								<option value="controversial">Most Controversial</option>
        								<option value="comments">Most Comments</option>
        								<option value="interaction">Most Interaction</option>
       				 				</select>
       				 					<input type=submit name=sort> 
        								<input type=hidden name=user_id value="""+ str(uid) +""">
										<input type=hidden name=region_id value="""+ str(rid) +""">
										<input type=hidden name=page_id value="""+ str(pgid) +""">
                				</FORM>
                			</div>
                
                <div class="colmask leftmenu">
            <div class="colleft">
        <div class="col1">
		"""


def printNewRegionSortBar(uid,rid,pgid,nrid):

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
        						<FORM type=post action=BisonController.py style="float:right;padding-right:12%;">
        							<select name="order_by">
        								<option value="recent">Most Recent</option>
        								<option value="positive">Most Positive</option>
       									<option value="negative">Most Negative</option>
        								<option value="controversial">Most Controversial</option>
        								<option value="comments">Most Comments</option>
        								<option value="interaction">Most Interaction</option>
       				 				</select>
       				 					<input type=submit value=Sort> 
        								<input type=hidden name=user_id value="""+ str(uid) +""">
										<input type=hidden name=region_id value="""+ str(rid) +""">
										<input type=hidden name=page_id value="""+ str(pgid) +""">
										<input type=hidden name=chooseRegion value="""+ str(nrid) +"""> 
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

def printAllPosts(uid, rid, pgid):
    print """
        </div> <!-- close col1 -->
        	<div class="col2">
        		<div class=menuitem>
        			<FORM type=post action=BisonController.py>
        				<input  type=submit name=go_profile value="Profile"> 
						<input type=hidden name=user_id value="""+ str(uid) +""">
						<input type=hidden name=region_id value="""+ str(rid) +""">
						<input type=hidden name=page_id value=4> 
        			</FORM>
        			
        		</div> 
        		<div class=menuitem>
        			<FORM type=post action=BisonController.py>
        				<input type=submit name=go_home value="Home"> 	
						<input type=hidden name=user_id value="""+ str(uid) +""">
						<input type=hidden name=region_id value="""+ str(rid) +""">
						<input type=hidden name=page_id value=2> 
        			</FORM>
        		</div> 
        				<div class=menuitem>
            				<FORM METHOD=POST action=BisonController.py>
            					Choose A Region
           					 		<select name=chooseRegion >
            							<option value="1">Under Where?</option>
            							<option value="3">Over There</option>
            							<option value="2">Outside Your Window</option>
           		 					</select>
           		 					<input type=submit name=post> 
    								<input type=hidden name=user_id value="""+ str(uid) +""">
    								<input type=hidden name=region_id value="""+ str(rid) +""">
            				</FORM>
        				</div>
        				
                          <div class=menuitem>    
                                <FORM type=post action=BisonController.py>
                                <input type=submit name=log_out value="Log Out"> 
								<input type=hidden name=user_id value="""+ str(uid) +""">
								<input type=hidden name=region_id value="""+ str(rid) +""">
								<input type=hidden name=page_id value=1> 
                                </FORM>
                                
                          </div>       
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
        
def printAdminBar(): 
	print """
	</div> <!-- close col1 -->
        	<div class="col2">
        		<div class=menuitem>    
                                <FORM type=post action=BisonController.py>
                                <input type=submit name=log_out value="Log Out">
								<input type=hidden name=page_id value=1> 
                                </FORM>
                                
                          </div>       
                                <br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>
                                </div>
                            </div> <!-- close col 2 -->
                                
                        </div> <!-- close colleft -->
                    </div> <!-- close colmask leftmenu -->
                                
                <div id="footer">
                        <p>Admin</p>
                </div>
            </body>
        </html>
        """
