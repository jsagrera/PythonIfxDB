# 
#  Licensed Materials - Property of IBM
#
#  (c) Copyright IBM Corp. 2007-2008
#

import unittest, sys
import ifx_db
import config
from testfunctions import IfxDbTestFunctions

class IfxDbTestCase(unittest.TestCase):

  def test_142_BindParamSelectStmtMultipleParams_02(self):
    obj = IfxDbTestFunctions()
    obj.assert_expect(self.run_test_142)

  def run_test_142(self):
    sql = "SELECT id, breed, name, weight FROM animals WHERE weight < ? AND weight > ?"
    
    conn = ifx_db.connect(config.ConnStr, config.user, config.password)
    
    if conn:
      stmt = ifx_db.prepare(conn, sql)
    
      weight = 200.05
      mass = 2.0
      
      ifx_db.bind_param(stmt, 1, weight, ifx_db.SQL_PARAM_INPUT)
      ifx_db.bind_param(stmt, 2, mass, ifx_db.SQL_PARAM_INPUT)
    
      result = ifx_db.execute(stmt) 
      if ( result ):
        row = ifx_db.fetch_tuple(stmt)
        while ( row ):
          #row.each { |child| print child }
          for i in row:
            print i
          row = ifx_db.fetch_tuple(stmt)
      ifx_db.close(conn)
    else:
      print "Connection failed."

#__END__
#__LUW_EXPECTED__
#0
#cat
#Pook            
#3.20
#1
#dog
#Peaches         
#12.30
#5
#goat
#Rickety Ride    
#9.70
#6
#llama
#Sweater         
#150.00
#__ZOS_EXPECTED__
#0
#cat
#Pook            
#3.20
#1
#dog
#Peaches         
#12.30
#5
#goat
#Rickety Ride    
#9.70
#6
#llama
#Sweater         
#150.00
#__SYSTEMI_EXPECTED__
#0
#cat
#Pook            
#3.20
#1
#dog
#Peaches         
#12.30
#5
#goat
#Rickety Ride    
#9.70
#6
#llama
#Sweater         
#150.00
#__IDS_EXPECTED__
#0
#cat
#Pook            
#3.20
#1
#dog
#Peaches         
#12.30
#5
#goat
#Rickety Ride    
#9.70
#6
#llama
#Sweater         
#150.00
