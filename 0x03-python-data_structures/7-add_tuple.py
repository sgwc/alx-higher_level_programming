#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
   len_a = len(tuple_a)
   len_b = len(tuple_b)
  
   if len_a == 0:
       a, b = 0, 0
   elif len_a == 1:
      a = tuple_a[0]
      b = 0
   elif len_a == 2:
       a, b = tuple_a
   else:
       a = tuple_a[0]
       b = tuple_a[1]

   if len_b == 0:
       c, d = 0, 0
   elif len_b == 1:
       c = tuple_a[0]
       d = 0
   elif len_b == 2:
       c, d = tuple_b
   else:
       c = tuple_b[0]
       d = tuple_b[1]

   res_tuple = (a + c, b + d)
   return(res_tuple)
