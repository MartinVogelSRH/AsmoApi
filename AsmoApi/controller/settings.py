import ConfigParser


def save():
    with open('Asmo.conf', 'wb') as config_file:
        configuration.write(config_file)
def defaultValues():
    #configuration = ConfigParser.SafeConfigParser()
    configuration.add_section('Server')
    configuration.set('Server','PORT','8080')
    configuration.add_section('Distance')
    configuration.set('Distance','TRIG_PIN','21')
    configuration.set('Distance','ECHO_PIN','20')
    configuration.set('Distance','MAX_DISTANCE','20')
    configuration.add_section('LED')
    configuration.set('LED','BLUE_PIN','13')
    configuration.set('LED','RED_PIN','19')
    configuration.set('LED','GREEN_PIN','26')
    configuration.add_section('Temperature')
    configuration.set('Temperature','DHT_PIN','4')
    save()

configuration = ConfigParser.SafeConfigParser()

try:
    #with open('Asmo.conf','r') as config_file:
    configuration.read('Asmo.conf')
    print(configuration.get('Server','port'))
except:
    defaultValues()

def setValues(newSettings):
    try:
        for section in newSettings:
            for setting in newSettings[section]:
                if configuration.has_section(section):
                    configuration.set(section,setting[0],setting[1])
                else:
                    configuration.add_section(section)
                    configuration.set(section,setting[0],setting[1])
        save()
        return 'Successfully changed the settings. Please restart the server to reload them.'
    except Exception as e:
        return e


