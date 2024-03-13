import os
dirname = os.path.dirname(__file__)

DATABASE_FILENAME = "ohte_gol.sqlite"
DATABASE_FILE_PATH = os.path.join(dirname, "..", DATABASE_FILENAME)

TEST_DATABASE_FILENAME = "test_ohte_gol.sqlite"
TEST_DATABASE_FILE_PATH = os.path.join(dirname, "..", DATABASE_FILENAME)
