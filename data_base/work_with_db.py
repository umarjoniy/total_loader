import psycopg2

from settings import logger

DB_URI = 'postgres://yjvzcnbkhjgauw:4cbdb1a32494270689f52f36068c99141e2b759731afc055ad25dfed490cc94f@ec2-34-255-225-151.eu-west-1.compute.amazonaws.com:5432/dc31ouckk7qrit'

base = psycopg2.connect(DB_URI)
cur = base.cursor()

def add_user(id, name):
    try:
        cur.execute('INSERT INTO users(id,username) VALUES (%s,%s)', (id, name))
        base.commit()
    except psycopg2.Error as e:
        print(e)


def check_id(id):
    try:
        cur.execute(f"SELECT id FROM users WHERE id={id}")
        for i in cur:
            return 'Yes'
        return 'No'
    except psycopg2.Error as e:
        logger.error(e)


def youtube_videos(video_name, quality, file_size, fps, file_id):
    try:
        cur.execute(r'INSERT INTO youtube_videos(video_name,quality,file_size,fps,file_id) VALUES (%s,%s,%s,%s,%s)',
                    (video_name, quality, file_size, fps, file_id))
        base.commit()
    except psycopg2.Error as e:
        logger.error(e)

def youtube_videos_delete(video_name,quality,fps):
    try:
        cur.execute('DELETE FROM youtube_videos WHERE (video_name=%s AND quality=%s AND fps=%s)',
                    (video_name, quality, fps))
        base.commit()
    except psycopg2.Error as e:
        logger.error(e)



@logger.catch()
def check_youtube_video(video_name, quality, fps):
    try:
        # когда в имени есть ' или " появляется ошибка!!!
        cur.execute("SELECT file_id FROM youtube_videos WHERE (video_name=%s AND quality=%s AND fps=%s)",
                    (video_name, quality, fps))
        for i in cur:
            return i
        return 0
    except psycopg2.Error as e:
        logger.error(e)
        return 'Error'
