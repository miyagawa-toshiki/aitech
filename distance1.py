def distance(lat1, lon1, lat2, lon2): #lat : 緯度　lon : 経度
  si_ta = math.fabs(lat2 - lat1)
  foi = math.fabs(lon2 - lon1)
  angle = math.sqrt(np.sin(si_ta/2)*np.sin(si_ta/2) + np.cos(lat1) * np.cos(lat2) * np.sin(foi/2) * np.sin(foi/2))
  distant = 2 * math.asin(angle)
  return distant
def move_time(lat1, lon1, lat2, lon2, speed): #lat : 緯度　lon : 経度
  si_ta = math.fabs(lat2 - lat1)
  foi = math.fabs(lon2 - lon1)
  angle = math.sqrt(np.sin(si_ta/2)*np.sin(si_ta/2) + np.cos(lat1) * np.cos(lat2) * np.sin(foi/2) * np.sin(foi/2))
  distant = 2 * math.asin(angle)
  time = distant / speed
  return time