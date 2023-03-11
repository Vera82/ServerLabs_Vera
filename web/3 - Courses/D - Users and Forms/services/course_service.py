from decimal import Decimal as dec
from typing import List 

from data.models import Course

def course_count() -> int:
    return 99
#:

def available_courses(count: int) -> List[Course]:
    return [
        Course(
            id = 1,
            category = 'Hotelaria e Turismo',
            price = dec(169),
            name = 'Gestor Turístico',
            summary = 'Et architecto provident deleniti facere repellat nobis iste. Id facere quia quae dolores dolorem tempore.',
            description = 'Et architecto provident deleniti facere repellat nobis iste. Id facere quia quae dolores dolorem tempore.',
            trainer_id = 1,
            trainer_name = 'Osmar', 
            schedule = 'Segundas e Quintas, 17 às 20h',
            available_seats = 40,
        ),
        Course(
            id = 2,
            category = 'Programação em C++',
            price = dec(250),
            name = 'Estruturas de Dados em C++',
            summary = 'Et architecto provident deleniti facere repellat nobis iste. Id facere quia quae dolores dolorem tempore.',
            description = 'Et architecto provident deleniti facere repellat nobis iste. Id facere quia quae dolores dolorem tempore.',
            trainer_id = 4,
            trainer_name = 'Bernardo',
            schedule = 'Terças e Quartas, 17h30 às 20h30',
            available_seats = 20,
        ),
            Course(
            id = 3,
            category = 'Natação',
            price = dec(250),
            name = 'Estilo Borboleta',
            summary = 'Et architecto provident deleniti facere repellat nobis iste. Id facere quia quae dolores dolorem tempore.',
            description = 'Et architecto provident deleniti facere repellat nobis iste. Id facere quia quae dolores dolorem tempore.',
            trainer_id = 2,
            trainer_name = 'Alberta',
            schedule = 'Terças e Sextas, 10 às 13h',
            available_seats = 16,
        ),
    ][:count]
    
#:

def most_popular_courses(count: int) -> List[Course]:
    return [
        Course(
            id = 1,
            category = 'Hotelaria e Turismo',
            price = dec(169),
            name = 'Gestor Turístico',
            summary = 'Et architecto provident deleniti facere repellat nobis iste. Id facere quia quae dolores dolorem tempore.',
            description = 'Et architecto provident deleniti facere repellat nobis iste. Id facere quia quae dolores dolorem tempore.',
            trainer_id = 1,
            trainer_name = 'Osmar', 
            schedule = 'Segundas e Quintas, 17 às 20h',
            available_seats = 40,
        ),
        Course(
            id = 2,
            category = 'Programação em C++',
            price = dec(250),
            name = 'Estruturas de Dados em C++',
            summary = 'Et architecto provident deleniti facere repellat nobis iste. Id facere quia quae dolores dolorem tempore.',
            description = 'Et architecto provident deleniti facere repellat nobis iste. Id facere quia quae dolores dolorem tempore.',
            trainer_id = 4,
            trainer_name = 'Bernardo',
            schedule = 'Terças e Quartas, 17h30 às 20h30',
            available_seats = 20,
        ),
            Course(
            id = 3,
            category = 'Natação',
            price = dec(250),
            name = 'Estilo Borboleta',
            summary = 'Et architecto provident deleniti facere repellat nobis iste. Id facere quia quae dolores dolorem tempore.',
            description = 'Et architecto provident deleniti facere repellat nobis iste. Id facere quia quae dolores dolorem tempore.',
            trainer_id = 2,
            trainer_name = 'Alberta',
            schedule = 'Terças e Sextas, 10 às 13h',
            available_seats = 16,
        ),
    ][:count]
#: 

def get_course_by_id(course_id: int) -> Course | None: 
    courses = available_courses(10000)
    for course in courses:
        if course.id == course.id:
            return course
    return None
#:
