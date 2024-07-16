few_shots = [
    {'Question' : "how many 1p tablets are there?",
     'SQLQuery' : "SELECT count(*) FROM devices WHERE category = '1P' AND type = 'Tablet'",
     'SQLResult': "Result of the SQL query",
     'Answer' : '147'},
    {'Question': "how many Multi modal devices are there?",
     'SQLQuery':"SELECT count(*) FROM devices WHERE type = 'Multi modal'",
     'SQLResult': "Result of the SQL query",
     'Answer': '98'},
    {'Question': "how many accessories type is there?" ,
     'SQLQuery' : """SELECT COUNT(*) FROM devices WHERE type = 'Accessories'""",
     'SQLResult': "Result of the SQL query",
     'Answer': '7'} ,
     {'Question' : "how many none devices are there?" ,
      'SQLQuery': "SELECT count(*) FROM devices WHERE type = 'None'",
      'SQLResult': "Result of the SQL query",
      'Answer' : '0'},
    {'Question': "Who is the manager for bishop?",
     'SQLQuery' : "SELECT manager FROM devices WHERE model = 'bishop'",
     'SQLResult': "Result of the SQL query",
     'Answer' : 'vivek'
     }
]