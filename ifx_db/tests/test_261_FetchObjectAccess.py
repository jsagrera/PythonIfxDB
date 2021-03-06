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

  def test_261_FetchObjectAccess(self):
    obj = IfxDbTestFunctions()
    obj.assert_expect(self.run_test_261)

  def run_test_261(self):
    conn = ifx_db.connect(config.ConnStr, config.user, config.password)
    
    server = ifx_db.server_info( conn )
    if (server.DBMS_NAME[0:3] == 'IDS'):
      op = {ifx_db.ATTR_CASE: ifx_db.CASE_UPPER}
      ifx_db.set_option(conn, op, 1)

    if (server.DBMS_NAME[0:3] == 'IDS'):
      sql = "SELECT breed, TRIM(TRAILING FROM name) AS name FROM animals WHERE id = ?"
    else:
      sql = "SELECT breed, RTRIM(name) AS name FROM animals WHERE id = ?"

    if conn:
      stmt = ifx_db.prepare(conn, sql)
      ifx_db.execute(stmt, (0,))

#      NOTE: This is a workaround
#      function fetch_object() to be implemented...
#      pet = ifx_db.fetch_object(stmt)
#      while (pet):
#          print "Come here, %s, my little %s!" % (pet.NAME, pet.BREED)
#          pet = ifx_db.fetch_object(stmt)
      
      class Pet:
          pass
      
      data = ifx_db.fetch_assoc(stmt)
      while ( data ):
         pet = Pet()
         pet.NAME = data['NAME']
         pet.BREED = data['BREED']
         print "Come here, %s, my little %s!" % (pet.NAME, pet.BREED)
         data = ifx_db.fetch_assoc(stmt)
         
      ifx_db.close(conn)
      
    else:
      print "Connection failed."

#__END__
#__LUW_EXPECTED__
#Come here, Pook, my little cat!
#__ZOS_EXPECTED__
#Come here, Pook, my little cat!
#__SYSTEMI_EXPECTED__
#Come here, Pook, my little cat!
#__IDS_EXPECTED__
#Come here, Pook, my little cat!
