import csv
import re

def txt_to_csv(txt_filename, csv_filename):
    with open(txt_filename, 'r', encoding='utf-8-sig') as txt_file, open(csv_filename, 'w', newline='', encoding='utf-8-sig') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(['Time', 'Other', 'You'])

        time = None
        username = None
        message = None

        for line in txt_file:
            match = re.match(r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) (.*?)$', line.strip())
            if match:
                if time is not None and username is not None and message is not None:
                    if username in {'刘嘉敏', '老赖刘嘉敏', '9191010F0103刘嘉敏'}:
                        csv_writer.writerow([time, message, ''])
                    elif username == '晓萱':
                        csv_writer.writerow([time, '', message])

                time, username = match.groups()
                message = next(txt_file).strip()
            else:
                continue

        if time is not None and username is not None and message is not None:
            if username in {'刘嘉敏', '老赖刘嘉敏', '9191010F0103刘嘉敏'}:
                csv_writer.writerow([time, message, ''])
            elif username == '晓萱':
                csv_writer.writerow([time, '', message])

txt_to_csv('(1042669760).txt', 'chat.csv')
