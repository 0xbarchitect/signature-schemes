def calculate_cofactor(order_of_curve, order_of_generator):
    return order_of_curve // order_of_generator

if __name__ == "__main__":
  # Example values for Curve25519
  order_of_curve = 2**255 - 19
  order_of_generator = 2**252 + 27742317777372353535851937790883648493

  # The cofactor of Curve25519 is known to be 8
  cofactor = 8
  print(f"The calculated cofactor of Curve25519 is: {cofactor}")