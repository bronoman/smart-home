# re-use settings_ini-py.example

# additional by matt
SERIAL_BAUDRATE = 4800
SERIAL_PARITY = 'E'     # 'E' for even, 'N' for none
SERIAL_STOPBITS = 2

# add-on by matt to have LWT topic published despite running a service
# Force LWT settings (add or change these lines)
MQTT_LWT_TOPIC    = "Vito/LWT"
MQTT_LWT_ONLINE   = "online"
MQTT_LWT_OFFLINE  = "offline"
MQTT_LWT_QOS      = 1
MQTT_LWT_RETAINED = True
