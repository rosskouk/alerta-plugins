# Alerta plugin routing rules

# Only send warning and critical alerts via Telegram.
def rules(alert, plugins):

    #print('Available attributes in alert object: \n\n')
    #print(dir(alert))
    #print('\n\n')
    #print('\n\nAlert Dup Count: ' + str(alert.duplicate_count))
    #print('\n\nAlert Severity: ' + str(alert.severity))
    if alert.severity not in ['informational']:
        print('\n\nAlert severity was not informational - reject, telegram')
        return [plugins['reject'], plugins['telegram']]
    else:
        print('\n\nAlert severity was informational - reject')
        return [plugins['reject']]