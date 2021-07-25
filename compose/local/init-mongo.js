db.createUser(
  {
    user: 'root',
    pwd: 'root_2021',
    roles: [
      {
        role: 'readWrite',
        db: 'users'
      }
    ]
  }
)
