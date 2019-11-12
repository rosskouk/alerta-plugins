# Alerta plugin routing rules

# Ensure alerts have occurred at least 3 time and are not informational before alerting
def rules(alert, plugins):

    if alert.duplicate_count <= 2:
        return [plugins['reject']]
    elif alert.severity not in ['informational']:
        return [plugins['reject'], plugins['telegram']]
    else:
        return [plugins['reject']]