
from ifx_db import *

ConStr = "SERVER=ids0;DATABASE=db1;HOST=127.0.0.1;PROTOCOL=onsoctcp;SERVICE=9088;UID=TestUser1;PWD=MySimplePass1;"
conn = ifx_db.connect( ConStr, "", "")

sql = "SELECT * FROM t1"
stmt = ifx_db.exec_immediate(conn, sql)
dictionary = ifx_db.fetch_both(stmt)
while dictionary != False:
    print( "c1 is : ",  dictionary["c1"] )
    print( "c2 is : ", dictionary[1] )
    print( "c3 is : ", dictionary["c3"] )
    print( "c4 is : ", dictionary["c4"] )
    print( "Going for next rec" )
    dictionary = ifx_db.fetch_both(stmt)

print( "Done" )
