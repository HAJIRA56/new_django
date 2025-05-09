pip install dj-database-url
import dj-database-url
import os
DATABASES = {
 "default": dj_database_url.parse(os.environ.get("postgresql://test_db_ytfa_user:BsKRCuFigoXpYrg8ORjNNF6hMRLLmF9j@dpg-d0epocemcj7s738321mg-a.oregon-postgres.render.com/test_db_ytfa"))
}
