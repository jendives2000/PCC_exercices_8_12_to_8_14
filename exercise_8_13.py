# Exercises from the book Python Crash Course by Eric Matthes.
# These exercises are about Arbitrary parameters in Functions, including keyword ones.
# -----------------------------------------------------------------------------
# Exercise 8-13:
# 2a. Build a profile of yourself by calling build_profile(), using:
# 2a.1. your first and last names
# 2a.2. and three other key-value pairs that describe you.

# -----------------------------------------------------------------------------
from icecream import ic

# -----------------------------------------------------------------------------

print("\n\nExercises 8-13:\n-------------------------------------------------\n")


# 2a. Build a profile of yourself by calling build_profile(), using:
def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info["first name"] = first
    user_info["last name"] = last
    return user_info


# 2a.1. your first and last names
# 2a.2. and three other key-value pairs that describe you.
build_profile_1 = build_profile(
    "Jean-Yves",
    "TRAN",
    job="Creative Python Developer",
    status="married",
    education="Master Degree",
)

for key, value in build_profile_1.items():
    print(f"{key.title()}: {value.title()}\n")
