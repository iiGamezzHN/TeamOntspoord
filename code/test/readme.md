In deze folder staan alle test codes, zodat de folder <i>code</i> overzichtelijk blijft

Je hebt deze code al:

parent_dir_name = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(parent_dir_name+"\\"+located_map+"\\code")

Voeg deze regel toe (hiermee kan je ook bestanden vanuit de folder <i>test</i> gebruiken in je main)
sys.path.append(parent_dir_name+"\\"+located_map+"\\code\\test")
