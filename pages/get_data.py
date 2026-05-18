import duckdb
import os
import threading
import json

file = next((file for file in os.listdir('data/') if 'OKR_data' in file and 'note' not in file), None)
path_file = os.path.join('data', file)

file_note = next((file for file in os.listdir('data/') if 'OKR_data_note' in file), None)
path_file_note = os.path.join('data', file_note)

if file is None:
    raise ValueError(
        "[!] No existe OKR_data en el directorio"
    )

conn = duckdb.connect()
lock = threading.Lock() 

with open('data/encode_columns.json', 'r', encoding = 'utf-8') as f:
    encodes = json.load(f)

# ====================================

def get_transmitidas_y_rechazadas(type_, value):
    global conn, path_file

    with lock:
        if type_ == "mes":
            return conn.execute(
                f""" 
                SELECT 
                    MONTH(strptime(fecha, '%d-%m-%Y')) AS mes,
                    SUM(transmitidas) AS transmitidas,
                    SUM(rechazadas) AS no_transmitidas
                FROM 
                    '{path_file}'
                WHERE
                    strptime(fecha, '%d-%m-%Y') >= DATE '2026-01-01'
                    AND
                    MONTH(strptime(fecha, '%d-%m-%Y')) = ?
                GROUP BY
                    1
                ORDER BY
                    mes ASC
                """
            , parameters = [value]).df()

        elif type_ == "trimestre":
            return conn.execute(
                f""" 
                SELECT 
                    QUARTER(strptime(fecha, '%d-%m-%Y')) AS mes,
                    SUM(transmitidas) AS transmitidas,
                    SUM(rechazadas) AS no_transmitidas
                FROM 
                    '{path_file}'
                WHERE
                    strptime(fecha, '%d-%m-%Y') >= DATE '2026-01-01'
                    AND
                    QUARTER(strptime(fecha, '%d-%m-%Y')) = ?
                GROUP BY
                    1
                ORDER BY
                    mes ASC
                """
            , parameters = [value]).df()

        elif type_ == "historico":
            return conn.execute(
                f""" 
                SELECT 
                    SUM(transmitidas) AS transmitidas,
                    SUM(rechazadas) AS no_transmitidas
                FROM 
                    '{path_file}'
                WHERE
                    strptime(fecha, '%d-%m-%Y') >= DATE '2026-01-01'
                """
            ).df()

# ====================================

def get_politicas_y_no_politicas(type_, value):
    global conn, path_file

    with lock:
        if type_ == "mes":
            return conn.execute(
                f""" 
                SELECT 
                    MONTH(strptime(fecha, '%d-%m-%Y')) AS mes,
                    SUM(politicas) AS politicas,
                    SUM(no_politicas) AS no_politicas
                FROM 
                    '{path_file}'
                WHERE
                    strptime(fecha, '%d-%m-%Y') >= DATE '2026-01-01'
                    AND
                    MONTH(strptime(fecha, '%d-%m-%Y')) = ?
                GROUP BY
                    1
                ORDER BY
                    mes ASC
                """
            , parameters = [value]).df()

        elif type_ == "trimestre":
            return conn.execute(
                f""" 
                SELECT 
                    QUARTER(strptime(fecha, '%d-%m-%Y')) AS mes,
                    SUM(politicas) AS politicas,
                    SUM(no_politicas) AS no_politicas
                FROM 
                    '{path_file}'
                WHERE
                    strptime(fecha, '%d-%m-%Y') >= DATE '2026-01-01'
                    AND
                    QUARTER(strptime(fecha, '%d-%m-%Y')) = ?
                GROUP BY
                    1
                ORDER BY
                    mes ASC
                """
            , parameters = [value]).df()

        elif type_ == "historico":
            return conn.execute(
                f""" 
                SELECT 
                    SUM(politicas) AS politicas,
                    SUM(no_politicas) AS no_politicas
                FROM 
                    '{path_file}'
                WHERE
                    strptime(fecha, '%d-%m-%Y') >= DATE '2026-01-01'
                """
            ).df()
        
# ====================================

def get_months_and_quarters_with_data():
    global conn, path_file

    with lock:
        df_month = conn.execute(
            f""" 
            SELECT DISTINCT MONTH(strptime(fecha, '%d-%m-%Y')) AS mes FROM '{path_file}'
            WHERE strptime(fecha, '%d-%m-%Y') >= DATE '2026-01-01'
            ORDER BY mes
            """
        ).df()

        df_quarter = conn.execute(
            f""" 
            SELECT DISTINCT QUARTER(strptime(fecha, '%d-%m-%Y')) AS trimestre FROM '{path_file}'
            WHERE strptime(fecha, '%d-%m-%Y') >= DATE '2026-01-01'
            ORDER BY trimestre
            """
        ).df()

        return df_month, df_quarter 
    
# ====================================
    
def get_transmitidas_y_rechazadas_por_mes():
    global conn, path_file 

    with lock:
        return conn.execute(
            f"""
            SELECT
                MONTH(strptime(fecha, '%d-%m-%Y')) AS mes,
                SUM(transmitidas) as transmitidas,
                SUM(rechazadas) as rechazadas
            FROM 
                '{path_file}'
            WHERE 
                strptime(fecha, '%d-%m-%Y') >= DATE '2026-01-01'
            GROUP BY
                1
            ORDER BY
                mes
            """
        ).df()
    
# ====================================
    
def get_ultimas_5_semanas():
    global conn, path_file_note

    with lock:
        return conn.execute(
            f"""
            SELECT 
                DISTINCT WEEK(strptime(fecha_peticion, '%d-%m-%Y')) AS semana
            FROM 
                '{path_file_note}'
            ORDER BY
                semana DESC
            LIMIT 5
            """
        ).df()
    
# ====================================

def get_formato_de_peticiones(semana):
    global conn, path_file_note

    with lock:
        df = conn.execute(
        f"""
        WITH base AS (       
            SELECT
                WEEK(strptime(fecha_peticion, '%d-%m-%Y')) AS semana,
                tipo_formato AS formato,
                COUNT(DISTINCT id) AS peticiones,
                COUNT(
                    CASE WHEN fecha_emision != '' THEN 1 END
                ) AS transmitidas
            FROM 
                '{path_file_note}'
            GROUP BY
                1, 2
            ORDER BY
                1 DESC, 3 DESC
        )

        SELECT 
            formato,
            peticiones,
            transmitidas
        FROM 
            base
        WHERE 
            semana = ?
        """
    , [semana]).df()
        
    df['formato'] = df['formato'].astype(str)
    df['formato'] = df['formato'].map(encodes['tipo_formato'])

    return df
    
# ====================================

def get_peticiones_por_programa(semana):
    global conn, path_file_note

    with lock:
        df = conn.execute(
        f"""
        WITH base AS (       
            SELECT
                WEEK(strptime(fecha_peticion, '%d-%m-%Y')) AS semana,
                programa AS programa,
                COUNT(DISTINCT id) AS peticiones,
                COUNT(
                    CASE WHEN fecha_emision != '' THEN 1 END
                ) AS transmitidas
            FROM 
                '{path_file_note}'
            GROUP BY
                1, 2
            ORDER BY
                1 DESC, 3 DESC
        )

        SELECT 
            programa,
            peticiones,
            transmitidas
        FROM 
            base
        WHERE 
            semana = ?
        """
    , [semana]).df()
        
    df['programa'] = df['programa'].astype(str)
    df['programa'] = df['programa'].map(encodes['programa'])

    return df