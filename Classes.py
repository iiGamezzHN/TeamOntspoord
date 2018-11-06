class Station:
  def __init__(self, name, n_connections, critical, latitude, longitude):
      self.name = name
      self.n_connections = n_connections
      self.critical = critical
      self.latitude = latitude
      self.longitude = longitude

class Connection:
  def __init__(self, station1, station2, length, critical):
      self.station1 = station1
      self.station2 = station2
      self.length = length
      self.critical = critical
