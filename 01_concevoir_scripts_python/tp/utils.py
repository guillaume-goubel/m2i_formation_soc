# IMPORT
import pandas as pd

# DATA 
log_file_to_read = "log_file.txt"

# FUNCTIONs
def read_log_file(file_to_read):

    df = pd.read_csv(file_to_read, delimiter=',')
    df.columns = ['datetime', 'username', 'ip', 'action', 'result']
    df_str = df.to_string(index=False)
    return df_str

# Extraites les tentatives de connexion échouées
def failed_attempt(file_to_read):

    df = pd.read_csv(file_to_read, delimiter=',', header=None)
    df.columns = ['datetime', 'username', 'ip', 'action', 'result']
    failed_logs = df[df['result'].str.contains('FAILED')]

    return failed_logs

def get_many_ip_failed_attempt(file_to_read):
    
    df = pd.read_csv(file_to_read, header=None)
    df.columns = ['datetime', 'username', 'ip', 'action', 'result']

    # Convertir la colonne 'datetime' en format datetime
    df['datetime'] = pd.to_datetime(df['datetime'])
    df_sorted = df.sort_values(by='datetime')
    
    # Filtrer les lignes où la colonne 'result' contient 'FAILED'
    # failed_attempts = df_sorted[df['result'].str.contains('FAILED')]

    # # Compter le nombre de tentatives échouées par adresse IP
    # failed_attempts_count = failed_attempts['result'].value_counts()

    # # # Identifier les adresses IP avec des tentatives échouées répétées (plus d'une fois)
    # repeated_failed_attempts = failed_attempts_count[failed_attempts_count > 1]

    # # Convertir les adresses IP en une liste
    # repeated_failed_attempts_list = repeated_failed_attempts.index.tolist()

    # # transform_string_array(repeated_failed_attempts_list, file_to_read)
    # return repeated_failed_attempts_list


# def sort_by_date(file_path):
#     # Lire le fichier texte en tant que DataFrame
#     df = pd.read_csv(file_path, header=None)

#     df.columns = ['datetime', 'username', 'ip', 'action', 'result']

#     # Convertir la colonne 'datetime' en format datetime
#     df['datetime'] = pd.to_datetime(df['datetime'])

#     # Trier par date (colonne 'datetime')
#     df_sorted = df.sort_values(by='datetime')

#     # Afficher le DataFrame trié
#     print(df_sorted)
