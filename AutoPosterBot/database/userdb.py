from pymongo import MongoClient
from typing import Dict, List, Optional
import asyncio
from config import DATABASE_URL, DATABASE_NAME

class Database:
    def __init__(self):
        # Use pymongo for sync MongoDB operations
        self.client = MongoClient(DATABASE_URL)
        self.db = self.client[DATABASE_NAME]
        self.movies_collection = self.db.movies
        
    def save_movie(self, movie_key: str, movie_data: Dict) -> bool:
        """Save new movie to database"""
        try:
            movie_data['_id'] = movie_key
            self.movies_collection.insert_one(movie_data)
            return True
        except Exception as e:
            print(f"Error saving movie: {e}")
            return False
    
    def get_movie(self, movie_key: str) -> Optional[Dict]:
        """Get movie from database"""
        try:
            movie = self.movies_collection.find_one({'_id': movie_key})
            return movie
        except Exception as e:
            print(f"Error getting movie: {e}")
            return None
    
    def add_file_to_movie(self, movie_key: str, file_info: Dict) -> bool:
        """Add new file to existing movie"""
        try:
            self.movies_collection.update_one(
                {'_id': movie_key},
                {'$push': {'files': file_info}}
            )
            return True
        except Exception as e:
            print(f"Error adding file to movie: {e}")
            return False
    
    def update_movie(self, movie_key: str, update_data: Dict) -> bool:
        """Update movie data"""
        try:
            self.movies_collection.update_one(
                {'_id': movie_key},
                {'$set': update_data}
            )
            return True
        except Exception as e:
            print(f"Error updating movie: {e}")
            return False
    
    def delete_movie(self, movie_key: str) -> bool:
        """Delete movie from database"""
        try:
            self.movies_collection.delete_one({'_id': movie_key})
            return True
        except Exception as e:
            print(f"Error deleting movie: {e}")
            return False
    
    def get_all_movies(self) -> List[Dict]:
        """Get all movies from database"""
        try:
            movies = []
            for movie in self.movies_collection.find():
                movies.append(movie)
            return movies
        except Exception as e:
            print(f"Error getting all movies: {e}")
            return []
    
    def search_movies(self, query: str) -> List[Dict]:
        """Search movies by title"""
        try:
            movies = []
            for movie in self.movies_collection.find({
                'title': {'$regex': query, '$options': 'i'}
            }):
                movies.append(movie)
            return movies
        except Exception as e:
            print(f"Error searching movies: {e}")
            return []
    
    def get_movies_by_language(self, language: str) -> List[Dict]:
        """Get movies by language"""
        try:
            movies = []
            for movie in self.movies_collection.find({
                'language': {'$regex': language, '$options': 'i'}
            }):
                movies.append(movie)
            return movies
        except Exception as e:
            print(f"Error getting movies by language: {e}")
            return []
    
    def get_movies_by_year(self, year: str) -> List[Dict]:
        """Get movies by year"""
        try:
            movies = []
            for movie in self.movies_collection.find({'year': year}):
                movies.append(movie)
            return movies
        except Exception as e:
            print(f"Error getting movies by year: {e}")
            return []
    
    def check_file_exists(self, movie_key: str, file_caption: str) -> bool:
        """Check if file already exists in movie"""
        try:
            movie = self.movies_collection.find_one({
                '_id': movie_key,
                'files.caption': file_caption
            })
            return movie is not None
        except Exception as e:
            print(f"Error checking file existence: {e}")
            return False
    
    def close(self):
        """Close database connection"""
        self.client.close()
