from pydantic import BaseModel, EmailStr, field_validator

class UserCreate(BaseModel):
    name: str  
    email: EmailStr 
    password: str 
    confirm_password: str

    @field_validator('confirm_password')
    def passwords_match(cls, v, values):
        if 'password' in values.data and v != values.data['password']:
            raise ValueError('Passwords do not match')
        return v

class UserLogin(BaseModel):
    email: EmailStr 
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str


from datetime import date

class ExpenseCreate(BaseModel):
    title: str
    amount: float
    category: str
    date: date
    payment_method: str
    description: str | None = None

class ExpenseResponse(BaseModel):
    id: int
    user_id: int
    title: str
    amount: float
    category: str
    date: date
    payment_method: str
    description: str | None = None

class ExpenseUpdate(BaseModel):
    title: str | None = None
    amount: float | None = None
    category: str | None = None
    date: date | None = None
    payment_method: str | None = None
    description: str | None = None