print """
		<!DOCTYPE html>
		<html>
			<head>
			<title>University Room</title>
			<link rel="stylesheet" type="text/css" href="stylesheet.css" media="screen" />
			</head>
			<body>
			<div id="header">
				LiveRoomAdder
			</div>
			<div class="colmask leftmenu">
				<div class="colleft">
					<div class="col1">
							<h2>Room List</h2>
						<p> 
						<table class="maintable">
							<tr>
		 						<td><b>Room-Id</b></font></td>
								<td><b>Room-Name</b></font></td>
								<td><b>Capacity</b></font></td>
							</tr>
							Found + str(number) + rooms.<br>
							<tr>
								<td><a href=?roomID=+str(rid)+> + str(rid) + </a></td>
								<td><a href=?roomID=+str(rid)+> + name + </a></td>
								<td> <!-- capacity --> + str(cap) + </td>
								<td>
									<form method="POST" action="miniUniversity.py">
										<input type="SUBMIT" name="removeRoom" value="Remove">	<!--How do I link this to a method-->
										<input type="hidden" name="removeRoomID" value="PUT THE ID HERE FOR THE ROOM TO REMOVE">
									</form>
								</td>
								<td>
									<form method="POST" action="miniUniversity.py">
										<input type="SUBMIT" name="changeCap" value="Change Capacity">	<!--How do I link this to a method-->
									</form>
								</td>
							</tr>
						</table>
						<br>
						<FORM METHOD="POST" action="miniFacebook.py">
							<INPUT TYPE="SUBMIT" NAME="addRoom" VALUE="Add a Room">
						</FORM>    
						<hr> How about this Magee?
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
