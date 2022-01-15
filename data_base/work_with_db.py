import psycopg2

from settings import logger

DB_URI = 'postgres://ymarfelyurbxsh:9d775269db7a88955fba6f6fb415f19320b59fbdd03cb3d57faf35a82a65f5bb@ec2-52-215-22-82.eu-west-1.compute.amazonaws.com:5432/d56f3k6cmh5ips'

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

def get_users():
    try:
        cur.execute('SELECT id FROM users')
        a=cur.fetchall()
        return a

    except psycopg2.Error as e:
        logger.error(e)
        return 'Error'


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
