from fastapi import APIRouter, Request
from starlette.requests import Request
from fastapi_chameleon import template

router = APIRouter()

@router.get('/')
@template()
async def index(course1: str = 'N/D'):
    return {
        'num_courses': 99,
        'num_students': 2315,
        'num_trainers': 23,
        'num_events': 159,
        'popular_courses': [
            {
                'id': 1,
                'category': 'Hotelaria e Turismo',
                'price': 169,
                'name': 'Gestor Turístico',
                'summary': 'Et architecto provident deliniti facere repellat nobis iste. If facere quia quae dolores dolorem tempore.',
                'trainer_id': 1,
                'trainer_name': 'Osmar',
            },
            {
                'id': 2,
                'category': 'Programação em C++',
                'price': 250,
                'name': 'Estrutura de Dados em C++',
                'summary': 'Et architecto provident deliniti facere repellat nobis iste. If facere quia quae dolores dolorem tempore.',
                'trainer_id': 4,
                'trainer_name': 'Bernardo',
            },
            {
                'id': 3,
                'category': 'Natação',
                'price': 250,
                'name': 'Estilo borboleta',
                'summary': 'Et architecto provident deliniti facere repellat nobis iste. If facere quia quae dolores dolorem tempore.',
                'trainer_id': 2,
                'trainer_name': 'Alberta',
            },  
        ],
        'selected trainers': [
            {
                'id': 2,
                'name': 'Alberta Almeida',
                'expertise': 'Programação Web',
                'presentation': 'Et architecto provident deliniti facere repellat nobis iste. If facere quia quae dolores dolorem tempore.',
                'twitter': 'https://www.twitter.com/alberta_almeida',
                'facebook': 'https://www.facebook.com/albertaalmeida',
                'instagram': 'https://www.instagram.com/albermeida',
                'linkedin': 'https://www.twitter.com/prof_alberta',
            },  
            {
                'id': 3,
                'name': 'Augusto Avillez',
                'expertise': 'Marketing',
                'presentation': 'Et architecto provident deliniti facere repellat nobis iste. If facere quia quae dolores dolorem tempore.',
                'twitter': 'https://www.twitter.com/augusto_avillez',
                'facebook': 'https://www.facebook.com/augustoavillez',
                'instagram': 'https://www.instagram.com/augillez',
                'linkedin': 'https://www.twitter.com/prof_augusto',
            },  
            {
                'id': 4,
                'name': 'Osmar Tello',
                'expertise': 'Gestão de Conteúdos',
                'presentation': 'Et architecto provident deliniti facere repellat nobis iste. If facere quia quae dolores dolorem tempore.',
                'twitter': 'https://www.twitter.com/osmar_tello',
                'facebook': 'https://www.facebook.com/osmartello',
                'instagram': 'https://www.instagram.com/osmello',
                'linkedin': 'https://www.twitter.com/prof_osmar',
            },  
        ],
    }
#:

@router.get('/about')
@template()
async def about():
    return {
        'num_courses': 99,
        'num_students': 2315,
        'num_trainers': 23,
        'num_events': 159,
        'testimonials': [
            {
                'user_id': 239,
                'user_name': 'Saul Goodman',
                'user_occupation': 'CEO & Founder',
                'text': 'Et architecto provident deliniti facere repellat nobis iste. If facere quia quae dolores dolorem tempore.',
            }, 
            {
                'user_id': 1001,
                'user_name': 'Sarah Wilson',
                'user_occupation': 'Designer',
                'text': 'Et architecto provident deliniti facere repellat nobis iste. If facere quia quae dolores dolorem tempore.',
            },   
            {
                'user_id': 704,
                'user_name': 'Jena Karlis',
                'user_occupation': 'Store Owner',
                'text': 'Et architecto provident deliniti facere repellat nobis iste. If facere quia quae dolores dolorem tempore.',
            },   
            {
                'user_id': 1589,
                'user_name': 'John Larson',
                'user_occupation': 'Entrepreneur',
                'text': 'Et architecto provident deliniti facere repellat nobis iste. If facere quia quae dolores dolorem tempore.',
            }, 
        ],        
    }
#: