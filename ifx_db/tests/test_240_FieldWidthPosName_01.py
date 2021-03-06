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

  def test_240_FieldWidthPosName_01(self):
    obj = IfxDbTestFunctions()
    obj.assert_expect(self.run_test_240)

  def run_test_240(self):
    conn = ifx_db.connect(config.ConnStr, config.user, config.password)
    
    result = ifx_db.exec_immediate(conn, "select * from sales")
    result2 = ifx_db.exec_immediate(conn, "select * from staff")
    result3 = ifx_db.exec_immediate(conn, "select * from emp_photo")
    
    for i in range(0, ifx_db.num_fields(result)):
      print str(i) + ":" + str(ifx_db.field_width(result,i))
    
    print "\n-----"
    
    for i in range(0, ifx_db.num_fields(result2)):
      print str(i) + ":" + str(ifx_db.field_width(result2,ifx_db.field_name(result2,i)))
          
    print "\n-----"
    
    for i in range(0, 3):
      print str(i) + ":" + str(ifx_db.field_width(result3,i)) + "," + str(ifx_db.field_display_size(result3,i))
    
    print "\n-----"
    print "region:%s" % ifx_db.field_type(result,'region')
    
    print "5:%s" % ifx_db.field_type(result2,5)

#__END__
#__LUW_EXPECTED__
#0:10
#1:15
#2:15
#3:11
#
#-----
#0:6
#1:9
#2:6
#3:5
#4:6
#5:9
#6:9
#
#-----
#0:6,6
#1:10,10
#2:1048576,2097152
#
#-----
#region:False
#5:decimal
#__ZOS_EXPECTED__
#0:10
#1:15
#2:15
#3:11
#
#-----
#0:6
#1:9
#2:6
#3:5
#4:6
#5:9
#6:9
#
#-----
#0:6,6
#1:10,10
#2:1048576,2097152
#
#-----
#region:False
#5:decimal
#__SYSTEMI_EXPECTED__
#0:10
#1:15
#2:15
#3:11
#
#-----
#0:6
#1:9
#2:6
#3:5
#4:6
#5:9
#6:9
#
#-----
#0:6,6
#1:10,10
#2:1048576,2097152
#
#-----
#region:False
#5:decimal
#__IDS_EXPECTED__
#0:10
#1:15
#2:15
#3:11
#
#-----
#0:6
#1:9
#2:6
#3:5
#4:6
#5:9
#6:9
#
#-----
#0:6,6
#1:10,10
#2:2147483647,-2
#
#-----
#region:string
#5:decimal
