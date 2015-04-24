#!/usr/bin/python

from PrintBarsViews import *
from views_contents import *
import cgi
import cgitb; cgitb.enable()

if __name__ == "__main__":

	showLoggedInIndivPost()


	if user_is_logged_in:
		if user_viewing_all_posts:
			if user_is_in_their_region:
				printSortTopBar()
				print_text_box()
				print_posts_from_region(posts)
				printLoggedInDisplayAllPost()
			else:
				printSortTopBar()
				print_posts_from_region(posts)
				printLoggedInDisplayAllPost()
		if user_viewing_one_post:
			if user_is_in_their_region:
				printPlainTopBar()
				print_indv_post(post)
				print_comment_on_box()
				print_all_comments(comments)
				printLoggedInIndivPost()
			else:
				printPlainTopBar()
				print_indv_post(post)
				print_all_comments(comments)
				printLoggedInIndivPost()
		if user_viewing_all_posts:
			

	else:
		if user_logging_in:
			printPlainTopBar()
			print_all_users(users)
			printToLogIn()
		if user_viewing_all_posts:
			printSortTopBar()
			print_posts_from_region(posts)
			printLoggedOutDisplayAllPost()
		else if user_viewing_one_post:
			printPlainTopBar()
			print_indv_post(post)
			print_all_comments(comments)
			printLoggedInIndivPost()
		
