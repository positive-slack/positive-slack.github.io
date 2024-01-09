Title: Design Patterns in SystemVerilog OOP: Fundamentals
Date: 2024-01-08
Category: Verification
Tags: systemverilog, oop, design_patterns
Slug: 2024-01-08-design-patterns-sv-oop-fundamentals
Status: published
Series: Design Patterns in SystemVerilog OOP
Series_index: 1
Summary: Overview of the key OOP possibilities of SystemVerilog and introduction of design patterns.

[TOC]

## Foreword for the series
At some point any programmer goes through this - finally start reading something solid about [design patterns](https://en.wikipedia.org/wiki/Design_Patterns) they might have heard a lot about. This happened to me eventually, so I want to start new post series "Design Patterns in SystemVerilog OOP" and share my reflection and thoughts on this topic. Of course, this is from the perspective of SystemVerilog.

How this can be useful for verification engineer? Actually, verification is the process of writing software. So, generally it is good to understand and be aware of all key concepts of programmers world simply to be a better engineer. This is even more important for engineers who came into this field from hardware (RTL design, physical design, embedded, etc.).

But before making a deep dive into patterns I want to make a solid ground and overview all the key OOP concepts and how SystemVerilog supports them. Maybe it will look a bit too basic and oversimplified, but sometimes it is useful even for experienced seniors to look back and review fundamentals one more time, isn't it?

## Classes, objects and handles
The fundamental concept in SV OOP is the `class`. Usually, it is a container for data, called *properties* (aka *attributes*/*fields*), and task and functions known as *methods*. Properties and methods are *members* of a class.

Instance of a `class` is called *object*. To create an object you need to call a special method `new()` known as *constructor*. However, there is no way in SV to explicitly destroy an object via any *destructor* method.

*Object handle* is a kind of safe pointer to an object, that can be represented as a variable. No arithmetic operations can be performed on it. Handle can be empty, storing a `null` value, or it can refer a concrete object in a memory.

You can refer an object itself and its internals using `this` keyword within a class.

```verilog
class foo;
  string id;

  function new(string id);
    this.id = id;
  endfunction : new
endclass

initial begin
  // you need always create objects explicitly
  foo foo_obj = new("fooooo");
  // foo_obj handle now refers to created object
  $display(foo_obj.id);
end
```

### Automatic and static members
Normally, all objects have their own independent copy of all members - they are `automatic` by default. In the example above, both objects have unique `id`.
However, if qualifier `static` is used, then the same variable is used for all objects.
Almost all static variables are initialized at runtime before time 0, and some trick effect called *"static variable initialization order fiasco"* may arise. I will elaborate on this in the further posts.

Almost the same for methods. By default, they all are `automatic`, but can be converted to static via the same qualifier. However, static methods have some things to remember:

- they cannot be `virtual`
- they can access only `static` members
- they can be called on class name via scope resolution operator `::`

```verilog
class bar;
  static int cnt;

  function new();
    // increment every time new object is constructed
    this.cnt += 1;
  endfunction

  static function int get_cnt();
    return this.cnt;
  endfunction
endclass

initial begin
  bar bar_0 = new();
  bar bar_1 = new();
  $display(bar_0.cnt);        // prints 2
  $display(bar_1.get_cnt());  // also prints 2
  $display(bar::get_cnt());   // again prints 2
end
```

## Inheritance
At some point you may want to extend fields or override methods of an original class. This is how code reuse in OOP works.
Special keyword `extends` allows to *inherit* all the underlying structure of a *base*/*super*/*parent* class.  Newly created class usually known as *extended*/*derived*/*child* class.

```verilog
class foo;
  string id;

  function new(string id);
    this.id = id;
  endfunction : new
endclass

class bar extends foo;
  int counter; // new field
  function new(string id);
    super.new(id);
  endfunction : new
endclass
```

Derived classes form an *inheritance tree*, where base class is a *root*.
[Multiple inheritance](https://dvcon-proceedings.org/wp-content/uploads/the-problems-with-lack-of-multiple-inheritance-in-systemverilog-and-a-solution.pdf), when derived class has several parents at a time, doesn't exist in SV as well as ["the diamond problem"](https://en.wikipedia.org/wiki/Multiple_inheritance#The_diamond_problem). However, some patterns allow to emulate this feature (avoiding the problem though).

## Encapsulation
This concept allows restricting access to class internals, in order to hide some sensitive data, state and other details from external world.
SV provides several qualifiers for this:

- `local` - item is accessible only within current class,
- `protected` - item become accessible from derived classes too.

By default, all fields/methods are public and can be accessed by anyone externally/internally.

```verilog
class foo;
  local string a; // only this.a is allowed
  protected string b; // can be accessed within any child too
  string c; // public

  local function secret_f(); endfunction // only for this
  protected function internal_f(); endfunction // for this and any derived
  function public_f(); endfunction // for any
endclass
```

The main goal of this is to prevent user from relying or making incorrect assumptions on class internals, which can be a subject of change.

## Polymorphism
Polymorphism allows running the same code over different objects, making code more reusable, reliable and maintainable. A lot of SV features serve this concept:

- *type casting*
- *virtual methods*
- *parametrized classes*

### Type casting
One thing about object handle, which hasn't been mentioned, that it can refer not only to objects of its class, but to objects of any derived classes too. Operations of moving object references around handles of different types called *casting*. There are two different types of casting:

- *up-casting* - cast to parent (or in base class direction), implicit via assignment;
- *down-casting* - cast to child class (or in derived class direction), explicit via  `$cast(target, source)`.

```verilog
class animal; endclass
class cat extends animal; endclass
class dog extends animal; endclass
class husky extends dog; endclass

initial begin
  // declare handles
  animal animal_h; // is null, but can handle any animal
  cat    cat_h;    // is null, but can handle any cat
  dog    dog_h;    // is null, but can handle any dog
  husky  husky_h;  // is null, but can handle only husky

  // construct objects - handles will store references
  cat_h   = new(); // construct `cat` object and put reference to handle
  husky_h = new(); // construct `husky` object and put reference to handle

  // up-casting is implicit - just assign to handle of parent class
  animal_h = cat_h;   // both handles refer the same object
  animal_h = husky_h; // make it refers to a different object
  //cat_h = husky_h;    // compilation error! different inheritance branches

  // down-casting is explicit - via system call $cast(target, source)
  // `animal_h` stores reference to `husky` object
  $cast(husky_h, animal_h); // `husky` object can be casted to `husky`
  $cast(dog_h, animal_h);   // `husky` object can be casted to `dog` too
  if (!$cast(cat_h, animal_h)) begin // catch runtime error
    $display("Can't cast husky to cat!");
  end
end
```

### Virtual methods
By default, class methods are non-virtual, but if qualifier `virtual` is added to a method declaration, then method becomes virtual in this and all derived classes.
Main differences:

- *non-virtual* - signature (number, names, types of arguments and return type) may be different in child class and method of handle class is always called, even it stores reference to child class object;
- *virtual* - signature must be the same in all derived classes and method of specific object is called, even handle is parent class.

```verilog
class cat;
  function purr();
    $display("purrrrrr");
  endfunction

  virtual function roar();
    $display("*keeping silence*");
  endfunction
endclass : cat

class domestic_cat extends cat;
  function int purr(string sound); // different signature
    $display(sound);
    return -1;
  endfunction

  virtual function roar(); // override virtual
    $display("meow");
  endfunction
endclass : domestic_cat

class lion extends cat;
  function purr();
    $display("*nope, going to eat you*");
  endfunction

  virtual function roar(); // override virtual
    $display("grraaaauuuu");
  endfunction
endclass : lion

initial begin
  domestic_cat kitty = new();
  lion simba = new();
  cat cats[] = '{kitty, simba};
  foreach(cats[i]) begin
    cats[i].purr(); // always "purrrrr" - non-virtual
    cats[i].roar(); // depends on object implementation - virtual
  end
end
```

### Parametrized classes
Class declaration supports generalization via parameters as SV `module`, `interface`, etc. do. This also  can be viewed as a form of polymorphism.

In other programming languages such classes may be referred as *generic classes*, but this feature usually only involves *generic types* or *generics*. In SV, in its turn, parameters can be either types or values (constants).
When you refer such class with concrete parameters you create *class specialization*. This specialized class is an unique type.

```verilog
class packet #(type PAYLOAD_T, int LENGTH);
  PAYLOAD_T payload [LENGTH];
endclass

// all these are unique types
typedef packet#(string, 1) str_pkt_t;
typedef packet#(real, 3) real_arr_pkt_t;
class bytes_pkt extends packet#(byte, 8); endclass
```

## Abstraction
It is the last key OOP concept left. Abstraction is focused on what the object represents or can do, ignoring the specific details of how it performs its functions.
The main goal of abstraction is to handle complexity by simplifying the user's interaction with the object.

In practice, abstraction is achieved through the use of abstract data types, focusing on the major operations and characteristics of an object without diving into the details of implementation. These data types are defined by abstract classes and interfaces (not SV `interface..endinterface` -- here and below interface is a term from programming field strictly).

#### Abstract classes
Class declared with `virtual` qualifier is called an *abstract class*. This class *cannot* be constructed, instead it is used as template, which user inherits and customizes. Such class outlines all the expected functionality, enforcing some kind of rules and borders for its subclasses.

Moreover, it allows to declare `pure virtual` methods, which are only method prototypes and usually called *abstract methods*. These methods *must* be implemented within child classes. In all other terms abstract classes are the same as non-abstract (*concrete*) classes - they can have fields, fully implemented methods (*concrete methods*), etc.

```verilog
virtual class animal;
  pure virtual function void make_sound();

  function void breathe();
    $display("I am breathing");
  endfunction
endclass

class dog extends animal;
  virtual function void make_sound();
    $display("bark");
  endfunction
endclass

class cat extends animal;
  virtual function void make_sound();
    $display("meow");
  endfunction
endclass

initial begin
  animal animals[string];
  dog the_dog = new();
  cat the_cat = new();

  //animals["unknown"] = new(); // compilation error
  animals["the_dog"] = the_dog;
  animals["the_cat"] = the_cat;
  foreach (animals[s]) begin
    animals[s].breathe();
    animals[s].make_sound();
  end
  $finish();
end
```

### Interface classes

Interface classes can be a topic for a separate article, so I'll try to be concise here.

Class declared with `interface` qualifier is called an *interface class*. Yes, it is quite unfortunate that "interface" word is overused in HDL world, so usually you have to emphasis that you are talking about concept from OOP. Nevertheless, interface class is used to define a set of methods without implementations.
This might look similar to abstract class - it also collects a bunch of abstract methods (`pure virtual`), but actually interface has a different purpose, more restrictions and special semantics.

Abstract class represents some kind of template for derived classes and express relation [*"is-a"*](https://en.wikipedia.org/wiki/Is-a). Interface represents a functional contract, that *implementer* must follow, and express relation *"can-do"*.  And here we come to a next thing that interface is *implemented* by a class (not derived). Special SV keyword `implements` must be used. A class can implement multiple interfaces at once.

One more thing to note for interface classes is that they are *stateless*, i.e. can not have any data properties, only abstract methods, types and SV parameters.

```verilog
interface class Courier;
  pure virtual function deliver();
endclass

class Person implements Courier;
  virtual function deliver();
    $display("Doing slow delivery");
  endfunction
endclass

class Vehicle; endclass
class Car extends Vehicle implements Courier;
  virtual function deliver();
    $display("Doing fast delivery");
  endfunction
endclass

function do_delivery(Courier courier);
  courier.deliver();
endfunction

initial begin
  Car truck = new();
  do_delivery(truck); // any with Courier interface
  $finish();
end
```

## Design patterns
Okay, here we go. Programmers use all this fancy OOP concepts to create testbenches, software and other applications. Interesting thing though, that despite having domains and programs of all colors and shapes, having freedom to organize classes and their interactions in all thinkable ways, engineers encounter quite similar underlying problems over and over again. Moreover, they invent quite similar solutions independently.

Some sharp minds in the past analyzed and identified a lot of common problems, and formalized generic solutions. And this was something bigger than just snippets of code for the specific language -- rather catalog of ideas or *patterns* to detect problems and solve it in a common way.

I am talking about the classic -- "Design Patterns" by the "Gang of Four": Erich Gamma, Richard Helm, Ralph Johnson, John Vlissides. It is generally known as the "GoF book". All the patterns I want to describe in this series (excluding some SV specific) were originated in this book.

And the last thing you need to consider about design patterns: they are useful, they are everywhere, but they are neither ["silver bullet"](https://en.wikipedia.org/wiki/Silver_bullet) or ["golden hammer"](https://sourcemaking.com/antipatterns/golden-hammer). If you bend your architecture only to fit some specific pattern whatever it takes or just because you like it, possibly you do the wrong job.

## References and further reading
- [Design Patterns - Erich Gamma, Richard Helm, Ralph Johnson, John Vlissides](https://www.google.ru/books/edition/Design_Patterns/tmNNfSkfTlcC)
- [A short course on SystemVerilog classes for UVM verification - Dave Rich](https://www.edn.com/a-short-course-on-systemverilog-classes-for-uvm-verification/)
- [Inheritance and polymorphism of SystemVerilog OOP for UVM verification - Dave Rich](https://www.edn.com/inheritance-and-polymorphism-of-systemverilog-oop-for-uvm-verification/)
- [The Problems with Lack of Multiple Inheritance in SystemVerilog and a Solution - Dave Rich](https://dvcon-proceedings.org/wp-content/uploads/the-problems-with-lack-of-multiple-inheritance-in-systemverilog-and-a-solution.pdf)
- [SystemVerilog Standard 2017 IEEE.1800-2017-SystemVerilog](https://ieeexplore.ieee.org/document/8299595): Chapter 8 Classes
