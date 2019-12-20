class People:
	def __init__(self, name, age, weight):
		self.name = name
		self.age = age
		self.__weight = weight
	
	def speak(self):
		print("{}说: 我今年{}岁了，体重{}千克".format(self.name, self.age,self.__weight))


class Student(People):
	def __init__(self, name, age, weight, grade):
		People.__init__(self, name, age, weight)
		self.grade = grade
	
	def speak(self):
		print("{}说：我{}岁了，我在读{}年级。".format(self.name, self.age, self.grade))


class Speaker:
	def __init__(self, name, topic):
		self.name = name
		self.topic = topic
	
	def speak(self):
		print("我叫{}，我演讲的主题是{}。".format(self.name, self.topic))


class Sample(Speaker, Student):
	def __init__(self, name, age, weight, grade, topic):
		Student.__init__(self, name, age, weight, grade)
		Speaker.__init__(self, name, topic)


test = Sample('tim', 25, 80, 4, 'Python')
test.speak()

s = Student('lee', 10, 40, 3)
s.speak()
super(Student, s).speak()



