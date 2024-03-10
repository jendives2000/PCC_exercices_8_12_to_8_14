# Exercises from the book Python Crash Course by Eric Matthes.
# These exercises are about Arbitrary parameters in Functions, including keyword ones.
# -----------------------------------------------------------------------------
# exercise 8-12:
# 1a.  Write a function that accepts a list of items a person wants on a sandwich.
# 1a.1. The function should have one parameter that collects as many items as the function call provides,
# 1a.2. and it should print a summary of the sandwich that’s being ordered.
# 1a.3. Call the function three times, using a different number of arguments each time.

# -----------------------------------------------------------------------------
from icecream import ic

# -----------------------------------------------------------------------------

print("\n\nExercises 8-12:\n-------------------------------------------------\n")


def ordering_sandw(*wanted_items, order_number):  # 1a. & 1a.1.
    summary_sandw = ", ".join(item.title() for item in wanted_items)
    print(  # 1a.2.
        f"\nOrder #{order_number}: Your sandwich is being prepared with:\n\t{summary_sandw}"
    )


# 1a.3.
processing_sandw_1 = ordering_sandw(
    "ketchup", "lettuce", "tomatoes", "onions", order_number=1
)
processing_sandw_2 = ordering_sandw(
    "hummus", "tomatoes", "garlic", "pickles", order_number=2
)
processing_sandw_3 = ordering_sandw(
    "mayonese", "parsley", "yellow cheese", "mustard", order_number=3
)
