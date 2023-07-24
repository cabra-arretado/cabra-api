FROM mysql:latest

ENV MYSQL_DATABASE=cabra-platform
# Yep, I know, this is not secure, but it's just a test and ain't going to prod
# this would be in a .env
ENV MYSQL_ROOT_PASSWORD=123456

# I don't need this, because I'm using a volume
COPY ./seed.sql /docker-entrypoint-initdb.d/

CMD ["mysqld"]

