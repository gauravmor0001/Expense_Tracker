from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

from app.database import get_db
from app.dependencies import get_current_user
from app.models import Expense, User
from app.schemas import ExpenseCreate, ExpenseResponse


router = APIRouter(
    prefix="/expenses",
    tags=["Expenses"]
)


@router.post(
    "",
    response_model=ExpenseResponse,
    status_code=status.HTTP_201_CREATED
)
def create_expense(
    expense_data: ExpenseCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    new_expense = Expense(
        user_id=current_user.id,
        title=expense_data.title,
        amount=expense_data.amount,
        category=expense_data.category,
        date=expense_data.date,
        payment_method=expense_data.payment_method,
        description=expense_data.description
    )

    try:
        db.add(new_expense)
        db.commit()
        db.refresh(new_expense)

    except SQLAlchemyError:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to save expense"
        )

    return new_expense