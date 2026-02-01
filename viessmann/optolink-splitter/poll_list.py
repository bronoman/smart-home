'''
Original: Copyright 2026 philippoo66
'''
# use with Viessmann 
#Gerät		ID	Protokoll	Produktname		Bemerkungen
#V200KW2	2098	KW		Vitotronic 200 (KW2)	Witterungsgeführte Kessel- u. Heizkreisregelung für gleitend abgesenkte Kesselwassertemperatur mit Regelung für 1 Heizkreis mit Mischer

# Datapoint Polling List +++++++++
poll_interval = 30 
# Polling interval (seconds), 0 for continuous, -1 to disable (default: 30)
poll_items = [     
# Datapoints defined here will be polled; ignored if poll_list.py is found in the working directory
# ([PollCycle,] Name, DpAddr, Length [, Scale/Type [, Signed]]),
# PollCycle:   Optional entry to allow the item to be polled only every x-th cycle
# Name:        Datapoint name, published to MQTT as {dpname}; Best practices recommendation: Always use lowercase Names for consistency and compatibility.
# DpAddr:      Address used to read the datapoint value (hex with '0x' or decimal)
# Length:      Number of bytes to read
# Scale/Type:  Optional; if omitted, value returns as a hex byte string without '0x'. See Wiki for details
# Signed:      Numerical data will interpreted as signed (True) or unsigned (False, default is False if not explicitly set)

#Confirmed (on display) for Vitotronic 200 KW 2 and Vitola 100
("kesseltemperatur_ist",          "0x0810", 2, 0.1, True),   # actual temp of furnace
("ww_speicher_ist",               "0x0804", 2, 0.1, True),   # warm water actual temp
("ww_speicher_soll",              "0x6300", 1, 1),           # warm water target temp
("normale_raumtemperatur_soll",   "0x2306", 1, 1),           # room temp target

("brenner_status",                "0x5521", 1),              # state of burner (00=OFF, 01=ON)
("speicherpumpe_status",          "0x0845", 1),              # state of storage pump (00=OFF, 01=ON)
("zirkulationspumpe_status",      "0x0846", 1),              # state of circulation pump (00=OFF, 01=ON)
("heizpumpe_status",              "0x2906", 1),              # state of heating pump (00=OFF, 01=ON)

# Vorlauf / Rücklauf – re-add the one that was ~50 °C (likely Rücklauf)
("vorlauf_hk1_ist",             "0x0812", 2, 0.1, True),     # Previous ~50 °C  - highly likely
#("vorlauf_hk1_ist",               "0x0811", 2, 0.1, True),   # wrong  ( ~36 °C did not appears)

# Frostschutz – last attempts
#("frostschutz_soll",              "0x2302", 1, 1),           # returns zero - not correct
("reduzierte_raum_soll",          "0x2307", 1, 1),             # Reduced room = frost in many KW2, frost on disply at 3 deg, needs investigation

# Betriebsart / Programm – code-based (not binary)
("betriebsart_global",            "0x2000", 1)               # Likely 30 = Heizen + WW
#("betriebsart_heizkreis",         "0x2300", 1),               # 0x2300 often overall mode - returns 00, likely irrellevant
#("heizkreis_1_status",            "0x2304", 1),               # HK1 Radiator – could be ok
#("heizkreis_2_status",            "0x3304", 1),               # HK2 Fußboden - not ok in combination with HK1

]
