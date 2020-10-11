from typing import Tuple

from app import schemas
from app.crud import crud_comment


async def create_test_comment(
    article: schemas.ArticleDB, author: schemas.UserDB
) -> Tuple:
    comment_body = "His name was my name too."
    comment_in = schemas.CommentInCreate(body="His name was my name too.")
    comment_id = await crud_comment.create(
        payload=comment_in, author_id=author.id, article_id=article.id
    )
    return comment_body, comment_id
