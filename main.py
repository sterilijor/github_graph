import os

from datetime import datetime, timedelta


def make_commits(days: int):
    for day in range(days, 1, -1):
        commit_date = datetime.now() - timedelta(days=day)
        date_str = commit_date.strftime('%d.%m.%Y г.')
        with open('data.txt', 'a', encoding='utf-8') as file:
            file.write(f'{date_str}\n')

        os.system('git add data.txt')
        os.system(f'git commit --date="{date_str}" -m "Commit for {date_str}"')

    os.system('git push -u origin master')


def main():
    start_date = datetime(2020, 9, 1)
    end_date = datetime(2024, 8, 5)
    delta = end_date - start_date

    make_commits(delta.days)


if __name__ == '__main__':
    main()
