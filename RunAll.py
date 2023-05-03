with open("SocrataDatasests.py") as a:
    exec(a.read())
with open("senior_project\senior_project\spiders\LAU_Data.py") as b:
    exec(b.read())
#ensure this file is last
with open("senior_project\senior_project\spiders\LAU_Auto.py") as c:
    exec(c.read())