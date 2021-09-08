# Description

This is a simple job application tracker that takes in 'Company','Contact Details', 'Position', 'Hiring Platform', 'Date Applied' and saves to a SQLite database

# Usage

Currently under construction. Run the view.py file. Once run, set create_db(create=False) to skip table creation call if necessary.

# Python Environment

This script runs on Python 3.9.4.

# Dependencies

This program depends on is for tkcalendar==1.6.1.

# Design Choices

The functionality of the homepage buttons is delegated to classes in funcs.py to create TopLevel windows and handle the logic within the class. Database manipulation is handled in interact_db.py
