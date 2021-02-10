By: Muhammad Waleed Usman
# ETL operations
# Complete the connection URI


connection_uri = "postgresql://repl:password@localhost:5432/datacamp_application"
db_engine = sqlalchemy.create_engine(connection_uri)

# Get user with id 4387
user1 = pd.read_sql("SELECT * FROM rating where rating.user_id=4387", db_engine)

# Get user with id 18163
user2 = pd.read_sql("SELECT * FROM rating where rating.user_id=18163", db_engine)

# Get user with id 8770
user3 = pd.read_sql("SELECT * FROM rating where rating.user_id=8770", db_engine)

# Use the helper function to compare the 3 users
print_user_comparison(user1, user2, user3)



# Complete the transformation function
def transform_avg_rating(rating_data):
  # Group by course_id and extract average rating per course
  avg_rating = rating_data.groupby('course_id').rating.mean()
  # Return sorted average ratings per course
  sort_rating = avg_rating.sort_values(ascending=False).reset_index()
  return sort_rating

def extract_rating_data(db_engine):
  # Group by course_id and extract average rating per course
  rating_data = pd.read_sql("SELECT * FROM rating", db_engine)
  return rating_data

# Extract the rating data into a DataFrame
rating_data = extract_rating_data(db_engine)
# Use transform_avg_rating on the extracted data and print results
avg_rating_data = transform_avg_rating(rating_data)
print(avg_rating_data)