# list all the projects
projects = gl.projects.list()
for project in projects:
    print(project)

# get the group with id == 2
group = gl.groups.get(2)
for group in groups:
    print()

# create a new user
user_data = {'email': 'jen@foo.com', 'username': 'jen', 'name': 'Jen'}
user = gl.users.create(user_data)
print(user)

# List access requests from projects and groups:

p_ars = project.accessrequests.list()
g_ars = group.accessrequests.list()

# Create an access request:

p_ar = project.accessrequests.create({})
g_ar = group.accessrequests.create({})

# Approve an access request:

ar.approve()  # defaults to DEVELOPER level
ar.approve(access_level=gitlab.MASTER_ACCESS)  # explicitly set access level

# Deny (delete) an access request:

project.accessrequests.delete(user_id)
group.accessrequests.delete(user_id)
# or
ar.delete()
