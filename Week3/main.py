import torch
import count_activation_function
import profile
import stack, queue

if __name__ == '__main__':
    print('Ex1: ')
    data = torch.Tensor([1, 2, 3])
    softmax = count_activation_function.Softmax()
    output = softmax(data)
    print(output)
    new_data = torch.Tensor([1, 2, 300000000])
    output = softmax(new_data)
    print(output)

    data = torch.Tensor([5, 2, 4])
    softmax_stable = count_activation_function.SoftmaxStable()
    output = softmax_stable(data)
    print(output)
    new_data = torch.Tensor([1, 2, 300000000])
    output = softmax_stable(new_data)
    print(output)

    print('Ex2: ')
    student1 = profile.Student(name="studentA", yob=2010, grade="7")
    teacher1 = profile.Teacher(name="teacherA", yob=1969, subject="Math")
    teacher2 = profile.Teacher(name="teacherB", yob=1995, subject="History")
    doctor1 = profile.Doctor(name="doctorA", yob=1945,
                             specialist="Endocrinologists")
    doctor2 = profile.Doctor(name="doctorB", yob=1975,
                             specialist="Cardiologists")
    ward1 = profile.Ward(name="Ward1")
    ward1.add_person(student1)
    ward1.add_person(teacher1)
    ward1.add_person(teacher2)
    ward1.add_person(doctor1)
    ward1.add_person(doctor2)
    print(ward1.count_doctor())

    print("Ex3: ")
    stack1 = stack.MyStack(capacity=5)
    stack1.push(1)
    assert stack1.is_full() == False
    stack1.push(2)
    print(stack1.top())

    print("Ex4: ")
    queue1 = queue.MyQueue(capacity=5)
    queue1.enqueue(1)
    assert queue1.is_full() == False
    queue1.enqueue(2)
    print(queue1.front())