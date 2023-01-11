from dataclasses import dataclass, field
from typing import List
from datetime import datetime

@dataclass
class Movie:
    _id: str
    title: str
    director: str
    year: int
    cast: List[str] = field(default_factory=list)
    series: List[str] = field(default_factory=list)
    last_watched: int = 0
    rating: int = 0
    tags: List[str] = field(default_factory=list)
    description: str = None
    video_link: str = None
    
@dataclass
class User:
    _id: str
    email: str
    password: str
    movies: List[str] = field(default_factory=list)