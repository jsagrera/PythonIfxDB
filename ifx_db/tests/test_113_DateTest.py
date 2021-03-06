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

  def test_113_DateTest(self):
    obj = IfxDbTestFunctions()
    obj.assert_expect(self.run_test_113)

  def run_test_113(self):
    conn = ifx_db.connect(config.ConnStr, config.user, config.password)
    
    if conn:
      drop = "DROP TABLE datetest"
      try:
        ifx_db.exec_immediate( conn, drop )
      except:
        pass
      
      create = "CREATE TABLE datetest ( id INTEGER, mydate DATE )"
      ifx_db.exec_immediate(conn, create)

      server = ifx_db.server_info( conn )
      if (server.DBMS_NAME[0:3] == 'IDS'):
        insert = "INSERT INTO datetest (id, mydate) VALUES (1,'1982-03-27')"
        ifx_db.exec_immediate(conn, insert)
        insert = "INSERT INTO datetest (id, mydate) VALUES (2,'1981-07-08')"
        ifx_db.exec_immediate(conn, insert)
      else:
        insert = "INSERT INTO datetest (id, mydate) VALUES (1,'1982-03-27')"
        ifx_db.exec_immediate(conn, insert)
        insert = "INSERT INTO datetest (id, mydate) VALUES (2,'1981-07-08')"
        ifx_db.exec_immediate(conn, insert)
      
      stmt = ifx_db.prepare(conn, "SELECT * FROM datetest")
      ifx_db.execute(stmt)

      result = ifx_db.fetch_row( stmt )
      while ( result ):
        row0 = ifx_db.result(stmt, 0)
        row1 = ifx_db.result(stmt, 1)
        print row0
        print row1
        result = ifx_db.fetch_row( stmt )
    else:
      print "Connection failed."

#__END__
#__LUW_EXPECTED__
#1
#1982-03-27
#2
#1981-07-08
#__ZOS_EXPECTED__
#1
#1982-03-27
#2
#1981-07-08
#__SYSTEMI_EXPECTED__
#1
#1982-03-27
#2
#1981-07-08
#__IDS_EXPECTED__
#1
#1982-03-27
#2
#1981-07-08
