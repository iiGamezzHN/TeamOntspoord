class Station:
  def __init__(self, name, n_connections, critical):
      self.name = name
      self.n_connections = n_connections
      self.critical = critical

class Connection:
  def __init__(self, station1, station2, length, critical, latitude, longitude):
      self.station1 = station1
      self.station2 = station2
      self.length = length
      self.critical = critical
      self.latitude = latitude
      self.longitude = longitude
