docker run --name some-redis -d redis redis-server --appendonly yes

docker run --name some-app --link some-redis:redis -d application-that-uses-redis

