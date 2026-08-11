import gspread
import pandas as pd
import duckdb
import json
import datetime
import os
from google.oauth2.service_account import Credentials

# ==================================================================

def connect_with_sheets():
    scopes = [
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive"
    ]

    creds = Credentials.from_service_account_file(
        "google-credentials.json",
        scopes=scopes
    )

    gc = gspread.authorize(creds)
    sh = gc.open_by_key("1elRko_FbLpPgBnbA1z5jc_d1Cn0yaeljzqUtOTn7eZg")

    worksheet = sh.worksheet('DATOS_NIVEL_NOTA') 
    df_sheet = pd.DataFrame(worksheet.get_all_records())

    with open('data/encode_columns.json', 'r') as f:
        encodes = json.load(f)

    formato_cols = [
        f"""
        COUNT(CASE WHEN tipo_formato = {i} THEN 1 END) 
        AS formato_{i}
        """
        for i in encodes['tipo_formato'].keys()
    ]

    programa_cols = [
        f"""
        COUNT(CASE WHEN programa = {i} THEN 1 END)
        AS programa_{i}
        """
        for i in encodes['programa'].keys()
    ]

    return df_sheet, formato_cols, programa_cols

# ==================================================================

def create_parquet_general(df_sheet, formato_cols, programa_cols):
    conn = duckdb.connect()
    conn.register("df_sheet", df_sheet)

    conn.execute(
        f""" 
        COPY(
            SELECT 
                fecha_peticion AS fecha,
                COUNT(DISTINCT id) AS peticiones,
                COUNT(
                    CASE WHEN fecha_emision != '' THEN 1 END
                ) 
                AS transmitidas,
                COUNT(
                    CASE WHEN fecha_emision = '' THEN 1 END
                )
                AS rechazadas,
                COUNT(
                    CASE WHEN clasificacion = 1 THEN 1 END
                ) 
                AS politicas,
                COUNT(
                    CASE WHEN clasificacion = 0 THEN 1 END
                ) 
                AS no_politicas,
                {','.join(formato_cols)},
                {','.join(programa_cols)}
            FROM 
                df_sheet
            GROUP BY
                fecha
            ORDER BY
                strptime(fecha, '%d-%m-%Y') DESC
        )
        TO 'data/OKR_abril.parquet' (FORMAT PARQUET)
        """
    )

    conn.execute(
        f""" 
        COPY(
            (SELECT * FROM 'data/OKR_abril.parquet')
            UNION ALL
            (SELECT * FROM 'data/OKR_historic.parquet')
        )
        TO 'data/OKR_data.parquet' (FORMAT PARQUET)
        """
    )

    conn.close()

# ==================================================================

def create_parquet_note(df_sheet):
    conn = duckdb.connect()
    conn.register("df_sheet", df_sheet)

    conn.execute(
        f""" 
        COPY(
            SELECT * FROM df_sheet
        )
        TO 'data/OKR_data_note.parquet' (FORMAT PARQUET)
        """
    )

    conn.close()

# ==================================================================

def main():
    file = 'OKR_data.parquet'
    if os.path.exists(os.path.join('data', file)):
        os.remove(f'data/{file}')

    df_sheet, formato_cols, programa_cols = connect_with_sheets()
    create_parquet_general(df_sheet, formato_cols, programa_cols)

    file = 'OKR_data_note.parquet'
    if os.path.exists(os.path.join('data', file)):
        os.remove(f'data/{file}')
        
    df_sheet, _, _ = connect_with_sheets()
    create_parquet_note(df_sheet)

if __name__ == "__main__":
    main()