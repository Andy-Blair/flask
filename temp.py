# -*- coding: utf-8 -*-
from hello import Role, User, db

admin_role = Role(name="Admin")
mod_role = Role(name = "Moderator")
user_role = Role(name="user")
user_john = User(username="john", role=admin_role)
user_susan = User(username="susan", role=user_role)
user_david = User(username="david", role=user_role)

db.session.add(admin_role)
db.session.add(mod_role)
db.session.add(user_role)
db.session.add(user_john)
db.session.add(user_susan)
db.session.add(user_david)

db.session.commit()

print (admin_role.id)
print Role.query.all()