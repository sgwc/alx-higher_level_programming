## Basic inheritance
Technically, every class we create uses inheritance. All Python classes are subclasses of the special class named object. This class provides very little in terms of data and behaviors (those behaviors it does provide are all double-underscore methods intended for internal use only), but it does allow Python to treat all objects in the same way.

If we don’t explicitly inherit from a different class, our classes will automatically inherit from object. However, we can openly state that our class derives from object using the following syntax:

```markup
class MySubClass(object):
 pass
```

This is inheritance! Since Python 3 automatically inherits from  _object_  if we don’t explicitly provide a different superclass. A  **superclass**, or parent class, is a class that is being inherited from. A  **subclass**  is a class that is inheriting from a superclass. In this case, the superclass is object, and  _MySubClass_  is the subclass. A subclass is also said to be  **derived**  from its parent class or that the subclass  **extends**  the parent.

As you’ve probably figured out from the example, inheritance requires a minimal amount of extra syntax over a basic class definition. Simply include the name of the parent class inside a pair of parentheses after the class name, but before the colon terminating the class definition. This is all we have to do to tell Python that the new class should be derived from the given superclass.

How do we apply inheritance in practice? The simplest and most obvious use of inheritance is to add functionality to an existing class. Let’s start with a simple contact manager that tracks the name and e-mail address of several people. The contact class is responsible for maintaining a list of all contacts in a class variable, and for initializing the name and address, in this simple class:

```markup
class Contact:
 all_contacts = []

def __init__(self, name, email):
self.name = name
self.email = email
Contact.all_contacts.append(self)
```

This example introduces us to class variables. The  _all_contacts_  list, because it is part of the class definition, is actually shared by all instances of this class. This means that there is only  **one**  _Contact.all_contacts_  list, and if we call  _self.all_contacts_  on any one object, it will refer to that single list. The code in the initializer ensures that whenever we create a new contact, the list will automatically have the new object added. Be careful with this syntax, for if you ever set the variable using  _self.all_contacts_, you will actually be creating a  **new**  instance variable on the object; the class variable will still be unchanged and accessible as  _Contact.all_contacts_.

This is a very simple class that allows us to track a couple pieces of data about our contacts. But what if some of our contacts are also suppliers that we need to order supplies from? We could add an  _order_  method to the  _Contact_  class, but that would allow people to accidentally order things from contacts who are customers or family friends. Instead, let’s create a new  _Supplier_  class that acts like a  _Contact_, but has an additional  _order_  method:

```markup
class Supplier(Contact):
 def order(self, order):
 print("If this were a real system we would send "
 "{} order to {}".format(order, self.name))
```

Now, if we test this class in our trusty interpreter, we see that all contacts, including suppliers, accept a name and e-mail address in their  ___init___, but only suppliers have a functional order method:

```markup
>>> c = Contact("Some Body", "somebody@example.net")
 >>> s = Supplier("Sup Plier", "supplier@example.net")
 >>> print(c.name, c.email, s.name, s.email)
 Some Body somebody@example.net Sup Plier supplier@example.net
 >>> c.all_contacts
 [<__main__.Contact object at 0xb7375ecc>,
 <__main__.Supplier object at 0xb7375f8c>]
 >>> c.order("Ineed pliers")
 Traceback (most recent call last):
 File "<stdin>", line 1, in <module>
 AttributeError: 'Contact' object has no attribute 'order'
 >>> s.order("I need pliers")
 If this were a real system we would send I need pliers order to
 Supplier
 >>>
```

So now our  _Supplier_  class can do everything a  _Contact_  can do (including adding itself to the list of  _all_contacts_) and all the special things it needs to handle as a supplier. This is the beauty of inheritance.

## Extending built-ins

One of the most interesting uses of this kind of inheritance is adding functionality to built-in classes. In the  _Contact_  class seen earlier, we are adding contacts to a list of all contacts. What if we also wanted to search that list by name? Well, we could add a method on the  _Contact_  class to search it, but it feels like this method actually belongs on the list itself. We can do this using inheritance:

```markup
class ContactList(list):
 def search(self, name):
 '''Return all contacts that contain the search value
 in their name.'''
 matching_contacts = []
 for contact in self:
 if name in contact.name:
 matching_contacts.append(contact)
 return matching_contacts

class Contact:
all_contacts = ContactList()

def __init__(self, name, email):
self.name = name
self.email = email
self.all_contacts.append(self)
```

Instead of instantiating a normal list as our class variable, we create a new  _ContactList_  class that extends the built-in list. Then we instantiate this subclass as our  _all_contacts_  list. We can test the new search functionality as follows:

```markup
>>> c1 = Contact("John A", "johna@example.net")
 >>> c2 = Contact("John B", "johnb@example.net")
 >>> c3 = Contact("Jenna C", "jennac@example.net")
 >>> [c.name for c in Contact.all_contacts.search('John')]
 ['John A', 'John B']
 >>>
```

Are you wondering how we changed the built-in syntax  _[]_  into something we can inherit from? Creating an empty list with  _[]_  is actually a shorthand for creating an empty list using list(); the two syntaxes are identical:

```markup
>>> [] == list()
 True
```

So, the  _list_  data type is like a class that we can extend, not unlike  _object_.

As a second example, we can extend the  _dict_  class, which is the long way of creating a dictionary (the  _{:}_  syntax).

```markup
class LongNameDict(dict):
 def longest_key(self):
 longest = None
 for key in self:
 if not longest or len(key) > len(longest):
 longest = key
 return longest
```

This is easy to test in the interactive interpreter:

```markup
>>> longkeys = LongNameDict()
 >>> longkeys['hello'] = 1
 >>> longkeys['longest yet'] = 5
 >>> longkeys['hello2'] = 'world'
 >>> longkeys.longest_key()
 'longest yet'
```

Most built-in types can be similarly extended. Commonly extended built-ins are  _object_,  _list_,  _set_,  _dict_,  _file_, and  _str_. Numerical types such as  _int_  and  _float_  are also occasionally inherited from.

## Overriding and super

So inheritance is great for adding new behavior to existing classes, but what about changing behavior? Our  _contact_  class allows only a name and an e-mail address. This may be sufficient for most contacts, but what if we want to add a phone number for our close friends?

We can do this easily by just setting a phone attribute on the contact after it is constructed. But if we want to make this third variable available on initialization, we have to  **override**  ___init___. Overriding is altering or replacing a method of the superclass with a new method (with the same name) in the subclass. No special syntax is needed to do this; the subclass’s newly created method is automatically called instead of the superclass’s method. For example:

```markup
class Friend(Contact):
 def __init__(self, name, email, phone):
 self.name = name
 self.email = email
 self.phone = phone
```

Any method can be overridden, not just  ___init___. Before we go on, however, we need to correct some problems in this example. Our  _Contact_  and  _Friend_  classes have duplicate code to set up the  _name_  and  _email_  properties; this can make maintenance complicated, as we have to update the code in two or more places. More alarmingly, our  _Friend_  class is neglecting to add itself to the  _all_contacts_  list we have created on the  _Contact_  class.

What we really need is a way to call code on the parent class. This is what the  _super_  function does; it returns the object as an instance of the parent class, allowing us to call the parent method directly:

```markup
class Friend(Contact):
 def __init__(self, name, email, phone):
 super().__init__(name, email)
 self.phone = phone
```

This example first gets the instance of the parent object using super, and calls  ___init___  on that object, passing in the expected arguments. It then does its own initialization, namely setting the  _phone_  attribute.

A  _super()_  call can be made inside any method, not just  ___init___. This means all methods can be modified via overriding and calls to  _super_. The call to super can also be made at any point in the method; we don’t have to make the call as the first line in the method. For example, we may need to manipulate the incoming parameters before forwarding them to the superclass.
https://hub.packtpub.com/inheritance-python/
