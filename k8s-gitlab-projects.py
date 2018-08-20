# List projects:

projects = gl.projects.list()

# Archived projects
projects = gl.projects.list(archived=1)
# Limit to projects with a defined visibility
projects = gl.projects.list(visibility='public')

# List owned projects
projects = gl.projects.owned()

# List starred projects
projects = gl.projects.starred()

# Search projects
projects = gl.projects.list(search='keyword')

# Get a single project:

# Get a project by ID
project = gl.projects.get(10)
# Get a project by userspace/name
project = gl.projects.get('myteam/myproject')

# Create a project:

project = gl.projects.create({'name': 'project1'})

# Create a project for a user (admin only):

alice = gl.users.list(username='alice')[0]
user_project = alice.projects.create({'name': 'project'})
user_projects = alice.projects.list()

# Create a project in a group:

# You need to get the id of the group, then use the namespace_id attribute
# to create the group
group_id = gl.groups.search('my-group')[0].id
project = gl.projects.create({'name': 'myrepo', 'namespace_id': group_id})

# Update a project:

project.snippets_enabled = 1
project.save()

# Delete a project:

gl.projects.delete(1)
# or
project.delete()

# Fork a project:

fork = project.forks.create({})

# fork to a specific namespace
fork = project.forks.create({'namespace': 'myteam'})

# Create/delete a fork relation between projects (requires admin permissions):

project.create_fork_relation(source_project.id)
project.delete_fork_relation()

# Get languages used in the project with percentage value:

languages = project.languages()

# Star/unstar a project:

project.star()
project.unstar()

# Archive/unarchive a project:

project.archive()
project.unarchive()

# Start the housekeeping job:

project.housekeeping()

# List the repository tree:

# list the content of the root directory for the default branch
items = project.repository_tree()

# list the content of a subdirectory on a specific branch
items = project.repository_tree(path='docs', ref='branch1')

# Get the content and metadata of a file for a commit, using a blob sha:

items = project.repository_tree(path='docs', ref='branch1')
file_info = p.repository_blob(items[0]['id'])
content = base64.b64decode(file_info['content'])
size = file_info['size']

# Get the repository archive:

tgz = project.repository_archive()

# get the archive for a branch/tag/commit
tgz = project.repository_archive(sha='4567abc')
