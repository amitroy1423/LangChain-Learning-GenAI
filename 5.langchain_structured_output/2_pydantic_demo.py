from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class Student(BaseModel):

    name: str = 'nitish'
    age: Optional[int] = None
    email: EmailStr
    cgpa: float = Field(gt=0, lt=10, default=5, description='A decimal value representing the cgpa of the student')


new_student = {'age':'32', 'email':'abc@gmail.com'}

student = Student(**new_student)

student_dict = dict(student)

print(student_dict['age'])

student_json = student.model_dump_json()

# Coercesion of the age field from string to integer is handled by Pydantic's type validation and coercion. When the Student model is instantiated with the new_student dictionary, Pydantic automatically converts the string '25' to an integer for the age field, as specified in the model definition.

#Fileld validation is performed by Pydantic based on the type hints and constraints defined in the model. For example, the cgpa field has a constraint that it must be greater than 0 and less than 10. If a value outside this range is provided, Pydantic will raise a validation error.Field descriptions are provided using the Field function, which allows for additional metadata to be associated with each field. This can be useful for documentation and validation purposes.