from emp import Employee

def test_cons():
    ob=Employee("Joey",90000)
    assert ob.name=="Joey"
    assert ob.salary==90000

def test_sal():
    ob=Employee("Joey",90000)
    
    assert ob.increment_salary(500)== 90500

def test_changename():
    ob=Employee("Joey",90000)
    ob.change_name("Ken Adams")
    assert ob.name=="Ken Adams"