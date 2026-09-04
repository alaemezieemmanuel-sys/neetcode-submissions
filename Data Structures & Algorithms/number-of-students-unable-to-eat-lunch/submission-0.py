class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        sandwich = sandwiches[0]
        if len(students) == 0:
                return 0
        while sandwich in students:
            student = students.pop(0)
            if sandwich == student:
                sandwiches.pop(0)
                if len(sandwiches) > 0:
                    sandwich = sandwiches[0]
            else:
                students.append(student)
        return len(students)

        