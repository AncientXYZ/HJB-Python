def bookstore_problem(num_books):
    cover_price = 80.25
    discount_rate = 0.40
    shipping_first_book = 5.00
    shipping_other_books = 2.25
    full_price = 80.25

    # Calculate the purchase price with discount and without shipping
    purchase_price_discounted = cover_price * (1 - discount_rate) * num_books

    # Calculate the total shipping cost
    total_shipping_cost = shipping_first_book + (num_books - 1) * shipping_other_books if num_books > 0 else 0

    # Calculate the total wholesale cost
    total_wholesale_cost = purchase_price_discounted + total_shipping_cost

    # Calculate the profit if sold at full price
    profit = (full_price * num_books) - total_wholesale_cost

    return {
        "Purchase Price (Discounted)": purchase_price_discounted,
        "Total Wholesale Cost": total_wholesale_cost,
        "Profit": profit
    }

# Example usage with 60 books:
results = bookstore_problem(60)
print(f"Purchase Price (Discounted) for 60 books: ${results['Purchase Price (Discounted)']:.2f}")
print(f"Total Wholesale Cost for 60 books: ${results['Total Wholesale Cost']:.2f}")
print(f"Profit for 60 books: ${results['Profit']:.2f}")

# To allow the user to enter the number of books and display the profit:
# num_books = int(input("Enter the number of books: "))
# results = bookstore_problem(num_books)
# print(f"Profit for {num_books} books: ${results['Profit']:.2f}")
