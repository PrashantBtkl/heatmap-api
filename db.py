import os
import psycopg2


PG_HOST = os.getenv("PG_HOST")
PG_PORT = os.getenv("PG_PORT")
PG_USER = os.getenv("PG_USER")
PG_PASS = os.getenv("PG_PASS")
PG_DB = os.getenv("PG_DB")


heatmaps_table = "test_heatmaps"

get_positions_query = """
SELECT x,y FROM {tbl}
VALUES
WHERE page_id=%s
""".format(
    tbl=heatmaps_table
)

def get_conn():
    return psycopg2.connect(
        host=PG_HOST, port=PG_PORT, user=PG_USER, password=PG_PASS, dbname=PG_DB
    )


def get_positions(page_id, conn):
	try:
		with conn:
			with conn.cursor() as cur:
				cur.execute(
					get_positions_query,
					(page_id,),
				)
				coords = cur.fetchall()

		return coords

	except Exception as e:
		print("exception occurred : ", e)
		print("page not found")