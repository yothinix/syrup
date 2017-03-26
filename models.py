
# start syrup-postgres
# host: localhost
# user: postgres
# pass: postgres

'''
docker run --name syrup-postgres -e POSTGRES_PASSWORD=postgres -p 5432:5432 -d postgres
'''

'''
psql -h localhost -U postgres -d syrup -a -f syrup.sql
'''
