import pandas as pd


def _convert_cols_to_int(df: pd.DataFrame, cols: list[str]):
    for col in cols:
        df[col] = df[col].astype(int)


def preprocess_item(item_dict: dict) -> pd.DataFrame:
    df = pd.DataFrame([item_dict])

    df['name'] = df['name'].apply(lambda x: x.split()[0])

    df['mileage'] = df['mileage'].str.replace(r' kmpl| km/kg', '', regex=True).astype(float)
    df['engine'] = df['engine'].str.replace(r' CC', '', regex=True).astype(float)
    df['max_power'] = df['max_power'].str.replace(r' bhp', '', regex=True)
    df['max_power'] = df['max_power'].replace('', '0.0').astype(float)

    df.drop(columns=['torque'], inplace=True)

    _convert_cols_to_int(df, ['engine', 'seats'])

    return df
