# Alerta plugin routing rules

# Ensure alerts have occurred at least 3 time and are not informational before alerting
def rules(alert, plugins):

    print('Alert attributes: \n\n')
    print(dir(alert))
    print('\n\n')
    print('\n\nAlert Dup Count: ' + str(alert.duplicate_count))
    print('\n\nAlert Severity: ' + str(alert.severity))
    if alert.duplicate_count:
        print('\n\nAlert Dup Count IF: ' + str(alert.duplicate_count))
        if alert.duplicate_count <= 2:
            print('\n\nAlert duplicate count was less than 2 - reject')
            return [plugins['reject']]
        elif alert.severity not in ['informational']:
            print('\n\nAlert severity was not informational - reject, telegram')
            return [plugins['reject'], plugins['telegram']]
        else:
            print('\n\nGot to first else - reject')
            return [plugins['reject']]
    else:
        print('\n\nGot to second else - reject')
        return [plugins['reject']]