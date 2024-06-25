# IMPORT
import pandas as pd
import matplotlib.pyplot as plt

# DATA 
log_file_to_read = "log_file.txt"

# FUNCTIONs
def read_log_file(file_to_read):

    df = pd.read_csv(file_to_read, delimiter=',', names=["timestamp", "user", "ip_address", "action", "status"])
    return df

def failed_attempt(file_to_read):

    df = pd.read_csv(file_to_read, delimiter=',', header=None, names=["timestamp", "user", "ip_address", "action", "status"])
    failed_logs = df[df['status'].str.contains('FAILED')]
    return failed_logs

def get_many_ip_failed_attempt(file_to_read, multiple_attempts=False, number_attempts=False):

    # Lire les données de log dans un DataFrame pandas
    log_df = pd.read_csv(file_to_read, header=None, names=["timestamp", "user", "ip_address", "action", "status"])

    # Supprimer les espaces en trop dans la colonne 'status'
    log_df['status'] = log_df['status'].str.strip()

    # Filtrer les tentatives échouées
    failed_attempts = log_df[log_df['status'] == 'FAILED']

    # Grouper par adresse IP et calculer le nombre de tentatives échouées, la première et la dernière tentative
    report_df = failed_attempts.groupby('ip_address').agg(
        ko_attempts=('ip_address', 'size'),
        first=('timestamp', 'min'),
        last=('timestamp', 'max')
    ).reset_index()
    
    if multiple_attempts :
        report_df = report_df[report_df['ko_attempts'] > int(number_attempts)]

    # Afficher le rapport sous forme de tableau
    return report_df

def get_graph(report_df):
    
    # Créer un graphique des tentatives échouées par adresse IP
    plt.figure(figsize=(20, 12))
    plt.bar(report_df['ip_address'], report_df['ko_attempts'], color='skyblue')
    plt.xlabel('Adresse IP')
    plt.ylabel('Nombre de tentatives échouées')
    plt.title('Nombre de tentatives échouées par adresse IP')
    plt.xticks(rotation=45)
    plt.tight_layout()

    # Afficher le graphique
    plt.show()
    
def create_alert_message_graph(report_df):
    
        # Itérer sur les lignes du DataFrame
    for index, row in report_df.iterrows():
        # Manipuler chaque ligne comme un Series pandas
        ip_address = row['ip_address']
        ko_attempts = row['ko_attempts']
        first_attempt = row['first']
        last_attempt = row['last']
        
        # Créer un message d'alerte basé sur les données de la ligne
        alert_message = (
            f"IP Address: {ip_address}\n"
            f"Failed Attempts: {ko_attempts}\n"
            f"First Attempt: {first_attempt}\n"
            f"Last Attempt: {last_attempt}\n"
        )
        print(alert_message) 
    
