import pandas as pd
import json
import datetime

# 导入数据
df = pd.read_csv('chat.csv')

# 时间字符串转换为datetime对象
df['Time'] = pd.to_datetime(df['Time'])

# 对时间进行排序
df = df.sort_values('Time')

# 创建一个新的列，表示是否新的对话开始
df['New_dialogue'] = (df['Time'].diff() > pd.Timedelta(minutes=30)) | df['Time'].diff().isna()

# 创建一个新的列，表示对话的id
df['Dialogue_id'] = df['New_dialogue'].cumsum()

# 初始化json列表
json_list = []

# 对每个对话进行处理
for dialogue_id, group in df.groupby('Dialogue_id'):
    # 初始化对话
    dialogue = {'prompt': '', 'completion': ''}
    
    # 对每个消息进行处理
    for i, row in group.iterrows():
        if pd.notna(row['Other']):
            # 对方的消息
            dialogue['prompt'] += row['Other'] + '\n'
        elif pd.notna(row['You']):
            # 我方的消息
            dialogue['completion'] += row['You'] + '\n'
    
    # 删除最后一个换行符
    dialogue['prompt'] = dialogue['prompt'].rstrip('\n')
    dialogue['completion'] = dialogue['completion'].rstrip('\n')
    
    # 添加到json列表
    json_list.append(dialogue)

# 把json列表保存为json文件
with open('dialogue.json', 'w') as f:
    json.dump(json_list, f)
