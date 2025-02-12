"""Schema for Sentiment_Analysis"""

from pydantic import BaseModel


class Analysis(BaseModel):
    """
    Sentiment Analysis shcema.
    """
    review: list[str]
