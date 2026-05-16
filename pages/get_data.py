import duckdb
import os
import threading

file = next((file for file in os.listdir('data/') if 'OKR_data' in file), None)
path_file = os.path.join('data', file)

if file is None:
    raise ValueError(
        "[!] No existe OKR_data en el directorio"
    )

conn = duckdb.connect()
lock = threading.Lock() 

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