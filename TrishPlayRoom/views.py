# collects all parts of a web page

def blank():
    pass

def error():
    pass

def home():
#   if logged in:
#   if in region:
    pass

def login():
    pass

def logout():
    pass

def post():
#   if IN REGION:
#     return post_outside()
#     else
#     return post_inside()
    pass

def post_list():
#   if IN REGION:
#     return post_outside()
#     else
#     return post_inside()
    pass

def profile():
    pass

def post_list_out_region():
    pass

def post_list_in_region():
#     get all posts from region
    pass

def post_out_region():
    pass

def post_in_region():
    pass

print """
        <!DOCTYPE html>
        <html>
            <head>
            <title>Bison Unlimited</title>
            <link rel="stylesheet" type="text/css" href="css/stylesheet.css" media="screen" />
            </head>
            <body>
            <div id="header">
                <img src="css/bison.jpg" height=30px width =50px>  <!-- CLICK THIS TO GO TO HOMEPAGE -->
                   Bison...Say Something
            </div>
            <div class="colmask leftmenu">
                <div class="colleft">
                    <div class="col1">
        <!-- THIS IS ONE EXAMPLE -->
                        <div id="pcb">
                            <div class="l_d_buttons">    <!-- UPDATE PROPER TABLES AND RELOAD PAGE? -->
                                <FORM METHOD="POST" action="----.py">
                                        <button id="like" >+ "value"</button> </br>
                                        <button id="down" value="dislike">-  "value"</button>
                                </FORM>
                            </div>
                            <div class="p_c"> <!-- THESE WILL TAKE YOU TO THE POST PAGE WHERE WE WILL DISPLAY THE POST AND COMMENTS AFFILIATED -->
                                <a href="./----.py?pid= + pid + "> <p> + post(contents) + </p> </a>                        
                                <a href="./----.py?pid= + pid + "> <p class="comment"> + post(comment) + </p> </a>
                            </div>
                            <hr>
                        </div>
        <!-- THIS IS ONE EXAMPLE -->
                    </div>



                    <div class="col2">
                        <div id="menu">
                            <a href="./miniUniversity.py"><div class="menuitem">All Rooms</div></a>
                            <a href="./miniUniversity.py?addRoom=1"><div class="menuitem">Add a Room</div></a>
                            <a href="./miniUniversity.py?minCap=1"><div class="menuitem">Find a Room of suitable size</div></a>
                            <br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>
                        </div>
                    </div>

                </div>
            </div>
            <div id="footer">
                <p>This page is still in progress</p>
            </div>
            </body>
        </html>
    """
