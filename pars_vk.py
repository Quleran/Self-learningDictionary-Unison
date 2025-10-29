import requests
import csv
import time

start = time.time()
def get_posts(group_url): # Функция для сбора данных с группы ВК
    token = ''
    posts = []
    offset = 0
    # Условия для количества итераций для каждой группы
    maxoffset = 0
    if (group_url == 'psu_iknt' or group_url == 'abitur_psu_mipt' or group_url == 'physics_psu'):
        maxoffset = 100
    elif (group_url == 'psu_community' or group_url == 'club203390763'):
        maxoffset = 200
    elif (group_url == 'molcentre_psu'):
        maxoffset = 300
    elif (group_url == 'public213358885'):
        maxoffset = 400
    elif (
            group_url == 'abiturients_psu' or group_url == 'psumexmat' or group_url == 'student_philfac_psu' or group_url == 'psycentrpsu'):
        maxoffset = 1500
    elif (group_url == 'so_psu' or group_url == 'wearesial'):
        maxoffset = 2000
    elif (
            group_url == 'psu21' or group_url == 'kpo_psu' or group_url == 'chemfac_psu' or group_url == 'fsf_psu' or group_url == 'geology_psu'):
        maxoffset = 3000
    elif (
            group_url == 'club7557592' or group_url == 'career_psu' or group_url == 'career_psu' or group_url == 'bio_psu'):
        maxoffset = 4000
    elif (group_url == 'ipfpgniu'):
        maxoffset = 5000
    elif (group_url == 'econom_psu' or group_url == 'sdk_academia'):
        maxoffset = 6000
    elif (group_url == 'overhear_pgniu'):
        maxoffset = 31500
    elif (group_url == 'permuniversity'):
        maxoffset = 12000
    else:
        maxoffset = 8000

    while offset < maxoffset:  # Цикл для сбора всех постов
        url = f'https://api.vk.com/method/wall.get?domain={group_url}&access_token={token}&v=5.92'
        response = requests.get(url, params={
            'count': 100,
            'offset': offset
        }
                                )
        data = response.json()

        for item in data['response']['items']:
            text = item['text']
            posts.append({'text': text})
        offset += 100
    with open('vk_posts.csv', 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['text'])

        for post in posts:
            writer.writerow([post['text']])



if __name__ == "__main__":
    posts = get_posts(group_url)

end = time.time()
print("pars",end-start)
