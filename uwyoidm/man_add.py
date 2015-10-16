###
#
# idmManAdd.py
#
# Troy Axthelm
# Advanced Research Computing Center
# University of Wyoming
# troy.axthelm@uwyo.edu
#
# Created: 15 October 2015
#
#
# Modified: <initials> <day> <month> <year> <change notes>
#
###

import logging

__version__='1.0'

def manualadd():
    # if --manual-add, begin interactive process to add IDM user
    logging.debug("begining manual addition process")
    confirm = raw_input("\nYou have selected to manually add a user, continue process (y/n)? [n]: ")

    # check to see if user selected to continue manual process
    if confirm.lower()!='y':
        logging.info("abort manual user process \'%s\', no changes have been made to idm" % confirm)
        exit()

    # prompt for user information
    print("\nPlease fill out the attributes as prompted. (** indicates optional field)\n")

    # username
    username = raw_input("Enter new user's username (eg: arccjdoe): ").replace(" ","")
    firstname = raw_input("**Enter new user's first name (eg: John): ")
    lastname = raw_input("**Enter new user's last name (eg: Doe): ")
    displayname = raw_input("Enter new user's display name (eg: John Doe): ")
    emailaddr = raw_input("**Enter new user's email address (eg: jdoe@mail.com): ")
    phone = raw_input("**Enter new user's phone number (eg: (123)456-789): ")
    orgunit = raw_input("**Enter new user's department or business (eg: Xco, Systems Support): ")
    title = raw_input("**Enter new user's official title or description (eg: Software Specialist): ")
    
    logging.debug("username: %s, firstname: %s, lastname: %s, displayname: %s, emailAddr: %s, phone: %s, orgunit: %s,\
    title: %s" % (username, firstname, lastname, displayname, emailaddr, phone, orgunit, title))

    # verify that required fields are not empty
    if username=='' or displayname=='':
        logging.error("missing required field, abort!")
        exit()

    # confirm user attributes
    print("\nPlease review the user attributes. User will be validated and added to IDM when confirmed.")
    print("\nusername:\t%s\nfirstname:\t%s\nlastname:\t%s\ndisplayname:\t%s\nemailAddr:\t%s\nphone:\t\t%s\norgunit:\t%s\n\
title:\t\t%s" % (username, firstname, lastname, displayname, emailaddr, phone, orgunit, title))

    confirm = raw_input("\nAre all of the above attributes are correct (y/n)? [n]: ") 

    # check to see if user confirmed attributes are correct
    if confirm.lower()!='y':
        logging.info("user attribute not confirmed\'%s\', no changes have been made to idm" % confirm)
        exit()

    logging.info("manual user ready to be added")
    exit()
