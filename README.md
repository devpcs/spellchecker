# spellchecker
Spell Checker for the entire website

# Install requirements
pip install -r requirements.txt

# run 
python spellchecker.py -u murul.com


# Notes
1. If you want to avoid reserved words reporting, simpley update the list at the top of the file. Sit back let the program go through entire website page by page and report.

2. Between pages, there is a artifical delay of 0.8 sec. Tune as it suits you.

3. URL has to be full URL with schema. ie. https://www. < website > .com. 
 
<a href="https://www.pivotcloudsolutions.com">Pivot Cloud Plaform</a> AI version is also avaible but only for platfrom users.
