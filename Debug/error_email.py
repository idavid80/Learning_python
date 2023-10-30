import csv
import smtplib


# def read_names(contacts, email): por diccionario no haría falta el email
def read_names(contacts):
    # names = "" Para que sea más rápida es mejor crear un diccionario
    names = {}
    with open(contacts) as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            """ lA FUNCIÓN IF NO SERÍA NECESARIA. Se añaden los datos directamente
            if row[0] == email:    
                name = row[1]"""
            names[row[0]] = row[1]
    return names

def send_message(date, title, emails, contacts):
    smtp = smtplib.SMTP('localhost')
    names = read_names(contacts)
    for email in emails.split(','):
        """ Creamos el diccionario fuera del for
        name = get_name(contacts, email)"""
        name = names[email]
        message = message_template(date, title, name)
        message['From'] = 'noreply@example.com'
        message['To'] = email
        smtp.send_message(message)
    smtp.quit()
    pass