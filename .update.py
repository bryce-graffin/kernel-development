"""
This module updates the README.md file of this repo with the last date it was changed.
"""
import datetime

# get the current date
current_date = datetime.datetime.now()

# import the README.md file and get the lines of text
with open("README.md", encoding='utf-8') as readme:
    readme_lines = readme.readlines()

    # update the first line of the file with the current date
    readme_lines[0] = (
        f'*current as of {current_date.day} {current_date.strftime("%B")} {current_date.year}*\n\n'
    )

# reopen the file and write the lines
with open("README.md", "w", encoding='utf-8') as readme:
    readme.writelines(readme_lines)
