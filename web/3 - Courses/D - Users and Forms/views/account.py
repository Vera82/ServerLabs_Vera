from datetime import date
from fastapi import APIRouter, Request
from fastapi_chameleon import template

from data.models import Student
from common import (
    base_viewmodel_with,
    is_valid_name,
    form_field_as_str,
)

router = APIRouter()

@router.get('/account/register')                            # type: ignore
@template()
async def register():
    return register_viewmodel()
#:

def register_viewmodel():
    return base_viewmodel_with({
        'name': '',
        'email': '',
        'password': '',
        'date_of_birth': '',
        'min_date': '1920-01-01',
        'max_date': date.today(),
        'checked': False,
    })
#:
    
@router.post('/account/register')                            # type: ignore
@template(template_file='account/register.pt')
async def post_register(request: Request):
    return register_viewmodel(request)
#:   
 
async def post_register_viewmodel(request: Request):  
    form_data = await request.form()
    name = form_field_as_str(form_data, 'name')
    email = form_data['email_addr']
    
    if not is_valid_name(name):
        error, error_msg = True, 'Invalid name!'
        
    else: 
        error, error_msg = False, ''
        
    return base_viewmodel_with({
        'error': error,
        'error_msg': error_msg,
        'name': name,
    })
#:   
    
@router.get('/account/login')                            # type: ignore
@template()
async def login():
       return login_viewmodel()
#:

def login_viewmodel():
    return base_viewmodel_with({
        'error': False,
        'error_msg': 'There was an error with your data. Please try again.'
    })
#:

@router.get('/account')                            # type: ignore
@template()
async def index():
    return account_viewmodel()
#:

def account_viewmodel():
    student = Student(
        id = 15_001,
        name = 'Alberto Antunes',
        email = 'alb@mail.com',
        password = 'abc',
        birth_date = date(1995, 2, 3),
    )
    return base_viewmodel_with({
        'name': student.name,
        'email': student.email,
    })
#: