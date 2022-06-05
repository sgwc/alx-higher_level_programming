#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
   len_a = len(tuple_a)
   len_b = len(tuple_b)
  
   if len_a == 0:
       a, b = 0, 0
   elif len_a == 1:
       a = tuple_a[0]
       b = 0
   else:
       a, b = tuple_a


   if len_b == 0:
       c, d = 0, 0
   elif len_b == 1:
       c = tuple_b[0]
       d = 0
   else:
       c, d = tuple_b

   res_tuple = (a + c, b + d)
   return(res_tuple)

