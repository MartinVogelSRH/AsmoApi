import ConfigParser



def defaultValues():
    #asmo_config = ConfigParser.SafeConfigParser()
    asmo_config.add_section('Server')
    asmo_config.set('Server','PORT','8080')
    asmo_config.add_section('Distance')
    asmo_config.set('Distance','TRIG_PIN','21')
    asmo_config.set('Distance','ECHO_PIN','20')
    asmo_config.set('Distance','MAX_DISTANCE','20')
    asmo_config.add_section('LED')
    asmo_config.set('LED','BLUE_PIN','13')
    asmo_config.set('LED','RED_PIN','13')
    asmo_config.set('LED','GREEN_PIN','13')
    asmo_config.add_section('Temperature')
    asmo_config.set('Temperature','DHT_PIN','4')
    with open('Asmo.conf', 'wb') as config_file:
        asmo_config.write(config_file)

asmo_config = ConfigParser.SafeConfigParser()

try:
    #with open('Asmo.conf','r') as config_file:
    asmo_config.read('Asmo.conf')
    print(asmo_config.get('Server','port'))
except:
    defaultValues()



