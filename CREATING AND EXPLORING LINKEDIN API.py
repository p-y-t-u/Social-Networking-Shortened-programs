import requests

r = requests.get(
    "https://api.linkedin.com/v2/me",
    headers={"Authorization": "Bearer AQX3U_WyXEm3CNVZ4X0v7GbL51Cqmci7Gby6-2IC4kOrvt3l9ZaNkldJIqYUKVadwbaXi1YCWxxT49b2lsLiGRcHS40wHxH60f1thonImE5Pm4i4l2_DXRk_n-WWQ1C9lDL6opHZLDX-qpBukFI9ckXo_bO7b-RMGltYfmcmNnHBEsoZ-yXTwInJXEao0Ke7Qwn44Sh4LJ4BFKzSPjfmc0vWoncbyf9aALtikepImLkILAnoPpr5t0G1-ihs6s_3QSljjHnk2O-V_jdOjgha7YCrrbz1vnrI3Fg7gifail300Oq1owWEuvCnNrHmZfjjEsi_ZPtHASiJqy8QWMSOkNdO6OUjBQ"})

print("User Profile Data:" if r.status_code == 200 else "Error:", 
      r.json() if r.status_code == 200 else r.text)
