df = pd.DataFrame({'name_0':['Катя', 'Ира', 'Настя'],
                   'name_1':['Ира', 'Лена', 'Оля'],
                   'name_2':['Аня', 'Катя', 'Катя'],
                   'day':[1, 0, 2]})

df_0 = df[['name_0', 'day']].copy()
df_1 = df[['name_1', 'day']].copy()
df_2 = df[['name_2', 'day']].copy()

df_0  = df_0.rename(columns={'name_0': 'name'})
df_1  = df_1.rename(columns={'name_1': 'name'})
df_2  = df_2.rename(columns={'name_2': 'name'})

df_all = pd.concat([df_0, df_1], ignore_index=True, axis=0)
df_all = pd.concat([df_all, df_2], ignore_index=True, axis=0)

df_group = df_all.groupby('name').agg(['sum', 'count']).reset_index().copy()
df_group = df_group.rename(columns={'sum': 'sum_day', 'count': 'count_name'})

df_group['count_day'] = len(df['day'])

df_group
